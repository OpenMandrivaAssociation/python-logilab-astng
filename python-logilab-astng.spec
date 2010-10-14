%define module	logilab-astng
%define name	python-%{module}
%define version 0.20.3
%define release %mkrel 1

Summary:	Extension of compiler.ast Python module
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://ftp.logilab.org/pub/astng/%{module}-%{version}.tar.gz
License:	GPLv2+
Group:		Development/Python
Url:		http://www.logilab.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python-logilab-common >= 0.49.0
BuildArch:	noarch
BuildRequires:	python-setuptools
%py_requires -d

%description
This module provides a common base representation of Python source
code for Logilab projects such as pylint. It extends class defined in
the compiler.ast module with some additional methods and attributes

%prep
%setup -q -n %{module}-%{version}

%build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog
%py_sitedir/logilab*
%exclude %py_sitedir/logilab/astng/test/
%py_sitedir/*.egg-info
