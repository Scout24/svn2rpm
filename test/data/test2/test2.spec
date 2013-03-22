Name: test2
Version: 19
Release: 75
Summary: test rpm for variant 1 with download
Group: Applications/System
License: GPL
URL: https://github.com/ImmobilienScout24/svn2rpm
# simple example for test. 
# Normally you would have Source0: http:/..../%{name}-%{version}.tar.gz  and
# then you could either put the tar.gz next to this spec file or have svn2rpm
# download it (if spectool is available)
Source0: file1.txt
# download our logo for testing, hosted in imgur because github forces all requests to HTTPS which can lead to wget / SSL errors
Source1: http://i.imgur.com/NWBidnZ.png
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

%description
test rpm for variant1: spec and sources together, some sources need download

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -m 0644 -t $RPM_BUILD_ROOT %{SOURCE0} %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/
