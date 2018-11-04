Name:           anaconda-installclass-tigeros
Version:        29
Release:        1%{?dist}
Summary:        @DISTRO_NAME@ installclass for Anaconda

License:        GPLv2+
URL:            https://github.com/RITlug/anaconda-installclass-tigeros
Source0:        tigeros.py

BuildRequires:  anaconda-core
BuildRequires:  python3-devel

Requires:       anaconda-core
Supplements:    (tigeros-release and anaconda-core)

%description
This package contains the installclass for TigerOS for
Anaconda.

%install
install -Dpm 0644 %{SOURCE0} %{buildroot}%{python3_sitearch}/pyanaconda/installclasses/tigeros.py

%files
%{python3_sitearch}/pyanaconda/installclasses/tigeros.py
%{python3_sitearch}/pyanaconda/installclasses/__pycache__/tigeros.*

%changelog
* Sun Nov 04 2018 Tim Zabel <tjz8659@rit.edu> - 29-1
- Fedora 29 build

* Wed May 16 2018 Tim Zabel <tjz8659@rit.edu> - 28-1
- Fedora 28 build
- removed unneeded build and prep segments
