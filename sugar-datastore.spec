# NOTE: Do not edit, file was generated by jhconvert

Name: sugar-datastore
Version: 0.83.3
Release: %mkrel 1
Summary: Datastore service for Sugar
License: GPL
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/glucose/sugar-datastore/sugar-datastore-0.83.3.tar.bz2

Requires: sugar-base >= 0.83.3
Requires: python-dbus  
Requires: xapian-bindings-python  
Requires: python  
Requires: python-cjson  

BuildRequires: libpython-devel  

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package contains a simple log like datastore able to connect with multiple
backends. The datastore supports connecting and disconnecting from backends
on the fly to help the support the limit space/memory characteristics and
the fact that network services may become unavailable at times.

%prep
%setup -q -n sugar-datastore-0.83.3


# eliminate %%configure's "clever" behaviour
%define __libtoolize true

%build
%configure 
make 

%install
rm -rf %{buildroot}
make  \
	DESTDIR=%{buildroot} \
	install


%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/dbus*/services/*
%{python_sitelib}/*
%doc LICENSE.GPL README.txt

