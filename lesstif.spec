Summary:	LessTif - source compatible library with OSF/Motif® 1.2
Summary(pl):	LessTif - biblioteka kompatybilna na poziomie ¼róde³ z OSF/Motif 1.2
Name:		lesstif
Version:	0.89.4
Release:	4
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.lesstif.org/pub/hungry/lesstif/srcdist/%{name}-%{version}.tar.gz
#Source0:	ftp://ftp.lesstif.org/pub/hungry/lesstif/srcdist/%{name}-current.tar.gz
Source1:	Mwm.desktop
Source2:	mwmrc
Source3:	mwm.RunWM
Source4:	mwm.wm_style
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-automake.patch
Icon:		lesstif-realsmall.gif
BuildRequires:	XFree86-devel
BuildRequires:	man2html
BuildRequires:	lynx
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	autoconf
BuildRequires:	automake
Obsoletes:	lesstif-M20
Obsoletes:	lesstif-M12
Provides:	motif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%define		_wmpropsdir	%{_datadir}/wm-properties

%description
Lesstif is an API compatible clone of the Motif 1.2 toolkit. Currently
Lesstif is partially implemented with most of the API in place. Saying
this a lot of the internal functionality is still missing. The primary
objectives have been to develop the widget code of the Lesstif
Toolkit.

%description -l pl
Lesstif jest bibliotek± kompatybiln± z API Motif 1.2. Aktualnie
implementacja jest czê¶ciowa, wiêkszo¶æ API istnieje, ale spora czê¶æ
funkcjonalno¶ci wewnêtrznej jest nie dokoñczona.

%package mwm
Summary:	Lesstif (Motif) window manager clone based on fvwm
Summary(pl):	Mened¿er okien bazuj±cy na fvwm, ale korzystaj±cy z Lesstifa (Motifa)
License:	GPL
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(pl):	X11/Zarz±dcy Okien
Requires:	%{name} = %{version}
Requires:	wmconfig >= 0.9.9-5
Requires:	xinitrc >= 3.0

%description mwm
A BETA release of mwm. It is derived from fvwm, with a new parser that
understands mwmrc syntax, and a general understanding of Mwm
resources.

%description mwm -l pl
Wersja BETA mwm. Wywodzi siê z fvwm, a z nowym parserem rozumiej±cym
sk³adniê mwmrc i zasoby Mwm.

%package clients
Summary:	Lesstif clients
Summary(pl):	Programy klienckie do Lesstifa
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name} = %{version}

%description clients
Uil and xmbind.

%description clients -l pl
Uil i xmbind.

%package devel
Summary:	Header files for Lesstif/Motif 1.2 development
Summary(pl):	Pliki nag³ówkowe do API Lesstif/Motif 1.2
License:	LGPL
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}
Provides:	motif-devel

%description devel
This package contains the lesstif header files required to develop
Motif 1.2 based applications.

%description devel -l pl
Pakiet zawiera pliki nag³ówkowe potrzebne do kompilacji aplikacji
opartych o Motif 1.2.

%package static
Summary:	Static Lesstif library
Summary(pl):	Biblioteki statyczne Lesstifa
License:	LGPL
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}
Provides:	motif-static

%description static
This package contains the lesstif static libraries.

%description static -l pl
Biblioteki statyczne Lesstifa.

%package -n Xbae
Summary:	The XbaeMatrix is a Motif-based widget which displays a grid of cells
Summary(pl):	XbaeMatrix jest motifowym widgetem wy¶wietlaj±cym tabelki
Copyright:	Bell Communications Research (distributable)
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description -n Xbae
The XbaeMatrix is a Motif-based widget which displays a grid of cells
in the same manner as a spreadsheet. The cell array is scrollable,
editable, and otherwise reasonably configurable in appearance. Each
cell usually displays text, but pixmaps can also be displayed (not
editable). The XbaeMatrix looks to some extent like a grid of
XmTextField widgets, but is actually implemented with a single
XmTextField. This means a big performance improvement due to less
overhead.

%description -n Xbae -l pl
XbaeMatrix jest motifowym widgetem wy¶wietlaj±cym tabelki z³o¿one z
pól w sposób podobny do arkuszy kalkulacyjnych. Tabelê mo¿na przewijaæ
i poddawaæ edycji. Ka¿de pole zazwyczaj wy¶wietla tekst, ale mo¿e
tak¿e bitmapê (bez mo¿liwo¶ci edycji).

%package -n Xbae-devel
Summary:	XbaeMatrix header files and development documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja do XbaeMatrix
Copyright:	Bell Communications Research (distributable)
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	Xbae = %{version}

%description -n Xbae-devel
XbaeMatrix header files and development documentation.

%description -n Xbae-devel -l pl
Pliki nag³ówkowe i dokumentacja programisty do XbaeMatrix.

%package -n Xbae-static
Summary:	XbaeMatrix static library
Summary(pl):	Biblioteka statyczna XbaeMatrix
Copyright:	Bell Communications Research (distributable)
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	Xbae-devel = %{version}

%description -n Xbae-static
XbaeMatrix static library.

%description -n Xbae-static -l pl
Biblioteka statyczna XbaeMatrix.

%package -n Xlt
Summary:	The LessTif extension library
Summary(pl):	Biblioteka rozszerzeñ do LessTifa
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description -n Xlt
The LessTif extension library. This consists of several widgets and
convience functions to make LessTif, or if you must Motif, programming
more enjoyable.

%description -n Xlt -l pl
Biblioteka rozszerzeñ do LessTifa. Zawiera trochê widgetów i funkcji
¿eby nieco uprzyjemniæ programowanie z u¿yciem LessTifa czy Motifa.

%package -n Xlt-devel
Summary:	Xlt header files and development documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja Xlt
License:	LGPL
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	Xlt = %{version}

%description -n Xlt-devel
Xlt header files and development documentation.

%description -n Xlt-devel -l pl
Pliki nag³ówkowe i dokumentacja programisty do Xlt.

%package -n Xlt-static
Summary:	Xlt static library
Summary(pl):	Biblioteka statyczna Xlt
License:	LGPL
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	Xlt-devel = %{version}

%description -n Xlt-static
Xlt static library.

%description -n Xlt-static -l pl
Biblioteka statyczna Xlt.

%prep
%setup -q
#%setup -q -n %{name}-current
#%patch0 -p1
%patch1 -p1

#find . -name CVS -exec rm -rf {} \; 2> /dev/null ||

%build
aclocal
autoconf
automake -a -c
%configure \
	--enable-shared \
	--enable-static \
	--enable-production \
	--disable-debug \
	--disable-scrollbar-verbose \
	--with-editres \
	--with-xdnd \
	--enable-build-12 \
	--enable-default-12 \
	--enable-build-Xbae \
	--enable-build-Xlt \
	--disable-build-20 \
	--disable-default-20

%{__make} mwmddir=/etc/X11/mwm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{sysconfig/wmstyle,X11},%{_aclocaldir},%{_wmpropsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mwmddir=/etc/X11/mwm \
	htmldir=/htmldoc

mv -f $RPM_BUILD_ROOT/htmldoc .
mv -f htmldoc/NOTES htmldoc/NOTES.html

(cd lib/Xbae/src; make install DESTDIR=$RPM_BUILD_ROOT)

rm -rf $RPM_BUILD_ROOT%{_libdir}/lib{Mrm,Xm}*
rm -rf $RPM_BUILD_ROOT%{_includedir}/{Mrm,Xm}
mv -f $RPM_BUILD_ROOT%{_prefix}/LessTif/Motif1.2/include/{Mrm,Xm} \
	$RPM_BUILD_ROOT%{_includedir}
mv -f $RPM_BUILD_ROOT%{_prefix}/LessTif/Motif1.2/lib/* \
	$RPM_BUILD_ROOT%{_libdir}

rm -f doc/INSTALL.html

# workaround - configure decides not to install *.m4 if aclocaldir is not writable
install scripts/autoconf/ac_find_motif.m4 $RPM_BUILD_ROOT%{_aclocaldir}
install lib/Xlt/ac_find_*.m4 $RPM_BUILD_ROOT%{_aclocaldir}
install lib/Xbae/ac_find_xbae.m4 $RPM_BUILD_ROOT%{_aclocaldir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/X11/mwm/system.mwmrc
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/mwm.sh
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/mwm.names

gzip -9nf clients/Motif-1.2/mwm/README \
	AUTHORS BUG-REPORTING CREDITS CURRENT_NOTES ChangeLog \
	KNOWN_BUGS NEWS README RELEASE-POLICY TODO \
	doc/*.txt \
	lib/Xbae/{AUTHORS,COPYING,FAQ,NEWS,README} \
	lib/Xlt/{AUTHORS,NEWS,README}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   -n Xbae -p /sbin/ldconfig
%postun -n Xbae -p /sbin/ldconfig

%post   -n Xlt -p /sbin/ldconfig
%postun -n Xlt -p /sbin/ldconfig

%post mwm
if [ -L /etc/X11/mwm ]; then
	rm -rf /etc/X11/mwm
	rm -rf /usr/X11R6/lib/X11/mwm/*
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/libMrm.so.*.*
%attr(755,root,root)%{_libdir}/libXm.so.*.*
%{_mandir}/man1/lesstif.1*

%files mwm
%defattr(644,root,root,755)
%doc clients/Motif-1.2/mwm/README*
%dir /etc/X11/mwm
%{_wmpropsdir}/Mwm.desktop
%config /etc/X11/mwm/*
%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
/etc/sysconfig/wmstyle/*.names
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
%doc {README,RELEASE-POLICY,TODO}.gz
%doc doc/*.txt* doc/*.html doc/www.lesstif.org/{images/*gif,*html} htmldoc/*

%attr(755,root,root) %{_libdir}/libMrm.so
%attr(755,root,root) %{_libdir}/libXm.so
%attr(755,root,root) %{_libdir}/libMrm.la
%attr(755,root,root) %{_libdir}/libXm.la

%{_includedir}/Mrm
%{_includedir}/Xm
%{_aclocaldir}/ac_find_motif.m4

%{_mandir}/man3/Composite.3*
%{_mandir}/man3/Constraint.3*
%{_mandir}/man3/Core.3*
%{_mandir}/man3/LessTifInternals.3*
%{_mandir}/man3/Object.3*
%{_mandir}/man3/OverrideShell.3*
%{_mandir}/man3/Rect.3*
%{_mandir}/man3/Shell.3*
%{_mandir}/man3/TopLevelShell.3*
%{_mandir}/man3/TransientShell.3*
%{_mandir}/man3/UnNamedObj.3*
%{_mandir}/man3/VendorShell.3*
%{_mandir}/man3/WmShell.3*
%{_mandir}/man3/Xm*

%files static
%defattr(644,root,root,755)
%{_libdir}/libMrm.a
%{_libdir}/libXm.a

%files -n Xbae
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXbae.so.*.*

%files -n Xbae-devel
%defattr(644,root,root,755)
%doc lib/Xbae/{AUTHORS,COPYING,FAQ,NEWS,README}.gz
%attr(755,root,root) %{_libdir}/libXbae.so
%attr(755,root,root) %{_libdir}/libXbae.la
%{_includedir}/Xbae
%{_aclocaldir}/ac_find_xbae.m4
%{_mandir}/man3/Xbae*

%files -n Xbae-static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/libXbae.a

%files -n Xlt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXlt.so.*.*

%files -n Xlt-devel
%defattr(644,root,root,755)
%doc lib/Xlt/{AUTHORS,NEWS,README}.gz
%attr(755,root,root) %{_libdir}/libXlt.so
%attr(755,root,root) %{_libdir}/libXlt.la
%{_includedir}/Xlt
%{_aclocaldir}/ac_find_xlt.m4
%{_aclocaldir}/ac_find_xpm.m4
%{_mandir}/man3/Xlt*

%files -n Xlt-static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/libXlt.a
