Summary:	C++ wrappers for GooCanvas 2 library
Summary(pl.UTF-8):	Interfejsy C++ dla biblioteki GooCanvas 2
Name:		goocanvasmm2
Version:	1.90.9
Release:	4
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/goocanvasmm/1.90/goocanvasmm-%{version}.tar.xz
# Source0-md5:	f10ce3f1f97ee6906a741ef88c815215
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	doxygen
BuildRequires:	glibmm-devel >= 2.14.2
BuildRequires:	goocanvas2-devel >= 2.0.1
BuildRequires:	gtkmm3-devel >= 3.0.0
BuildRequires:	libtool
BuildRequires:	mm-common >= 0.9.5
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glibmm >= 2.14.2
Requires:	goocanvas2 >= 2.0.1
Requires:	gtkmm3 >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for GooCanvas 2 library.

%description -l pl.UTF-8
Interfejsy C++ dla biblioteki GooCanvas 2.

%package devel
Summary:	Header files for goocanvasmm 2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki goocanvasmm 2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.14.2
Requires:	goocanvas2-devel >= 2.0.1
Requires:	gtkmm3-devel >= 3.0.0

%description devel
Header files for goocanvasmm 2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki goocanvasmm 2.

%package static
Summary:	Static goocanvasmm 2 library
Summary(pl.UTF-8):	Statyczna biblioteka goocanvasmm 2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static goocanvasmm 2 library.

%description static -l pl.UTF-8
Statyczna biblioteka goocanvasmm 2.

%package apidocs
Summary:	goocanvasmm 2 API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki goocanvasmm 2
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for goocanvasmm 2 library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki goocanvasmm 2.

%prep
%setup -q -n goocanvasmm-%{version}

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgoocanvasmm-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoocanvasmm-2.0.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgoocanvasmm-2.0.so
%{_libdir}/goocanvasmm-2.0
%{_includedir}/goocanvasmm-2.0
%{_pkgconfigdir}/goocanvasmm-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgoocanvasmm-2.0.a

%files apidocs
%defattr(644,root,root,755)
# it can't be compressed
%{_docdir}/goocanvasmm-2.0
%{_datadir}/devhelp/books/goocanvasmm-2.0
