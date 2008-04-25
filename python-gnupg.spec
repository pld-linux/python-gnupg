%define		module	gnupg
Summary:	A Python module for the GnuPG
Summary(pl.UTF-8):	Moduł Pythona do GnuPG
Name:		python-%{module}
Version:	0.3.2
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/py-gnupg/GnuPGInterface-0.3.2.tar.gz
# Source0-md5:	d4627d83446f96bd8c22f8d15db3f7c2
URL:		http://py-gnupg.sourceforge.net/
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuPG interface for Python.

%description -l pl.UTF-8
Interfejs do GnuPG dla Pythona.

%prep
%setup -q -n GnuPGInterface-%{version}
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
