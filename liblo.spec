Summary:	Open Sound Control library
Name:		liblo
Version:	0.28
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/liblo/%{name}-%{version}.tar.gz
# Source0-md5:	e2a4391a08b49bb316c03e2034e06fa2
URL:		http://liblo.sf.net
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	doxygen
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liblo is an implementation of the Open Sound Control protocol for
POSIX systems.

%package devel
Summary:	Header files for liblo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for liblo.

%prep
%setup -q

%{__sed} -i 's/-Werror//g' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
#%doc doc/html/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/lo
%{_pkgconfigdir}/*.pc

