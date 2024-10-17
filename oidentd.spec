Name:           oidentd
Version:        2.0.8
Release:        8
Summary:        Ident server with masquerading support
License:        GPL
Group:          System/Servers
URL:            https://ojnk.sourceforge.net/
Source0:        http://superb-west.dl.sourceforge.net/sourceforge/ojnk/oidentd-%{version}.tar.gz
Source1:        %{name}.init
Source2:        %{name}.users
Source3:        %{name}.sysconfig
Source4:        %{name}.conf
BuildRequires:  flex
BuildRequires:  bison
Provides:       identd
Requires(pre):  rpm-helper
Requires(post): rpm-helper
Requires(preun): rpm-helper
Requires(postun): rpm-helper

%description
Oidentd is an ident (rfc1413) daemon that runs on Linux, FreeBSD,
OpenBSD and Solaris 2.x. Oidentd supports most features of pidentd
plus more. Most notably, oidentd allows users to specify the identd
response that the server will output when a successful lookup is
completed. Oidentd supports IP masqueraded connections on Linux, and
is able to forward requests to hosts that masq through the host on
which oidentd runs.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%{__mkdir_p} %{buildroot}{%{_sysconfdir}/sysconfig,%{_initrddir}}
%{__cp} -a %{SOURCE1} %{buildroot}%{_initrddir}/%{name} ; chmod 755 %{buildroot}%{_initrddir}/%{name}
%{__cp} -a %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%{__cp} -a %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}_masq.conf
%{__cp} -a %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}.conf
%{__mkdir_p} %{buildroot}%{_localstatedir}/lib/%{name}

%clean
%{__rm} -rf %{buildroot}

%pre
%_pre_useradd %{name} %{_localstatedir}/lib/%{name} /bin/true

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%postun
%_postun_userdel %{name}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README ChangeLog doc/rfc1413
%config(noreplace) %{_sysconfdir}/%{name}_masq.conf
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_initrddir}/%{name}
%{_sbindir}/%{name}
%{_mandir}/*/*
%dir %{_localstatedir}/lib/%{name}


%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 2.0.8-6mdv2011.0
+ Revision: 664795
- rebuild old package

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.0.8-4mdv2010.0
+ Revision: 430197
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.0.8-3mdv2009.0
+ Revision: 254402
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Nov 10 2007 David Walluck <walluck@mandriva.org> 2.0.8-1mdv2008.1
+ Revision: 107348
- really add missing sources
- 2.0.8
- fix Requires syntax
- bunzip all sources
- add missing sources

  + Nicolas Vigier <nvigier@mandriva.com>
    - Import oidentd



* Mon Jan  9 2006 Olivier Blin <oblin@mandriva.com> 2.0.7-9mdk
- proper use of mkrel
- fix typo in initscript

* Mon Jan  9 2006 Olivier Blin <oblin@mandriva.com> 2.0.7-8mdk
- convert parallel init to LSB

* Tue Jan 03 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.7-7mdk
- add parallel init support
- get rid of 3mdk's changelog #2

* Mon Dec 12 2005 Olivier Blin <oblin@mandriva.com> 2.0.7-6mdk
- merge back changelog from current 3mdk

* Mon Oct 10 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.7-3mdk
- fix requires
- fix executable-marked-as-config-file
- %%mkrel

* Mon Oct 10 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.7-5mdk
- rebuild

* Wed Mar 02 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.0.7-4mdk
- add GFDL as license
- add to rfc1413 %%doc

* Wed Mar 02 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.0.7-3mdk
- fix parsing of new ip_conntrack format (P0 from debian)
- drop redundant requires
- fix executable-marked-as-config-file
- cosmetics
- convert changelog to utf-8

* Thu Aug 19 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.0.7-2mdk
- rebuild

* Wed Jul 30 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.0.7-1mdk
- 2.0.7

* Mon Jul 07 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.0.6-1mdk
- 2.0.6

* Tue Feb 25 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.0.5-1mdk
- 2.0.5

* Wed Nov 27 2002 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.0.4-6mdk
- Cleanups
- Fixed init script
- Fix config files

* Mon Oct 21 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.0.4-5mdk
- from Per Øyvind Karlsen <peroyvind@delonic.no> :
	- Cleaned up initscript
	- Fixed permissions

* Mon Oct 14 2002 Per Øyvind Karlsen <peroyvind@delonic.no> 2.0.4-4mdk
- Added own user and group

* Mon Oct 07 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.0.4-3mdk
- from Per Øyvind Karlsen <peroyvind@delonic.no> :
	- Fixed SysV init script
	- Fixed group

* Wed Sep 25 2002 Per Øyvind Karlsen <peroyvind@delonic.no> 2.0.4-2mdk
- Fixed %%post_service and %%preun_service
- Cleanups

* Wed Sep 25 2002 Per Øyvind Karlsen <peroyvind@delonic.no> 2.0.4-1dlc
- Initial release, spec file adopted from PLD
