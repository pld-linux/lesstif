Summary:	LessTif - source compatible library with OSF/Motif® 1.2
Name:		lesstif
Version:	0.89.0
Release:	2
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.lesstif.org/pub/hungry/lesstif/srcdist/%{name}-%{version}.tar.gz
#Source0:	ftp://ftp.lesstif.org/pub/hungry/lesstif/srcdist/%{name}-current.tar.gz
Patch0:		lesstif-DESTDIR.patch
Patch1:		lesstif-automake.patch
Icon:		lesstif-realsmall.gif
BuildRequires:	XFree86-devel
BuildRequires:	man2html
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	lesstif-M20
Obsoletes:	lesstif-M12

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
Summary(pl):	Biblioteki statyczne Lesstifa
Copyright:	LGPL
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
This package contains the lesstif static libraries.

%description -l pl static
Biblioteki statyczne Lesstifa.

%package -n Xbae
Summary:	The XbaeMatrix is a Motif-based widget which displays a grid of cells
Copyright:	Bell Communications Research (distributable)
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description -n Xbae
The XbaeMatrix is a Motif-based widget which displays a grid of cells in the
same manner as a spreadsheet. The cell array is scrollable, editable, and
otherwise reasonably configurable in appearance. Each cell usually displays
text, but pixmaps can also be displayed (not editable). The XbaeMatrix looks
to some extent like a grid of XmTextField widgets, but is actually
implemented with a single XmTextField. This means a big performance
improvement due to less overhead.

%package -n Xbae-devel
Summary:	XbaeMatrix header files and development documentation
Copyright:	Bell Communications Research (distributable)
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	Xbae = %{version}

%description -n Xbae-devel
XbaeMatrix header files and development documentation.

%package -n Xbae-static
Summary:	XbaeMatrix static library
Copyright:	Bell Communications Research (distributable)
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	Xbae-devel = %{version}

%description -n Xbae-static
XbaeMatrix static library.

%prep
%setup -q
#%setup -q -n %{name}-current
%patch0 -p1
%patch1 -p1

#find . -name CVS -exec rm -rf {} \; 2> /dev/null ||

%build
autoconf
automake
LDFLAGS="-s"; export LDFLAGS
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
	--disable-build-20 \
	--disable-default-20

make mwmddir=/etc/X11/mwm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11,usr/share/aclocal}

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	mwmddir=/etc/X11/mwm \
	htmldir=/home/httpd/html/Lesstif-%{version}

(cd lib/Xbae/src; make install DESTDIR=$RPM_BUILD_ROOT)

rm -rf $RPM_BUILD_ROOT%{_libdir}/lib{Mrm,Xm}*
rm -rf $RPM_BUILD_ROOT%{_includedir}/{Mrm,Xm}
mv $RPM_BUILD_ROOT%{_prefix}/LessTif/Motif1.2/include/{Mrm,Xm} \
	$RPM_BUILD_ROOT%{_includedir}
mv $RPM_BUILD_ROOT%{_prefix}/LessTif/Motif1.2/lib/* \
	$RPM_BUILD_ROOT%{_libdir}

rm -f doc/INSTALL.html

install lib/Xbae/ac_find_xbae.m4 $RPM_BUILD_ROOT/usr/share/aclocal

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	clients/Motif-1.2/mwm/README \
	AUTHORS BUG-REPORTING CREDITS CURRENT_NOTES ChangeLog \
	KNOWN_BUGS NEWS NOTES README RELEASE-POLICY TODO \
	doc/*.txt \
	lib/Xbae/{AUTHORS,COPYING,FAQ,NEWS,README}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   -n Xbae -p /sbin/ldconfig
%postun -n Xbae -p /sbin/ldconfig

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

%attr(755,root,root) %{_libdir}/libMrm.so
%attr(755,root,root) %{_libdir}/libXm.so
%attr(755,root,root) %{_libdir}/libMrm.la
%attr(755,root,root) %{_libdir}/libXm.la

%{_includedir}/Mrm
%{_includedir}/Xm

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
%{_mandir}/man3/XmArrowButton.3*
%{_mandir}/man3/XmArrowButtonGadget.3*
%{_mandir}/man3/XmBulletinBoard.3*
%{_mandir}/man3/XmCascadeButton.3*
%{_mandir}/man3/XmCascadeButtonGadget.3*
%{_mandir}/man3/XmClipboard.3*
%{_mandir}/man3/XmComboBox.3*
%{_mandir}/man3/XmCommand.3*
%{_mandir}/man3/XmDesktop.3*
%{_mandir}/man3/XmDialogShell.3*
%{_mandir}/man3/XmDialogShellExt.3*
%{_mandir}/man3/XmDisplay.3*
%{_mandir}/man3/XmDragContext.3*
%{_mandir}/man3/XmDragIcon.3*
%{_mandir}/man3/XmDragOverShell.3*
%{_mandir}/man3/XmDrawingArea.3*
%{_mandir}/man3/XmDrawnButton.3*
%{_mandir}/man3/XmDropSiteManager.3*
%{_mandir}/man3/XmDropTransfer.3*
%{_mandir}/man3/XmFileSelectionBox.3*
%{_mandir}/man3/XmForm.3*
%{_mandir}/man3/XmFrame.3*
%{_mandir}/man3/XmGadget.3*
%{_mandir}/man3/XmGrabShell.3*
%{_mandir}/man3/XmIconGadget.3*
%{_mandir}/man3/XmLabel.3*
%{_mandir}/man3/XmLabelGadget.3*
%{_mandir}/man3/XmList.3*
%{_mandir}/man3/XmMainWindow.3*
%{_mandir}/man3/XmManager.3*
%{_mandir}/man3/XmMenuShell.3*
%{_mandir}/man3/XmMessageBox.3*
%{_mandir}/man3/XmNotebook.3*
%{_mandir}/man3/XmPanedWindow.3*
%{_mandir}/man3/XmPrimitive.3*
%{_mandir}/man3/XmProtocol.3*
%{_mandir}/man3/XmPushButton.3*
%{_mandir}/man3/XmPushButtonGadget.3*
%{_mandir}/man3/XmRowColumn.3*
%{_mandir}/man3/XmSash.3*
%{_mandir}/man3/XmScale.3*
%{_mandir}/man3/XmScreen.3*
%{_mandir}/man3/XmScrollBar.3*
%{_mandir}/man3/XmScrolledWindow.3*
%{_mandir}/man3/XmSelectionBox.3*
%{_mandir}/man3/XmSeparator.3*
%{_mandir}/man3/XmSeparatorGadget.3*
%{_mandir}/man3/XmSpinBox.3*
%{_mandir}/man3/XmTearOffButton.3*
%{_mandir}/man3/XmText.3*
%{_mandir}/man3/XmTextField.3*
%{_mandir}/man3/XmToggleButton.3*
%{_mandir}/man3/XmToggleButtonGadget.3*
%{_mandir}/man3/XmVendorShell.3*
%{_mandir}/man3/XmWorld.3*
%{_mandir}/man3/XtConfigureObject.3*
%{_mandir}/man3/XtDestroyWidget.3*
%{_mandir}/man3/XtManageChild.3*
%{_mandir}/man3/XtUnmanageChild.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libMrm.a
%{_libdir}/libXm.a

%files -n Xbae
%attr(755,root,root) %{_libdir}/libXbae.so.*.*

%files -n Xbae-devel
%defattr(644,root,root,755)
%doc lib/Xbae/{AUTHORS,COPYING,FAQ,NEWS,README}.gz
%attr(755,root,root) %{_libdir}/libXbae.so
%attr(755,root,root) %{_libdir}/libXbae.la
%{_includedir}/Xbae
/usr/share/aclocal/ac_find_xbae.m4

%{_mandir}/man3/XbaeCaption.3*
%{_mandir}/man3/XbaeInput.3*
%{_mandir}/man3/XbaeMatrix.3*

%files -n Xbae-static
%attr(644,root,root) %{_libdir}/libXbae.a
