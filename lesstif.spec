Summary:	LessTif - source compatible library with OSF/Motif® 1.2
Name:		lesstif
Version:	0.87.9
Release:	1
#Release:	@DATE@
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.lesstif.org/pub/hungry/lesstif/srcdist/%{name}-%{version}.tar.gz
#Source0:	ftp://ftp.lesstif.org/pub/hungry/lesstif/srcdist/%{name}-current.tar.gz
Patch0:		lesstif.optflags.patch
Icon:		lesstif-realsmall.gif
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	lesstif-M20, lesstif-M12

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
Group(pl):	X11/Programowanie/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains the lesstif header files required to develop Motif 1.2
based applications.

%package static
Summary:	Static Lesstif library
Copyright:	LGPL
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains the lesstif static libraries.

%prep
%setup -q
#%setup -q -n %{name}-current
%patch0 -p1

#find . -name CVS -exec rm -rf {} \; 2> /dev/null ||

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure	--prefix=/usr/X11R6 \
		--enable-shared \
		--enable-static \
		--enable-production \
		--disable-debug \
		--enable-build-12

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11
make install \
	prefix=$RPM_BUILD_ROOT/usr/X11R6 \
	mrmdir=$RPM_BUILD_ROOT/usr/X11R6/include/Mrm \
	xmdir=$RPM_BUILD_ROOT/usr/X11R6/include/Xm \
	man1dir=$RPM_BUILD_ROOT/usr/X11R6/man/man1 \
	man3dir=$RPM_BUILD_ROOT/usr/X11R6/man/man3 \
	man5dir=$RPM_BUILD_ROOT/usr/X11R6/man/man5 \
	htmldir=$RPM_BUILD_ROOT/home/httpd/html/Lesstif-%{version}

strip $RPM_BUILD_ROOT/usr/X11R6/{lib/lib*.so,bin/{mwm,uil,xmbind}}

# mwm
ln -sf ../../usr/X11R6/lib/X11/mwm $RPM_BUILD_ROOT/etc/X11/mwm

rm -f doc/INSTALL.html

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man*/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root)/usr/X11R6/lib/lib*.so.*.*
%attr(644,root,root) /usr/X11R6/man/man1/lesstif.1.*

%files mwm
%defattr(644,root,root,755)
%doc clients/Motif-1.2/mwm/README doc/MWM.txt
%dir /etc/X11/mwm
%dir /usr/X11R6/lib/X11/mwm
%attr(755,root,root) /usr/X11R6/bin/mwm

%config /usr/X11R6/lib/X11/mwm/*
%config /usr/X11R6/lib/X11/app-defaults/*

/usr/X11R6/man/man1/mwm.1.*
/usr/X11R6/man/man5/mwmrc.5.*

%files clients
%attr(644,root,root,755)
%doc doc/UIL.txt
%attr(755,root,root) /usr/X11R6/bin/uil
%attr(755,root,root) /usr/X11R6/bin/xmbind
/usr/X11R6/man/man1/xmbind.1.*

%files devel
%defattr(644, root, root, 755)
%doc AUTHORS BUG-REPORTING CREDITS CURRENT_NOTES ChangeLog KNOWN_BUGS NEWS
%doc NOTES README RELEASE-POLICY TODO
%doc doc/*.txt doc/*.html doc/www.lesstif.org/{images/*gif,*html}

%docdir /home/httpd/html/Lesstif-%{version}
%doc /home/httpd/html/Lesstif-%{version}/*

%attr(755,root,root) /usr/X11R6/lib/lib*.so

/usr/X11R6/include/Mrm
/usr/X11R6/include/Xm

/usr/X11R6/man/man3/*

%files static
%attr(644,root,root) /usr/X11R6/lib/lib*.a

%changelog
* Sat Feb 27 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.87.9-1]
- simplifications in %files,
- added %doc for /home/httpd/html/Lesstif-%%{version}/* files,
- changed permission to 755 on /usr/X11R6/lib/lib*.so,
- changed Group in static and devel to X11/Development/Libraries,
- added Group(pl),
- added gzipping man pages,
- removed man group from man pages.

* Sun Aug 30 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.86.0]
- all %doc moved from main package to devel,
- changed perrmissions on shared libraries to 755,
- added static subpackage.
 
* Sun Jun  7 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.85-1]
- added --disable-debug configure parameter,
- fixed few typos.

* Wed May 20 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.84-1]
- %%{version} macro instead %%{PACKAGE_VERSION},
- added -q %setup parameter,
- added using %%{name} macro in Buildroot,
- added "Requires: %%{name} = %%{version}" for mwm,
- added documentation in html (/home/httpd/html/Lesstif-%%{version}),
- changed file list with documentation included to packages also added man3
  pages and html documentation to dever subpackage,
- added %defattr macro in %files (require rpm >= 2.4.99; recomended >= 2.5).

* Mon Mar 16 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.83-1]
- added -q parameter for %setup,
- now lesstif is compiled as copatible with Motif 1.2,
- added %defattr macro,
- removed patching sources for diffrent platforms,
- runing /configure moved to %buid,
- changed source URL,
- added Icon to main and devel subpackage,
- added using $RPM_OPT_FLAGS in CFLAGS,
- removed -n parameter from %setup (it is not neccessary),
- changed Group for main package also changed Group for devel
  subpackage to Development/Libraries/X11,
- removed lesstif-M*  subpackages,
- rearanged Copyright filds,
- fiew simplification in %files,
- added stripping /usr/X11R6/bin/{mwm,uil,xmbind},
- added package icon (lesstif-realsmall.gif),
- removwd Imake config files (files from XFree86-devel have similar
  functionality),
- removed Packager field (if you want recompile and redisstrubute this stuff
  put this field in your own ~/.rpmrc).

* Fri Nov 21 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.82-1]
- added "Requires: lesstif-%%{PACKAGE_VERSION}" for devel,
- changed Copyright to GPL, LGPL,
- changed --enable-build configure option from 12 to 20 (Motif 2.0 not
  completly testet by me; please report any problems),
- added M20 package,
- in M12 and M20 lesstif shared libs maked with Motiff 1.2/2.0 libs version,
- added X resources for mwm.

* Mon Sep 15 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.81-2]
- added missing links libXm.so libMrm.so to devel,

* Wed Sep 10 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.81-1]
- changed alle %attr for %doc to (-, root, root),

* Sun Jul 20 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.80-2]
- added to all %doc %attr macros (this allows build package from normal user
  account),
- some simplification in %files (%doc).

* Wed Jul 9 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- added using %%{PACKAGE_VERSION} macro in "Source:" and %files,
- added additional parameter "--enable-build-12" to runing configure,
- added %postun and %clear,
- in %post and %postun ldconfig is called as parameter with "-p"
  (this feature is avalable in rpm >= 2.4.3 and you must have this
  version and if you want recompile package from src.rpm you must have new
  version rpm),
- added package lesstif-M12 simple Motif 1.2 wrapper,
- simplified %install section,
- added %attr macros in %files sections,
- added stripping shared libraries,
- added URL field,
- added Lessdox - a html development documentation to lesstif-devel,
- added lesstif-0.80public-nopedantic.patch, this allow compile lesstif on
  sparc by removing "-pedantic" from CFLAGS.
