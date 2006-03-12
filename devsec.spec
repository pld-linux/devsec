# TODO:
# - use system libs: ffmpeg!!, mpeg4ip
# - requires webserver?
# - move cgi files to webappdir, move html files to own directory
# - add webapps configuration
# - move camera configs to /etc
#
# Conditional build:
Summary:	Devolution Security - video surveillance system for the Linux/X11 platform
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
%define		_webappdir	%{_prefix}/lib/cgi-bin/%{_webapp}

%description
Devolution Security is a video surveillance system for the Linux/X11 platform.
Features:
 - Up to 16 cameras
 - Motion detection
 - Record on motion detection
 - Record up to 25 fps mpeg4 video
 - Multicast live streams to local network
 - Unicast to internet IP address
 - Very configurable
 - Themeable X11 interface
 - Configurable helper buttons
 - Web based interface

%package cgi
Summary:	cgi files for devsec
Group:		Applications/WWW
Requires:       %{name} = %{version}-%{release}
Requires:	webapps

%description cgi

%package libs
Summary:        libraries for devsec
Summary(pl):    Biblioteki do devsec
Group:          Libraries

%description libs
Libraries for Devolution Security.

%description libs -l pl
Biblioteki dla Devolution Security.

%package devel
Summary:        Developement files for devsec
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}

%description devel
Developement files for devsec.

%package static
Summary:        Static libraries for devsec
Summary(pl):    Statyczne biblioteki devsec
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description static
Static library for devsec.

%description static -l pl
Statyczne biblioteki devsec.

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
%{_libdir}/dtk/skins/*.la
%{_libdir}/dtk/skins/*.so
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
%{_libdir}/*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
