%define		motif_ver		1.2

Summary:	LessTif - source compatible library with OSF/Motif %{motif_ver}
Summary(pl):	LessTif - biblioteka kompatybilna na poziomie ºrÛde≥ z OSF/Motif %{motif_ver}
Name:		lesstif
Version:	0.93.9
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.lesstif.org/pub/hungry/lesstif/srcdist/%{name}-%{version}.tar.bz2
Source1:	Mwm.desktop
Source2:	mwmrc
Source3:	mwm.RunWM
Source4:	mwm.wm_style
Patch0:		%{name}-am.patch
Icon:		%{name}-realsmall.gif
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
Lesstif is an API compatible clone of the Motif %{motif_ver} toolkit. Currently
Lesstif is partially implemented with most of the API in place. Saying
this a lot of the internal functionality is still missing. The primary
objectives have been to develop the widget code of the Lesstif
Toolkit.

%description -l pl
Lesstif jest bibliotek± kompatybiln± z API Motif %{motif_ver}. Aktualnie
implementacja jest czÍ∂ciowa, wiÍkszo∂Ê API istnieje, ale spora czÍ∂Ê
funkcjonalno∂ci wewnÍtrznej jest nie dokoÒczona.

%package mwm
Summary:	Lesstif (Motif) window manager clone based on fvwm
Summary(pl):	Menedøer okien bazuj±cy na fvwm, ale korzystaj±cy z Lesstifa (Motifa)
License:	GPL
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(pl):	X11/Zarz±dcy Okien
Requires:	%{name} = %{version}
Requires:	wmconfig >= 0.9.9-5
Requires:	xinitrc >= 3.0
Obsoletes:	openmotif-mwm

%description mwm
A BETA release of mwm. It is derived from fvwm, with a new parser that
understands mwmrc syntax, and a general understanding of Mwm
resources.

%description mwm -l pl
Wersja BETA mwm. Wywodzi siÍ z fvwm, a z nowym parserem rozumiej±cym
sk≥adniÍ mwmrc i zasoby Mwm.

%package clients
Summary:	Lesstif clients
Summary(pl):	Programy klienckie do Lesstifa
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name} = %{version}
Obsoletes:	openmotif-clients

%description clients
Uil and xmbind.

%description clients -l pl
Uil i xmbind.

%package devel
Summary:	Header files for Lesstif/Motif %{motif_ver} development
Summary(pl):	Pliki nag≥Ûwkowe do API Lesstif/Motif %{motif_ver}
License:	LGPL
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Provides:	motif-devel = %{motif_ver}
Obsoletes:	openmotif-devel

%description devel
This package contains the lesstif header files required to develop
Motif %{motif_ver} based applications.

%description devel -l pl
Pakiet zawiera pliki nag≥Ûwkowe potrzebne do kompilacji aplikacji
opartych o Motif %{motif_ver}.

%package static
Summary:	Static Lesstif library
Summary(pl):	Biblioteki statyczne Lesstifa
License:	LGPL
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}
Provides:	motif-static
Obsoletes:	openmotif-static

%description static
This package contains the lesstif static libraries.

%description static -l pl
Biblioteki statyczne Lesstifa.

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

%{__make} mwmddir=/etc/X11/mwm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{sysconfig/wmstyle,X11},%{_aclocaldir},%{_wmpropsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mwmddir=/etc/X11/mwm \
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
%doc clients/Motif-%{motif_ver}/mwm/README*
%dir /etc/X11/mwm
%{_wmpropsdir}/Mwm.desktop
%config /etc/X11/mwm/*
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
