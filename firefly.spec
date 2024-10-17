%define name firefly
%define version 1.1.1
%define release 8

Summary: Multi-user professional help desk system
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Communications
URL: https://somwhere.com
BuildRoot: %{_tmppath}/%{name}
Requires: mod_php, php-gd, php-pgsql, postgresql, postgresql-server
Buildarch: noarch

%description
Firefly is a multi-user professional help desk system with several additional
applications including company and contact management, knowledge database 
management, and contracts management. 
Firefly is also an application framework providing services such as
user authentication, profile management, and database abstraction.
It is designed on PHP3, postgreSQL, and Apache.

Any new module profits firefly's user authentification and framework services.
A library of generic functions and a unified structure of the folders
make it possible to develop ew modules easily.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/www/html/firefly
cp -avf images include modules templates *.php *.gif *.css $RPM_BUILD_ROOT/var/www/html/firefly

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README README-FR CREDITS doc_* DocUser.txt INSTALL LICENSE INSTALL-FR GPL GPL-FR dumps/*
/var/www/html/firefly



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-7mdv2011.0
+ Revision: 618286
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.1.1-6mdv2010.0
+ Revision: 428761
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.1.1-5mdv2009.0
+ Revision: 245166
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.1.1-3mdv2008.1
+ Revision: 125023
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import firefly


* Mon Mar 01 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.1.1-3mdk
- Own dir

* Tue Jan 20 2004 Antoine Ginies <aginies@bi.mandrakesoft.com> 1.1.1-2mdk
- move dumps directory to %%doc
- add require postgresql-server

* Mon Jan 19 2004 aginies <aginies@mandrakesoft.com> 1.1.1-1mdk
- first release ?
