%define module	logilab-astng

# Depenedency geenrator finds too many abi deps here
%define __noautoreq 'python\\(abi\\).*'

Summary:	Extension of compiler.ast Python module
Name:		python-%{module}
Version:	0.24.3
Release:	2
Source0:	http://download.logilab.org/pub/astng/logilab-astng-%{version}.tar.gz
License:	GPLv2+
Group:		Development/Python
Url:		https://www.logilab.org/
Requires:	python-logilab-common >= 0.53.0
Requires:	python(abi) = %{py_ver}
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
This module provides a common base representation of Python source
code for Logilab projects such as pylint. It extends class defined in
the compiler.ast module with some additional methods and attributes

%prep
%setup -q -n %{module}-%{version}

%build

%install
%__python setup.py install --root=%{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog
%py_sitedir/logilab*


%changelog
* Thu Jan 12 2012 Lev Givon <lev@mandriva.org> 0.23.1-1mdv2012.0
+ Revision: 760525
- Update to 0.23.1.

* Thu Jul 28 2011 Lev Givon <lev@mandriva.org> 0.22.0-1
+ Revision: 692095
- Update to 0.22.0.

* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.21.1-1
+ Revision: 636245
- update to new version 0.21.1

* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.21.0-1mdv2011.0
+ Revision: 603069
- update to new version 0.21.0

* Mon Nov 08 2010 Funda Wang <fwang@mandriva.org> 0.20.3-2mdv2011.0
+ Revision: 594926
- rebuild for py2.7

* Thu Oct 14 2010 Lev Givon <lev@mandriva.org> 0.20.3-1mdv2011.0
+ Revision: 585620
- Update to 0.20.3.

* Mon Sep 13 2010 Lev Givon <lev@mandriva.org> 0.20.2-1mdv2011.0
+ Revision: 578046
- Update to 0.20.2.

* Fri May 28 2010 Lev Givon <lev@mandriva.org> 0.20.1-1mdv2011.0
+ Revision: 546542
- Update to 0.20.1.

* Thu Apr 01 2010 Lev Givon <lev@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 530556
- Update to 0.20.0.

* Mon Dec 21 2009 Lev Givon <lev@mandriva.org> 0.19.3-1mdv2010.1
+ Revision: 480708
- Update to 0.19.3.

* Sun Dec 20 2009 Lev Givon <lev@mandriva.org> 0.19.2-1mdv2010.1
+ Revision: 480301
- Update to 0.19.2.

* Thu Nov 12 2009 Lev Givon <lev@mandriva.org> 0.19.1-1mdv2010.1
+ Revision: 465474
- Update to 0.19.1.

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.19.0-2mdv2010.0
+ Revision: 442301
- rebuild

* Sun Apr 19 2009 Lev Givon <lev@mandriva.org> 0.19.0-1mdv2009.1
+ Revision: 368050
- Update to 0.19.0.

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 0.17.4-1mdv2009.1
+ Revision: 324271
- New upstream release

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.17.3-2mdv2009.1
+ Revision: 323759
- rebuild

* Tue Nov 04 2008 Lev Givon <lev@mandriva.org> 0.17.3-1mdv2009.1
+ Revision: 299694
- Update to 0.17.3.

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.17.2-4mdv2009.0
+ Revision: 259654
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.17.2-3mdv2009.0
+ Revision: 247500
- rebuild

* Tue Feb 19 2008 Lev Givon <lev@mandriva.org> 0.17.2-1mdv2008.1
+ Revision: 172407
- Update to 0.17.2.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 09 2007 Lev Givon <lev@mandriva.org> 0.17.1-1mdv2008.0
+ Revision: 50547
- Update to 0.17.1.

* Tue Apr 17 2007 Lev Givon <lev@mandriva.org> 0.17.0-1mdv2008.0
+ Revision: 13857
- Import python-logilab-astng



* Wed Mar 21 2007 Lev Givon <lev@mandriva.org> 0.17.0-1mdv2007.0
- Initial Mandriva package.

