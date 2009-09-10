Summary:	Write tests that implement the Test Anything Protocol
Name:		libtap
Version:	1.01
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://people.freebsd.org/~nik/public_distfiles/tap-%{version}.tar.gz
# Source0-md5:	5b22a1e94de03c7210a7df71fa18a556
URL:		http://jc.ngo.org.uk/trac-bin/trac.cgi/wiki/LibTap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tap library provides functions for writing test scripts that
produce output consistent with the Test Anything Protocol. A test
harness that parses this protocol can run these tests and produce
useful reports indi- cating their success or failure.

%package devel
Summary:	Header files for tap library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki tap
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for tap library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tap.

%package static
Summary:	Static tap library
Summary(pl.UTF-8):	Statyczna biblioteka tap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static tap library.

%description static -l pl.UTF-8
Statyczna biblioteka tap.

%prep
%setup -q -n tap-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libtap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtap.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/tap.h
%{_libdir}/libtap.la
%{_libdir}/libtap.so
%{_mandir}/man3/tap.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libtap.a
