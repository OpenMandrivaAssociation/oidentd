Name:           oidentd
Version:        2.0.8
Release:        %mkrel 6
Summary:        Ident server with masquerading support
License:        GPL
Group:          System/Servers
URL:            http://ojnk.sourceforge.net/
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
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{_initrddir}/%{name}
%{_mandir}/*/*
%dir %{_localstatedir}/lib/%{name}
