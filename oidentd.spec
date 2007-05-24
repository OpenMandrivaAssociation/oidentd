%define	name	oidentd
%define	version	2.0.7
%define	release	%mkrel 9

Summary:	Ident server with masquerading support
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL GFDL
Group:		System/Servers
Source0:	http://prdownloads.sourceforge.net/ojnk/%{name}-%{version}.tar.bz2
Source1:	%{name}.init.bz2
Source2:	%{name}.users.bz2
Source3:	%{name}.sysconfig.bz2
Source4:	%{name}.conf.bz2
Patch0:		oidentd-2.0.7-fix-parsing-of-new-ip-conntrack-format.patch.bz2
URL:		http://ojnk.sourceforge.net/
BuildRequires:	flex bison
Provides:	identd
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(pre,post,preun,postun):	rpm-helper

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
%patch0 -p1 -b .new_conntrack_format

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/sysconfig,%{_initrddir}}
bzcat %{SOURCE1} > $RPM_BUILD_ROOT%{_initrddir}/%{name} ; chmod 755 $RPM_BUILD_ROOT%{_initrddir}/%{name}
bzcat %{SOURCE3} > $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
bzcat %{SOURCE2} > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}_masq.conf
bzcat %{SOURCE4} > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf
install -d $RPM_BUILD_ROOT%{_localstatedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%_pre_useradd %{name} %{_localstatedir}/%{name} /bin/true

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
%{_initrddir}/%{name}
%{_mandir}/*/*
%dir %{_localstatedir}/%{name}
