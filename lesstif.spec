%define		motif_ver		1.2

Summary:	LessTif - source compatible library with OSF/Motif %{motif_ver}
Summary(es):	Clon de la caja de herramientas Motif
Summary(ja):	lesstif - Motif互換ツールキット
Summary(pl):	LessTif - biblioteka kompatybilna na poziomie �r�de� z OSF/Motif %{motif_ver}
Summary(pt_BR):	Um clone do Motif toolkit
Name:		lesstif
Version:	0.93.91
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/lesstif/%{name}-%{version}.tar.bz2
# Source0-md5:	7f1a07b8e7b79e3c7dd32ddb4c4e699e
Source1:	Mwm.desktop
Source2:	mwmrc
Source3:	mwm.RunWM
Source4:	mwm.wm_style
Source5:	mwm-xsession.desktop
Patch0:		%{name}-amfix.patch
Patch1:		%{name}-ac.patch
Icon:		lesstif-realsmall.gif
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	lynx
Provides:	motif = %{motif_ver}
Obsoletes:	lesstif-M12
Obsoletes:	lesstif-M20
%if %(echo %{motif_ver} | sed s/\\.//) >= 20
# openmotif provides library version 2.1, so there will be conflicts
Obsoletes:	openmotif
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
Lesstifは、MotifツールキットとAPIレベルの互換性をもつツールキットです。
現在のLesstifは、ほとんどのAPIを実装していますが、一部の内部関数は
まだ実装されていません。多くのMotifアプリケーションはLesstifを使って
コンパイル及び実行することができます。

%description -l pl
Lesstif jest bibliotek� kompatybiln� z API Motif %{motif_ver}.
Aktualnie implementacja jest cz蟠ciowa, wi�kszo倶 API istnieje, ale
spora cz蟠� funkcjonalno�ci wewn�trznej jest nie doko�czona.

%description -l pt_BR
O Lesstif � um clone do Motif, com a API compat�vel.

%package mwm
Summary:	Lesstif (Motif) window manager clone based on fvwm
Summary(ja):	fvwmをベースにしたMotifウインドウマネージャ
Summary(pl):	Zarz�dca okien oparty na fvwm, ale korzystaj�cy z Lesstifa (Motifa)
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

%description mwm -l es
MWM es un administrador de ventanas que adhiere ampliamente a la
especificaci�n Motif.

%description -l ja
MWMは、Motifのmwmスペックに準拠したウインドウマネージャです。

%description mwm -l pl
Wersja BETA mwm. Wywodzi si� z fvwm, a z nowym parserem rozumiej�cym
sk�adni� mwmrc i zasoby Mwm.

%description mwm -l pt_BR
O MWM � um gerenciador de janelas que adere largamente � especifica艫o
Motif.

%package clients
Summary:	Lesstif clients
Summary(ja):	lesstifクライアント
Summary(pl):	Programy klienckie do Lesstifa
License:	GPL
Group:		X11/Applications
Requires:	%{name} = %{version}
Obsoletes:	openmotif-clients

%description clients
Uil and xmbind.

%description clients -l es
Clientes de lesstif.

%description -l ja
Uilとxmbind

%description clients -l pl
Uil i xmbind.

%description clients -l pt_BR
lesstiff: Uil e xmbind.

%package devel
Summary:	Header files for Lesstif/Motif %{motif_ver} development
Summary(es):	Bibliotecas y archivos de inclusi�n para desarrollo del lesstif
Summary(pl):	Pliki nag鞄wkowe do API Lesstif/Motif %{motif_ver}
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para desenvolvimentos com o lesstif
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Provides:	motif-devel = %{motif_ver}
Obsoletes:	openmotif-devel
Conflicts:	tcl-devel < 8.3.4-8

%description devel
This package contains the lesstif header files required to develop
Motif %{motif_ver} based applications.

%description devel -l es
Bibliotecas y archivos de inclusi�n que se requieren para desarrollar
aplicaciones basadas en lesstif/motif-%{motif_ver}.

%description devel -l pl
Pakiet zawiera pliki nag鞄wkowe potrzebne do kompilacji aplikacji
opartych o Motif %{motif_ver}.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o requeridas para desenvolver
aplica苺es baseadas no lesstif/motif-%{motif_ver}.

%package static
Summary:	Static Lesstif library
Summary(es):	Bibliotecas para lesstif en versi�n est�tica
Summary(pl):	Biblioteki statyczne Lesstifa
Summary(pt_BR):	Bibliotecas para o lesstif em vers�o est�tica
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}
Provides:	motif-static
Obsoletes:	openmotif-static

%description static
This package contains the lesstif static libraries.

%description static -l es
Bibliotecas para lesstif en versi�n est�tica.

%description static -l pl
Biblioteki statyczne Lesstifa.

%description static -l pt_BR
Bibliotecas para o lesstif em vers�o est�tica.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd test
rm -f missing
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

# for proper app-defaults path
install -d $RPM_BUILD_ROOT{%{_appdefsdir},%{_libdir}}
ln -sf ../X11R6/lib/X11 $RPM_BUILD_ROOT%{_libdir}/X11

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
%attr(755,root,root) %{_libdir}/libXm.so.*.*
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

%attr(755,root,root) %{_libdir}/libMrm.so
%attr(755,root,root) %{_libdir}/libXm.so
%{_libdir}/libMrm.la
%{_libdir}/libXm.la

%{_includedir}/Mrm
%{_includedir}/Xm
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
%{_libdir}/libXm.a
