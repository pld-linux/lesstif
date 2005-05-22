%define		motif_ver	2.1
%define		mver		%(echo %{motif_ver} | tr -d .)
Summary:	LessTif - source compatible library with OSF/Motif %{motif_ver}
Summary(es):	Clon de la caja de herramientas Motif
Summary(ja):	lesstif - Motif¸ß´¹¥Ä¡¼¥ë¥­¥Ã¥È
Summary(pl):	LessTif - biblioteka kompatybilna na poziomie ¼róde³ z OSF/Motif %{motif_ver}
Summary(pt_BR):	Um clone do Motif toolkit
Name:		lesstif
Version:	0.94.4
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/lesstif/%{name}-%{version}.tar.bz2
# Source0-md5:	3096ca456c0bc299d895974d307c82d8
Source1:	Mwm.desktop
Source2:	mwmrc
Source3:	mwm.RunWM
Source5:	mwm-xsession.desktop
Patch0:		%{name}-link.patch
Patch1:		%{name}-freetype-includes.patch
Patch2:		%{name}-libdir.patch
Icon:		lesstif-realsmall.gif
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	lynx
%if %{mver} >= 20
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	xft-devel
%endif
Provides:	motif = %{motif_ver}
Obsoletes:	lesstif-M12
Obsoletes:	lesstif-M20
%if %{mver} >= 20
# openmotif used to provide library version 2.1, so there would be conflicts
Obsoletes:	openmotif < 2.2
Obsoletes:	openmotif-libs < 2.2
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties
%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
Lesstif is an API compatible clone of the Motif %{motif_ver} toolkit.
Currently Lesstif is partially implemented with most of the API in
place. Saying this a lot of the internal functionality is still
missing. The primary objectives have been to develop the widget code
of the Lesstif Toolkit.

%description -l es
Clon de la caja de herramientas Motif.

%description -l ja
Lesstif¤Ï¡¢Motif¥Ä¡¼¥ë¥­¥Ã¥È¤ÈAPI¥ì¥Ù¥ë¤Î¸ß´¹À­¤ò¤â¤Ä¥Ä¡¼¥ë¥­¥Ã¥È¤Ç¤¹¡£
¸½ºß¤ÎLesstif¤Ï¡¢¤Û¤È¤ó¤É¤ÎAPI¤ò¼ÂÁõ¤·¤Æ¤¤¤Þ¤¹¤¬¡¢°ìÉô¤ÎÆâÉô´Ø¿ô¤Ï
¤Þ¤À¼ÂÁõ¤µ¤ì¤Æ¤¤¤Þ¤»¤ó¡£Â¿¤¯¤ÎMotif¥¢¥×¥ê¥±¡¼¥·¥ç¥ó¤ÏLesstif¤ò»È¤Ã¤Æ
¥³¥ó¥Ñ¥¤¥ëµÚ¤Ó¼Â¹Ô¤¹¤ë¤³¤È¤¬¤Ç¤­¤Þ¤¹¡£

%description -l pl
Lesstif jest bibliotek± kompatybiln± z API Motif %{motif_ver}.
Aktualnie implementacja jest czê¶ciowa, wiêkszo¶æ API istnieje, ale
spora czê¶æ funkcjonalno¶ci wewnêtrznej jest nie dokoñczona.

%description -l pt_BR
O Lesstif é um clone do Motif, com a API compatível.

%package mwm
Summary:	Lesstif (Motif) window manager clone based on fvwm
Summary(ja):	fvwm¤ò¥Ù¡¼¥¹¤Ë¤·¤¿Motif¥¦¥¤¥ó¥É¥¦¥Þ¥Í¡¼¥¸¥ã
Summary(pl):	Zarz±dca okien oparty na fvwm, ale korzystaj±cy z Lesstifa (Motifa)
License:	GPL
Group:		X11/Window Managers
Requires:	%{name} = %{version}-%{release}
Requires:	xinitrc-ng
Obsoletes:	openmotif-mwm

%description mwm
A BETA release of mwm. It is derived from fvwm, with a new parser that
understands mwmrc syntax, and a general understanding of Mwm
resources.

%description mwm -l es
MWM es un administrador de ventanas que adhiere ampliamente a la
especificación Motif.

%description mwm -l ja
MWM¤Ï¡¢Motif¤Îmwm¥¹¥Ú¥Ã¥¯¤Ë½àµò¤·¤¿¥¦¥¤¥ó¥É¥¦¥Þ¥Í¡¼¥¸¥ã¤Ç¤¹¡£

%description mwm -l pl
Wersja BETA mwm. Wywodzi siê z fvwm, a z nowym parserem rozumiej±cym
sk³adniê mwmrc i zasoby Mwm.

%description mwm -l pt_BR
O MWM é um gerenciador de janelas que adere largamente à especificação
Motif.

%package clients
Summary:	Lesstif clients
Summary(ja):	lesstif¥¯¥é¥¤¥¢¥ó¥È
Summary(pl):	Programy klienckie do Lesstifa
License:	GPL
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openmotif-clients

%description clients
Uil and xmbind.

%description clients -l es
Clientes de lesstif.

%description clients -l ja
Uil¤Èxmbind

%description clients -l pl
Uil i xmbind.

%description clients -l pt_BR
lesstiff: Uil e xmbind.

%package devel
Summary:	Header files for Lesstif/Motif %{motif_ver} development
Summary(es):	Bibliotecas y archivos de inclusión para desarrollo del lesstif
Summary(pl):	Pliki nag³ówkowe do API Lesstif/Motif %{motif_ver}
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimentos com o lesstif
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	XFree86-devel
Provides:	motif-devel = %{motif_ver}
Obsoletes:	openmotif-devel
Conflicts:	tcl-devel < 8.3.4-8

%description devel
This package contains the lesstif header files required to develop
Motif %{motif_ver} based applications.

%description devel -l es
Bibliotecas y archivos de inclusión que se requieren para desarrollar
aplicaciones basadas en lesstif/motif-%{motif_ver}.

%description devel -l pl
Pakiet zawiera pliki nag³ówkowe potrzebne do kompilacji aplikacji
opartych o Motif %{motif_ver}.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão requeridas para desenvolver
aplicações baseadas no lesstif/motif-%{motif_ver}.

%package static
Summary:	Static Lesstif library
Summary(es):	Bibliotecas para lesstif en versión estática
Summary(pl):	Biblioteki statyczne Lesstifa
Summary(pt_BR):	Bibliotecas para o lesstif em versão estática
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	motif-static
Obsoletes:	openmotif-static

%description static
This package contains the lesstif static libraries.

%description static -l es
Bibliotecas para lesstif en versión estática.

%description static -l pl
Biblioteki statyczne Lesstifa.

%description static -l pt_BR
Bibliotecas para o lesstif em versão estática.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

ln -sf ../acinclude.m4 test/acinclude.m4

%build
%{__libtoolize}
%{__aclocal} -I .
%{__autoconf}
%{__automake}
cd test
%{__aclocal} -I ..
%{__autoconf}
# -f must not be used here
automake -a -c --foreign
cd ..

%configure \
	--enable-shared \
	--enable-static \
	--enable-production \
	--disable-debug \
	--disable-scrollbar-verbose \
	--with-editres \
	--with-xdnd \
	--disable-build-12 \
	--disable-build-20 \
	--disable-build-21 \
	--enable-build-%(echo %{motif_ver} | sed s/\\.//)

%{__make} \
	mwmddir=%{_sysconfdir}/X11/mwm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{sysconfig/wmstyle,X11} \
	$RPM_BUILD_ROOT{%{_aclocaldir},%{_datadir}/xsessions,%{_wmpropsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mwmddir=%{_sysconfdir}/X11/mwm \
	appdir=%{_appdefsdir} \
	htmldir=/htmldoc

mv -f $RPM_BUILD_ROOT/htmldoc .

rm -f doc/www.lesstif.org/INSTALL.html

# workaround - configure decides not to install *.m4 if aclocaldir is not writable
install scripts/autoconf/ac_find_motif.m4 $RPM_BUILD_ROOT%{_aclocaldir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/X11/mwm/system.mwmrc
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/mwm.sh
install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/xsessions/mwm.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post mwm
if [ -L %{_sysconfdir}/X11/mwm ]; then
	rm -rf %{_sysconfdir}/X11/mwm
	rm -rf %{_libdir}/X11/mwm/*
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libMrm.so.*.*
%attr(755,root,root) %{_libdir}/libUil.so.*.*
%attr(755,root,root) %{_libdir}/libXm.so.*.*
%if %{mver} >= 21
%attr(755,root,root) %{_libdir}/libDtPrint.so.*.*
%endif
%{_mandir}/man1/lesstif.1*

%files mwm
%defattr(644,root,root,755)
%doc clients/Motif-%{motif_ver}/mwm/README*
%dir %{_sysconfdir}/X11/mwm
%{_wmpropsdir}/Mwm.desktop
%config %{_sysconfdir}/X11/mwm/*
%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
%attr(755,root,root) %{_bindir}/mwm

%{_datadir}/xsessions/mwm.desktop

%{_appdefsdir}/*

%{_mandir}/man1/mwm.1*
%{_mandir}/man5/mwmrc.5*

%files clients
%defattr(644,root,root,755)
%doc doc/UIL.txt*
%attr(755,root,root) %{_bindir}/uil
%attr(755,root,root) %{_bindir}/xmbind
%{_mandir}/man1/uil.1*
%{_mandir}/man1/xmbind.1*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS BUG-REPORTING CREDITS ChangeLog NEWS README ReleaseNotes.txt
%doc doc/*.txt* doc/*.html doc/www.lesstif.org/{images/*png,*html} htmldoc/*
%attr(755,root,root) %{_bindir}/motif-config
%attr(755,root,root) %{_bindir}/mxmkmf
%attr(755,root,root) %{_libdir}/libMrm.so
%attr(755,root,root) %{_libdir}/libUil.so
%attr(755,root,root) %{_libdir}/libXm.so
%{_libdir}/libMrm.la
%{_libdir}/libUil.la
%{_libdir}/libXm.la
%{_libdir}/LessTif
%{_includedir}/Mrm
%{_includedir}/Xm
%{_includedir}/uil

%if %{mver} >= 21
%attr(755,root,root) %{_libdir}/libDtPrint.so
%{_libdir}/libDtPrint.la
%{_includedir}/Dt
%endif

%{_aclocaldir}/ac_find_motif.m4

%{_mandir}/man3/ApplicationShell.3*
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
%{_libdir}/libUil.a
%{_libdir}/libXm.a
%if %{mver} >= 21
%{_libdir}/libDtPrint.a
%endif
