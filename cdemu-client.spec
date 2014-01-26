Summary:	Command-line client for controlling CDEmu daemon
Name:		cdemu-client
Version:	2.1.1
Release:	1
Group:		Emulators
License:	GPLv2+
Url:		http://cdemu.sourceforge.net/
Source0:	http://downloads.sourceforge.net/cdemu/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	intltool
BuildRequires:	glib-gettextize
Requires:	python-dbus
Requires:	cdemu-daemon >= %{version}
BuildArch:	noarch

%description
This is cdemu-client, a simple command-line client for controlling
CDEmu daemon. It is part of the userspace-cdemu suite, a free, GPL
CD/DVD-ROM device emulator for linux.

It provides a way to perform the key tasks related to controlling
the CDEmu daemon, such as loading and unloading devices, displaying
devices' status and retrieving/setting devices' debug masks.

%files -f cdemu.lang
%doc README AUTHORS COPYING NEWS ChangeLog
%{_sysconfdir}/bash_completion.d/cdemu-client
%{_bindir}/cdemu
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/cdemu.1*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake -DPOST_INSTALL_HOOKS:BOOL=OFF
%make

%install
%makeinstall_std -C build

%find_lang cdemu

