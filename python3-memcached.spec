#
# Conditional build:
%bcond_with	tests	# unit tests (tests/utils.py missing in sdist)

%define		module	memcached
Summary:	Pure Python memcached client
Summary(pl.UTF-8):	Klient memcached w czystym Pythonie
Name:		python3-%{module}
Version:	1.62
Release:	1
License:	PSF v2
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/python-memcached/
Source0:	https://files.pythonhosted.org/packages/source/p/python-memcached/python-memcached-%{version}.tar.gz
# Source0-md5:	390ddff32f7ee1ae7166b3486c44de9f
URL:		https://pypi.org/project/python-memcached/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pynose
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
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
%setup -q -n python-memcached-%{version}

%build
%py3_build

%if %{with tests}
nosetests-%{py3_ver} tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md SECURITY.md
%{py3_sitescriptdir}/memcache.py
%{py3_sitescriptdir}/__pycache__/memcache.cpython-*.py[co]
%{py3_sitescriptdir}/python_memcached-%{version}-py*.egg-info
