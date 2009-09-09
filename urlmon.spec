%define name	urlmon
%define version	4.0
%define release	%mkrel 8

Summary:	An URL monitor
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		urlmon-4.0-perl-path.patch.bz2
License:	GPL
Group:		Networking/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Url: http://www.ibiblio.org/pub/Linux/apps/www/mirroring/
Requires:	perl >= 5
Requires:	perl-Digest-MD5
Requires:	perl-libnet
Requires:	perl-MIME-Base64
Requires:	perl-HTML-Parser
Requires:	perl-libwww-perl
Requires:	perl-MD5
Buildarch:	noarch

%description
urlmon makes a connection to a web site and records the last_modified
time for that url. Upon subsequent calls, it will check the URL again,
this time comparing the information to the previously recorded
times. Since the last_modified data is not required to be given by the
http (it's optional), urlmon will then take an MD5 checksum.  This is
actually more accurate, as time stamps can be faked or
inaccurate. Filtering is possible, so that URLs whose content is
always changing (due to server-side parsing or some equivalent, as
often used in rotating adverstisements) can accurately be monitored.

%prep
%setup
%patch0 -p1 -b .perl-path

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d %buildroot/%_bindir
install -m 755 urlmon %buildroot/%_bindir
install -m 755 nscape2urlmon %buildroot/%_bindir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.txt FILTERS.txt MODULES.txt URLMONRC.txt COPYING
%doc contrib
%_bindir/urlmon
%_bindir/nscape2urlmon

