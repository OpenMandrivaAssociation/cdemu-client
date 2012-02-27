Name:		cdemu-client
Version:	1.5.0
Summary:	Command-line client for controlling CDEmu daemon
Release:	1
Source0:	http://downloads.sourceforge.net/project/cdemu/%{name}/%name-%version.tar.bz2
Group:		Emulators
License:	GPLv2+
URL:		http://cdemu.sourceforge.net/
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	intltool
BuildRequires:	glib-gettextize
Requires:	python-dbus
Requires:	cdemu-daemon >= %{version}
Obsoletes:	cdemu < 0.9
Obsoletes:	python-cdemu < 0.9

%description
This is cdemu-client, a simple command-line client for controlling
CDEmu daemon. It is part of the userspace-cdemu suite, a free, GPL
CD/DVD-ROM device emulator for Linux.

It provides a way to perform the key tasks related to controlling
the CDEmu daemon, such as loading and unloading devices, displaying
devices' status and retrieving/setting devices' debug masks.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS
%{_bindir}/cdemu
%{_mandir}/man1/cdemu.1*
%config(noreplace) %{_sysconfdir}/bash_completion.d/cdemu-bashcomp
%{_datadir}/applications/cdemu-client.desktop
