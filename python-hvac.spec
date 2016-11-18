%define srcname hvac
%define version 0.2.16
%define unmangled_version 0.2.16
%define release 1

Summary: HashiCorp Vault API client
Name: python-hvac
Version: %{version}
Release: %{release}
Source0: %{srcname}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{srcname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ian Unruh <ianunruh@gmail.com>
BuildRequires: python-setuptools python
Url: https://github.com/ianunruh/hvac

%description
UNKNOWN

%prep
%setup -n %{srcname}-%{unmangled_version} -n %{srcname}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
