#
# Conditional build:
%bcond_with	gnome		# build with support for GNOME2 wm-properties
#
%define		motif_ver	2.1
%define		mver		%(echo %{motif_ver} | tr -d .)
Summary:	LessTif - source compatible library with OSF/Motif %{motif_ver}
Summary(es.UTF-8):	Clon de la caja de herramientas Motif
Summary(ja.UTF-8):	lesstif - Motif互換ツールキット
Summary(pl.UTF-8):	LessTif - biblioteka kompatybilna na poziomie źródeł z OSF/Motif %{motif_ver}
Summary(pt_BR.UTF-8):	Um clone do Motif toolkit
Name:		lesstif
Version:	0.95.2
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/lesstif/%{name}-%{version}.tar.bz2
# Source0-md5:	754187dbac09fcf5d18296437e72a32f
Source1:	Mwm.desktop
Source2:	mwmrc
Source5:	mwm-xsession.desktop
Patch0:		%{name}-link.patch
Patch1:		%{name}-ac.patch
Patch2:		%{name}-libdir.patch
Patch3:		%{name}-lt_fix.patch
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	lynx
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
%if %{mver} >= 20
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXrender-devel
%endif
Requires:	xorg-lib-libXt >= 1.0.0
Provides:	motif = %{motif_ver}
Obsoletes:	lesstif-M12
Obsoletes:	lesstif-M20
%if %{mver} >= 20
# openmotif used to provide library version 2.1, so there would be conflicts
Obsoletes:	openmotif < 2.2
Obsoletes:	openmotif-libs < 2.2
%endif
Conflicts:	filesystem < 3.0-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/gnome/wm-properties
%define		_appdefsdir	/usr/share/X11/app-defaults

%description
Lesstif is an API compatible clone of the Motif %{motif_ver} toolkit.
Currently Lesstif is partially implemented with most of the API in
place. Saying this a lot of the internal functionality is still
missing. The primary objectives have been to develop the widget code
of the Lesstif Toolkit.

%description -l es.UTF-8
Clon de la caja de herramientas Motif.

%description -l ja.UTF-8
Lesstifは、MotifツールキットとAPIレベルの互換性をもつツールキットです。
現在のLesstifは、ほとんどのAPIを実装していますが、一部の内部関数は
まだ実装されていません。多くのMotifアプリケーションはLesstifを使って
コンパイル及び実行することができます。

%description -l pl.UTF-8
Lesstif jest biblioteką kompatybilną z API Motif %{motif_ver}.
Aktualnie implementacja jest częściowa, większość API istnieje, ale
spora część funkcjonalności wewnętrznej jest nie dokończona.

%description -l pt_BR.UTF-8
O Lesstif é um clone do Motif, com a API compatível.

%package mwm
Summary:	Lesstif (Motif) window manager clone based on fvwm
Summary(ja.UTF-8):	fvwmをベースにしたMotifウインドウマネージャ
Summary(pl.UTF-8):	Zarządca okien oparty na fvwm, ale korzystający z Lesstifa (Motifa)
License:	GPL
Group:		X11/Window Managers
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openmotif-mwm

%description mwm
A BETA release of mwm. It is derived from fvwm, with a new parser that
understands mwmrc syntax, and a general understanding of Mwm
resources.

%description mwm -l es.UTF-8
MWM es un administrador de ventanas que adhiere ampliamente a la
especificación Motif.

%description mwm -l ja.UTF-8
MWMは、Motifのmwmスペックに準拠したウインドウマネージャです。

%description mwm -l pl.UTF-8
Wersja BETA mwm. Wywodzi się z fvwm, a z nowym parserem rozumiejącym
składnię mwmrc i zasoby Mwm.

%description mwm -l pt_BR.UTF-8
O MWM é um gerenciador de janelas que adere largamente à especificação
Motif.

%package clients
Summary:	Lesstif clients
Summary(ja.UTF-8):	lesstifクライアント
Summary(pl.UTF-8):	Programy klienckie do Lesstifa
License:	GPL
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	openmotif-clients

%description clients
Uil and xmbind.

%description clients -l es.UTF-8
Clientes de lesstif.

%description clients -l ja.UTF-8
Uilとxmbind

%description clients -l pl.UTF-8
Uil i xmbind.

%description clients -l pt_BR.UTF-8
lesstiff: Uil e xmbind.

%package devel
Summary:	Header files for Lesstif/Motif %{motif_ver} development
Summary(es.UTF-8):	Bibliotecas y archivos de inclusión para desarrollo del lesstif
Summary(pl.UTF-8):	Pliki nagłówkowe do API Lesstif/Motif %{motif_ver}
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolvimentos com o lesstif
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXt-devel >= 1.0.0
Requires:	xorg-proto-xproto-devel
Requires:	xorg-proto-printproto-devel
Provides:	motif-devel = %{motif_ver}
Obsoletes:	openmotif-devel
Conflicts:	tcl-devel < 8.3.4-8

%description devel
This package contains the lesstif header files required to develop
Motif %{motif_ver} based applications.

%description devel -l es.UTF-8
Bibliotecas y archivos de inclusión que se requieren para desarrollar
aplicaciones basadas en lesstif/motif-%{motif_ver}.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe potrzebne do kompilacji aplikacji
opartych o Motif %{motif_ver}.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão requeridas para desenvolver
aplicações baseadas no lesstif/motif-%{motif_ver}.

%package static
Summary:	Static Lesstif library
Summary(es.UTF-8):	Bibliotecas para lesstif en versión estática
Summary(pl.UTF-8):	Biblioteki statyczne Lesstifa
Summary(pt_BR.UTF-8):	Bibliotecas para o lesstif em versão estática
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	motif-static
Obsoletes:	openmotif-static

%description static
This package contains the lesstif static libraries.

%description static -l es.UTF-8
Bibliotecas para lesstif en versión estática.

%description static -l pl.UTF-8
Biblioteki statyczne Lesstifa.

%description static -l pt_BR.UTF-8
Bibliotecas para o lesstif em versão estática.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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

# --x-includes is needed to detect Xft headers
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
	--enable-build-%(echo %{motif_ver} | sed s/\\.//) \
	--x-includes=/usr/include

%{__make} \
	mwmddir=%{_sysconfdir}/X11/mwm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/mwm \
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

%{?with_gnome:install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}}
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/X11/mwm/system.mwmrc
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
%{?with_gnome:%{_wmpropsdir}/Mwm.desktop}
%config %{_sysconfdir}/X11/mwm/*
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
