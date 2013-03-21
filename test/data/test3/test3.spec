Name: test3
Version: 19
Release: 75
Summary: test rpm for variant 2
Group: Applications/System
License: GPL
URL: https://github.com/ImmobilienScout24/svn2rpm
Source: %{name}-%{version}.tar.gz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

%description
test rpm for variant2: spec and exploded Source0 together

%prep
%setup


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -m 0644 -t $RPM_BUILD_ROOT file1.txt file2.txt

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/
