
%define version 1.0.0
%define snapshot 299
%define rel	2

%if 0
# Update commands:
REV=$(svn info https://cdemu.svn.sourceforge.net/svnroot/cdemu/trunk/cdemu-client | sed -ne 's/^Last Changed Rev: //p')
svn export -r $REV https://cdemu.svn.sourceforge.net/svnroot/cdemu/trunk/cdemu-client cdemu-client-$REV
tar -cjf cdemu-client-$REV.tar.bz2 cdemu-client-$REV
%endif

Name:		cdemu-client
Version:	%version
Summary:	Command-line client for controlling CDEmu daemon
%if %snapshot
Release:	%mkrel 1.svn%snapshot.%rel
Source:		%name-%snapshot.tar.bz2
%else
Release:	%mkrel %rel
Source:		http://downloads.sourceforge.net/cdemu/%name-%version.tar.bz2
%endif
Group:		Emulators
License:	GPLv2+
URL:		http://cdemu.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	intltool
BuildRequires:	glib-gettextize
Requires:	python-dbus
Requires:	cdemu-daemon
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
%if %snapshot
%setup -q -n %name-%snapshot
%else
%setup -q
%endif

%build
%if %snapshot
./autogen.sh
%endif
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS
%{_bindir}/cdemu
%{python_sitelib}/cdemu
%{_mandir}/man1/cdemu.1*
