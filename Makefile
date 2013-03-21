TOPLEVEL := svn2rpm svn2rpm.spec
GITREV := HEAD

VERSION := $(shell cat VERSION 2>/dev/null)
REVISION := "$(shell git rev-list $(GITREV) -- $(TOPLEVEL) 2>/dev/null| wc -l)$(EXTRAREV)"
PV = svn2rpm-$(VERSION)

.PHONY: all deb srpm clean rpm info debinfo rpminfo

all: deb rpm
	ls -l dist/*.deb dist/*.rpm

deb: clean
	mkdir -p dist build/deb/usr/bin build/deb/usr/share/doc/svn2rpm build/deb/usr/share/lintian/overrides build/deb/DEBIAN
	install -m 0755 svn2rpm build/deb/usr/bin/svn2rpm
	install -m 0644 DEBIAN/* build/deb/DEBIAN
	sed -i -e s/__VERSION__/$(VERSION).$(REVISION)/ build/deb/usr/bin/svn2rpm
	sed -i -e s/__VERSION__/$(VERSION).$(REVISION)/ build/deb/DEBIAN/control
	mv build/deb/DEBIAN/copyright build/deb/usr/share/doc/svn2rpm/copyright
	mv build/deb/DEBIAN/overrides build/deb/usr/share/lintian/overrides/svn2rpm
	chmod -R go-w build # remove group writeable in case you have it in your umask
	find build/deb -type f -name \*~ | xargs rm -vf
	fakeroot dpkg -b build/deb dist
	lintian --quiet -i dist/*deb

srpm: clean
	mkdir -p dist build/$(PV) build/BUILD
	cp -r $(TOPLEVEL) Makefile build/$(PV)
	mv build/$(PV)/*.spec build/
	sed -i -e s/__VERSION__/$(VERSION)/ -e /^Release/s/$$/.$(REVISION)/ build/*.spec
	sed -i -e s/__VERSION__/$(VERSION).$(REVISION)/ build/$(PV)/svn2rpm
	tar -czf build/$(PV).tar.gz -C build $(PV)
	rpmbuild --define="_topdir $(CURDIR)/build" --define="_sourcedir $(CURDIR)/build" --define="_srcrpmdir $(CURDIR)/dist" --nodeps -bs build/*.spec

rpm: srpm
	ln -svf ../dist build/noarch
	rpmbuild --nodeps --define="_topdir $(CURDIR)/build" --define="_rpmdir %{_topdir}" --rebuild $(CURDIR)/dist/*.src.rpm
	echo -e '\n\n\n\n\nWARNING! THIS RPM IS NOT INTENDED FOR PRODUCTION USE. PLEASE USE rpmbuild --rebuild dist/*.src.rpm TO CREATE A PRODUCTION RPM PACKAGE!\n\n\n\n\n'

info: rpminfo debinfo

debinfo: deb
	dpkg-deb -I dist/*.deb

rpminfo: rpm
	rpm -qip dist/*.noarch.rpm

debrepo: deb
	/data/mnt/is24-ubuntu-repo/putinrepo.sh dist/*.deb

rpmrepo: rpm
	echo "##teamcity[buildStatus text='{build.status.text} RPM Version $(shell rpm -qp dist/*src.rpm --queryformat "%{VERSION}-%{RELEASE}")']"
	repoclient uploadto "$(TARGET_REPO)" dist/*.rpm

clean:
	rm -Rf dist/*.rpm dist/*.deb build

# todo: create debian/RPM changelog automatically, e.g. with git-dch --full --id-length=10 --ignore-regex '^fixes$' -S -s 68809505c5dea13ba18a8f517e82aa4f74d79acb src doc *.spec

