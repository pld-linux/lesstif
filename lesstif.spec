Summary:	LessTif - source compatible library with OSF/Motif® 1.2
Name:		lesstif
Version:	0.88.1
Release:	1
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.lesstif.org/pub/hungry/lesstif/srcdist/%{name}-%{version}.tar.gz
#Source0:	ftp://ftp.lesstif.org/pub/hungry/lesstif/srcdist/%{name}-current.tar.gz
Patch0:		lesstif.optflags.patch
Patch1:		lesstif-mwmrc_path.patch
Icon:		lesstif-realsmall.gif
BuildPrereq:	XFree86-devel
BuildPrereq:	man2html
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	lesstif-M20
Obsoletes:	lesstif-M12

%define _prefix /usr/X11R6

%description
Lesstif is an API compatible clone of the Motif 1.2 toolkit.
Currently Lesstif is partially implemented with most of the API in place.
Saying this a lot of the internal functionality is still missing.  The
primary objectives have been to develop the widget code of the Lesstif
Toolkit.

%package mwm
Summary:	Lesstif (Motif) window manager clone based on fvwm
Copyright:	GPL
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Requires:	%{name} = %{version}

%description mwm
A BETA release of mwm.  It is derived from fvwm, with a new parser that
understands mwmrc syntax, and a general understanding of Mwm resources.

%package clients
Summary:	Lesstif clients
Copyright:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Requires:	%{name} = %{version}

%description clients
Uil and xmbind.

%package devel
Summary:	Header files for Lesstif/Motif 1.2 development
Copyright:	LGPL
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package contains the lesstif header files required to develop Motif 1.2
based applications.

%package static
Summary:	Static Lesstif library
Copyright:	LGPL
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
This package contains the lesstif static libraries.

%prep
%setup -q
#%setup -q -n %{name}-current
%patch0 -p1
%patch1 -p1

#find . -name CVS -exec rm -rf {} \; 2> /dev/null ||

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=%{_prefix} \
	--enable-shared \
	--enable-static \
	--enable-production \
	--disable-debug \
	--disable-scrollbar-verbose \
	--with-editres \
	--with-xdnd \
	--enable-build-12 \
	--enable-default-12 \
	--disable-build-20 \
	--disable-default-20
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11
make install \
	DESTDIR=$RPM_BUILD_ROOT \
	mwmddir=/etc/X11/mwm \
	man1dir=%{_mandir}/man1 \
	man3dir=%{_mandir}/man3 \
	man5dir=%{_mandir}/man5 \
	htmldir=/home/httpd/html/Lesstif-%{version}

# correction locations some files files
rm -rf $RPM_BUILD_ROOT{%{_includedir}/{Mrm,Xm},%{_libdir}/lib*}

mv $RPM_BUILD_ROOT%{_prefix}/LessTif/Motif1.2/include/* $RPM_BUILD_ROOT%{_includedir}
mv $RPM_BUILD_ROOT%{_prefix}/LessTif/Motif1.2/lib/lib* $RPM_BUILD_ROOT%{_libdir}

rm -f doc/INSTALL.html

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	clients/Motif-1.2/mwm/README \
	AUTHORS BUG-REPORTING CREDITS CURRENT_NOTES ChangeLog \
	KNOWN_BUGS NEWS NOTES README RELEASE-POLICY TODO \
	doc/*.txt

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post mwm
if [ -L /etc/X11/mwm ]; then
	rm -rf /etc/X11/mwm
	rm -rf /usr/X11R6/lib/X11/mwm/*
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/lib*.so.*.*
%{_mandir}/man1/lesstif.1*

%files mwm
%defattr(644,root,root,755)
%doc clients/Motif-1.2/mwm/README*
%dir /etc/X11/mwm
%config /etc/X11/mwm/*
%attr(755,root,root) %{_bindir}/mwm

%config %{_libdir}/X11/app-defaults/*

%{_mandir}/man1/mwm.1*
%{_mandir}/man5/mwmrc.5*

%files clients
%defattr(644,root,root,755)
%doc doc/UIL.txt*
%attr(755,root,root) %{_bindir}/uil
%attr(755,root,root) %{_bindir}/xmbind
%{_mandir}/man1/xmbind.1*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,BUG-REPORTING,CREDITS,CURRENT_NOTES,ChangeLog,KNOWN_BUGS,NEWS}.gz
%doc {NOTES,README,RELEASE-POLICY,TODO}.gz
%doc doc/*.txt* doc/*.html doc/www.lesstif.org/{images/*gif,*html}

%docdir /home/httpd/html/Lesstif-%{version}
%doc /home/httpd/html/Lesstif-%{version}/*

%attr(755,root,root) %{_libdir}/lib*.so

%{_includedir}/Mrm
%{_includedir}/Xm

%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Fri May 28 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.88.1-1]
- based on RH spec,
- spec rewrited by PLD team.
