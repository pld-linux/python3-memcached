#
# Conditional build:
%bcond_with	tests	# unit tests (not in sdist)

%define		module	memcached
Summary:	Pure Python memcached client
Summary(pl.UTF-8):	Klient memcached w czystym Pythonie
Name:		python-%{module}
# keep 1.59 here for python2 support
Version:	1.59
Release:	1
# see memcache.py /__license__
License:	PSF
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/python-memcached/
Source0:	https://files.pythonhosted.org/packages/source/p/python-memcached/%{name}-%{version}.tar.gz
# Source0-md5:	fe5a7c66da01b0c4f5223a4db8cb8659
URL:		https://pypi.org/project/python-memcached/
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-coverage
BuildRequires:	python-hacking
BuildRequires:	python-mock
BuildRequires:	python-nose
BuildRequires:	python-six >= 1.4.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This software is a 100% Python interface to the memcached memory cache
daemon. It is the client side software which allows storing values in
one or more, possibly remote, memcached servers.

%description -l pl.UTF-8
Ten pakiet to napisany w 100% w Pythonie interfejs do demona pamięci
podręcznej memcached. Jest to biblioteka strony klienckiej, która
pozwala przechowywać wartości w jednym lub większej liczbie, także
zdalnych, serwerów memcached.

%prep
%setup -q

%build
%py_build

%if %{with tests}
nosetests-%{py_ver}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md
%{py_sitescriptdir}/memcache.py[co]
%{py_sitescriptdir}/python_memcached-%{version}-py*.egg-info
