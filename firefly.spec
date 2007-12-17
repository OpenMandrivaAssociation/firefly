%define name firefly
%define version 1.1.1
%define release %mkrel 3

Summary: Multi-user professional help desk system
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Communications
URL: http://somwhere.com
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

