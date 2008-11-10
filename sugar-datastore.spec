Name: sugar-datastore
Version: 0.82.1
Release: %mkrel 1
Summary: Sugar Datastore

Group: Development/Python
License: GPLv2+
URL: http://dev.laptop.org/
Source0: http://dev.laptop.org/pub/sugar/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

BuildRequires: python

Requires: gnome-python-gnomevfs
Requires: xapian-bindings-python
Requires: python-sqlite2
Requires: python-cjson

%description
sugar-datastore is a simple log like datastore able to connect with multiple
backends. The datastore supports connectionig and disconnecting from
backends on the fly to help the support the limit space/memory
characteristics of the OLPC system and the fact that network services
may become unavailable at times

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE.GPL README.txt
%{python_sitelib}/*
%{_bindir}/*
%{_datadir}/dbus-1/services/*.service

