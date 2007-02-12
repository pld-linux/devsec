# TODO:
# - use system libs: ffmpeg!!, mpeg4ip
# - requires webserver?
# - move cgi files to webappdir, move html files to own directory
# - add webapps configuration
# - move camera configs to /etc
#
Summary:	Devolution Security - video surveillance system for the Linux/X11 platform
Summary(pl.UTF-8):   Devolution Security - system do nadzoru obrazu dla platformy Linux/X11
Name:		devsec
Version:	3.0.6
Release:	0.2
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/devsec/%{name}-%{version}.tar.gz
# Source0-md5:	539db08716f0237c8a8c06c25b368b4b
Patch0:		%{name}-no_extern.patch
URL:		http://devsec.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.7
BuildRequires:	faac-devel >= 1.18
# Should be required:
#BuildRequires:	ffmpeg-devel
BuildRequires:	imlib-devel >= 1.9.14
BuildRequires:	lame-libs-devel >= 3.95
BuildRequires:	libcgi-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtemplate-devel
BuildRequires:	libvorbis-devel
# Required for manuals from ffmpeg (to be removed):
BuildRequires:	perl-tools-pod
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_webappdir	%{_prefix}/lib/%{_webapp}

%description
Devolution Security is a video surveillance system for the Linux/X11
platform. Features:
 - Up to 16 cameras
 - Motion detection
 - Record on motion detection
 - Record up to 25 fps MPEG4 video
 - Multicast live streams to local network
 - Unicast to internet IP address
 - Very configurable
 - Themeable X11 interface
 - Configurable helper buttons
 - Web based interface

%description -l pl.UTF-8
Devolution Security to system do nadzoru obrazu dla platformy
Linux/X11. Możliwości:
 - do 16 kamer
 - wykrywanie ruchu
 - nagrywanie przy wykryciu ruchu
 - nagrywanie obrazu MPEG4 do 25 klatek/sekundę
 - udostępnianie strumieni na żywo w sieci lokalnej
 - kierowanie strumienia na internetowy adres IP
 - duża konfigurowalność
 - interfejs X11 z obsługą motywów
 - konfigurowalne przyciski pomocnicze
 - interfejs WWW

%package cgi
Summary:	Web based interface for Devolution Security
Summary(pl.UTF-8):   Interfejs WWW do Devolution Security
Group:		Applications/WWW
Requires:       %{name} = %{version}-%{release}
Requires:	webapps

%description cgi
Web based interface for Devolution Security.

%description cgi -l pl.UTF-8
Interfejs WWW do Devolution Security.

%package libs
Summary:	Devolution Security libraries
Summary(pl.UTF-8):   Biblioteki Devolution Security
Group:		Libraries

%description libs
Devolution Security libraries.

%description libs -l pl.UTF-8
Biblioteki Devolution Security.

%package devel
Summary:	Header files for Devolution Security libraries
Summary(pl.UTF-8):   Pliki nagłówkowe bibliotek Devolution Security
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for Devolution Security libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Devolution Security.

%package static
Summary:	Static Devolution Security libraries
Summary(pl.UTF-8):   Statyczne biblioteki Devolution Security
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Devolution Security libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Devolution Security.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_webapps}/%{_webapp},%{_webappdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CONSUMER_KEYS ChangeLog README
#%%dir %{_sysconfdir}
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/dtk
%dir %{_libdir}/dtk/config
%dir %{_libdir}/dtk/config/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_libdir}/dtk/config/%{name}/*.conf
%dir %{_libdir}/dtk/config/%{name}/messages
%{_libdir}/dtk/config/%{name}/messages/*.ulaw
%dir %{_libdir}/dtk/config/%{name}/mp4live
%config(noreplace) %verify(not md5 mtime size) %{_libdir}/dtk/config/%{name}/mp4live/*.conf
%dir %{_libdir}/dtk/skins
%attr(755,root,root) %{_libdir}/dtk/skins/*.so
%{_libdir}/dtk/skins/*.la
%dir %{_pixmapsdir}/%{name}
%{_pixmapsdir}/%{name}/*.png
%{_pixmapsdir}/%{name}/*.yuv

%files cgi
%defattr(644,root,root,755)
%attr(755,root,root) /home/httpd/cgi-bin/index.cgi
/home/httpd/cgi-bin/templates
/home/httpd/html/*.css
/home/httpd/html/*.html
%dir /home/httpd/html/images
/home/httpd/html/images/*.jpg
/home/httpd/html/images/*.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
