%define		motif_ver		1.2

Summary:	LessTif - source compatible library with OSF/Motif %{motif_ver}
Summary(es):	Clon de la caja de herramientas Motif
Summary(pl):	LessTif - biblioteka kompatybilna na poziomie ¼róde³ z OSF/Motif %{motif_ver}
Summary(pt_BR):	Um clone do Motif toolkit
Name:		lesstif
Version:	0.93.18
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.lesstif.org/pub/hungry/lesstif/srcdist/%{name}-%{version}.tar.bz2
Source1:	Mwm.desktop
Source2:	mwmrc
Source3:	mwm.RunWM
Source4:	mwm.wm_style
Patch0:		%{name}-am.patch
Icon:		lesstif-realsmall.gif
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lynx
BuildRequires:	flex
BuildRequires:	bison
Obsoletes:	lesstif-M20
Obsoletes:	lesstif-M12
%if %(echo %{motif_ver} | sed s/\\.//) >= 20
# openmotif provides library version 2.1, so there witl be conflicts
Obsoletes:	openmotif
%endif
Provides:	motif = %{motif_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%define		_wmpropsdir	%{_datadir}/wm-properties

%description
Lesstif is an API compatible clone of the Motif %{motif_ver} toolkit.
Currently Lesstif is partially implemented with most of the API in
place. Saying this a lot of the internal functionality is still
missing. The primary objectives have been to develop the widget code
of the Lesstif Toolkit.

%description -l es
Clon de la caja de herramientas Motif

%description -l pl
Lesstif jest bibliotek± kompatybiln± z API Motif %{motif_ver}.
Aktualnie implementacja jest czê¶ciowa, wiêkszo¶æ API istnieje, ale
spora czê¶æ funkcjonalno¶ci wewnêtrznej jest nie dokoñczona.

%description -l pt_BR
O Lesstif é um clone do Motif, com a API compatível.

%package mwm
Summary:	Lesstif (Motif) window manager clone based on fvwm
Summary(pl):	Mened¿er okien bazuj±cy na fvwm, ale korzystaj±cy z Lesstifa (Motifa)
License:	GPL
Group:		X11/Window Managers
Requires:	%{name} = %{version}
Requires:	wmconfig >= 0.9.9-5
Requires:	xinitrc >= 3.0
Obsoletes:	openmotif-mwm

%description mwm
A BETA release of mwm. It is derived from fvwm, with a new parser that
understands mwmrc syntax, and a general understanding of Mwm
resources.

%description -l es mwm
MWM es un administrador de ventanas que adhiere ampliamente a la
especificación Motif.

%description mwm -l pl
Wersja BETA mwm. Wywodzi siê z fvwm, a z nowym parserem rozumiej±cym
sk³adniê mwmrc i zasoby Mwm.

%description -l pt_BR mwm
O MWM é um gerenciador de janelas que adere largamente à especificação
Motif.

%package clients
Summary:	Lesstif clients
Summary(pl):	Programy klienckie do Lesstifa
License:	GPL
Group:		X11/Applications
Requires:	%{name} = %{version}
Obsoletes:	openmotif-clients

%description clients
Uil and xmbind.

%description -l es clients
Clientes de lesstif.

%description clients -l pl
Uil i xmbind.

%description -l pt_BR clients
lesstiff: Uil e xmbind.

%package devel
Summary:	Header files for Lesstif/Motif %{motif_ver} development
Summary(es):	Bibliotecas y archivos de inclusión para desarrollo del lesstif
Summary(pl):	Pliki nag³ówkowe do API Lesstif/Motif %{motif_ver}
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimentos com o lesstif
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Provides:	motif-devel = %{motif_ver}
Obsoletes:	openmotif-devel

%description devel
This package contains the lesstif header files required to develop
Motif %{motif_ver} based applications.

%description -l es devel
Bibliotecas y archivos de inclusión que se requieren para desarrollar
aplicaciones basadas en lesstif/motif-%{motif_ver}.

%description devel -l pl
Pakiet zawiera pliki nag³ówkowe potrzebne do kompilacji aplikacji
opartych o Motif %{motif_ver}.

%description -l pt_BR devel
Bibliotecas e arquivos de inclusão requeridas para desenvolver
aplicações baseadas no lesstif/motif-%{motif_ver}.

%package static
Summary:	Static Lesstif library
Summary(es):	Bibliotecas para lesstif en versión estática
Summary(pl):	Biblioteki statyczne Lesstifa
Summary(pt_BR):	Bibliotecas para o lesstif em versão estática
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}
Provides:	motif-static
Obsoletes:	openmotif-static

%description static
This package contains the lesstif static libraries.

%description -l es static
Bibliotecas para lesstif en versión estática.

%description static -l pl
Biblioteki statyczne Lesstifa.

%description -l pt_BR static
Bibliotecas para o lesstif em versão estática.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
automake -a -c
(cd test
aclocal
autoconf
automake -a -c)

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

%{__make} mwmddir=%{_sysconfdir}/X11/mwm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/{sysconfig/wmstyle,X11},%{_aclocaldir},%{_wmpropsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
mwmddir=%{_sysconfdir}/X11/mwm \
	htmldir=/htmldoc

mv -f $RPM_BUILD_ROOT/htmldoc .

rm -f doc/www.lesstif.org/INSTALL.html

# workaround - configure decides not to install *.m4 if aclocaldir is not writable
install scripts/autoconf/ac_find_motif.m4 $RPM_BUILD_ROOT%{_aclocaldir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/X11/mwm/system.mwmrc
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/mwm.sh
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/mwm.names

gzip -9nf clients/Motif-%{motif_ver}/mwm/README \
	AUTHORS BUG-REPORTING CREDITS \
	ChangeLog NEWS README ReleaseNotes.txt \
	doc/*.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post mwm
if [ -L %{_sysconfdir}/X11/mwm ]; then
	rm -rf %{_sysconfdir}/X11/mwm
	rm -rf %{_libdir}/X11/mwm/*
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
%doc clients/Motif-%{motif_ver}/mwm/README*
%dir %{_sysconfdir}/X11/mwm
%{_wmpropsdir}/Mwm.desktop
%config %{_sysconfdir}/X11/mwm/*
%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
/etc/sysconfig/wmstyle/*.names
%attr(755,root,root) %{_bindir}/mwm

%{_libdir}/X11/app-defaults/*

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
%doc {AUTHORS,BUG-REPORTING,CREDITS,ChangeLog,NEWS,README,ReleaseNotes.txt}.gz
%doc doc/*.txt* doc/*.html doc/www.lesstif.org/{images/*png,*html} htmldoc/*

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
