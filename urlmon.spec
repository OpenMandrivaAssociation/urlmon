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



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 4.0-8mdv2010.0
+ Revision: 434586
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 4.0-7mdv2009.0
+ Revision: 261805
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 4.0-6mdv2009.0
+ Revision: 255255
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 4.0-4mdv2008.1
+ Revision: 128806
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import urlmon


* Wed Apr 02 2003 Lenny Cartier <lenny@mandrakesoft.com> 4.0-4mdk
- requires
- noarch

* Wed Sep 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 4.0-3mdk
- rebuild

* Tue Apr 10 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 4.0-2mdk
- sanitized specfile (s/Copyright/License)

* Tue Feb 27 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 4.0-1mdk
- First Mandrake package

# end of file
