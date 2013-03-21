Name: svn2rpm
Version: __VERSION__
Release: 1
Summary: Build RPMs from SVN
Group: Applications/System
License: GPL
URL: https://github.com/ImmobilienScout24/svn2rpm
Source0: %{name}-%{version}.tar.gz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
Requires: rpmdevtools, rpm-build
Requires: subversion

%description
Export from SVN and build an SRC RPM package. Requirements:
- SPEC file must be part of files checked out from SVN
- VARIANT 1: SVN contains SPEC file and optionally SOURCES
- VARIANT 2: SVN is exploded SOURCE0

%prep
%setup -q

%install
umask 0002
rm -rf $RPM_BUILD_ROOT
install -m 0755 svn2rpm -D $RPM_BUILD_ROOT/usr/bin/svn2rpm

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/bin/svn2rpm
