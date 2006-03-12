# TODO:
# - use system libs: ffmpeg
# - many missing BR
# - do cleanups in files
# - requires webserver?
# - make subpackages: devel, cgi/webserver
#
# Conditional build:
Summary:	Devolution Security - video surveillance system for the Linux/X11 platform
Name:		devsec
Version:	3.0.6
Release:	0.1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/devsec/%{name}-%{version}.tar.gz
# Source0-md5:	539db08716f0237c8a8c06c25b368b4b
Patch0:		%{name}-no_extern.patch
URL:		http://devsec.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.7
BuildRequires:	faac-devel >= 1.18
BuildRequires:	imlib-devel >= 1.9.14
BuildRequires:	lame-libs-devel >= 3.95
BuildRequires:	libcgi-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtemplate-devel
BuildRequires:	libvorbis-devel
# Required for manuals from ffmpeg (to be removed):
BuildRequires:	perl-tools-pod
# Should be required:
#BuildRequires:	ffmpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
#%%dir %{_sysconfdir}
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
#%{_datadir}/%{name}
#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
#%{_examplesdir}/%{name}-%{version}
%dir %{_pixmapsdir}/%{name}
%{_pixmapsdir}/%{name}/*.png

%{_includedir}/*.h
