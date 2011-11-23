Name:		cdemu-client
Version:	1.4.0
Summary:	Command-line client for controlling CDEmu daemon
Release:	1
Source:		http://downloads.sourceforge.net/cdemu/%name-%version.tar.gz
Group:		Emulators
License:	GPLv2+
URL:		http://cdemu.sourceforge.net/
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
CD/DVD-ROM device emulator for linux.

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
# not used outside this package, for now:
%{_mandir}/man1/cdemu.1*
