# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details
%define _disable_ld_no_undefined 1

Name:		sugar-datastore
Version:	0.108.1
Release:	1
Summary:	Datastore service for Sugar
License:	GPL
Group:		Graphical desktop/Other
Url:		http://sugarlabs.org/

Source0:	http://download.sugarlabs.org/sources/sucrose/glucose/sugar-datastore/sugar-datastore-%{version}.tar.xz

Requires:	python2-dbus  
Requires:	python2  
Requires:	python2-cjson  
Requires:	sugar-base >= 0.88.0
Requires:	xapian-bindings-python  

BuildRequires:	python2-devel  


%description
This package contains a simple log like datastore able to connect with multiple
backends. The datastore supports connecting and disconnecting from backends
on the fly to help the support the limit space/memory characteristics and
the fact that network services may become unavailable at times.

%prep
%setup -q


%build
%define __libtoolize true
%configure
%make

%install
%makeinstall_std


%files 
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_bindir}/*
%{_datadir}/dbus*/services/*
%{python2_sitelib}/*
%doc AUTHORS COPYING NEWS README

