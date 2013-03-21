Name: test1
Version: 19
Release: 75
Summary: test rpm for variant 1 without download
Group: Applications/System
License: GPL
URL: https://github.com/ImmobilienScout24/svn2rpm
Source0: file1.txt
Source1: file2.txt
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

%description
test rpm for variant1: spec and sources together

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -m 0644 -t $RPM_BUILD_ROOT %{SOURCE0} %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/
