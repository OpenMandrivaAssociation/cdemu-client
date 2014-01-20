Name:		cdemu-client
Version:	2.0.0
Summary:	Command-line client for controlling CDEmu daemon
Release:	1
Source0:	http://downloads.sourceforge.net/cdemu/%{name}-%{version}.tar.bz2
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
%doc README AUTHORS
%{_bindir}/cdemu
%{_mandir}/man1/cdemu.1*
%config(noreplace) %{_sysconfdir}/bash_completion.d/cdemu-bashcomp
%{_datadir}/applications/cdemu-client.desktop


%changelog
* Mon Feb 27 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.5.0-1
+ Revision: 781104
- update to 1.5.0
- noarch

* Wed Nov 23 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.4.0-1
+ Revision: 732902
- version update requirment fix
- version update to 1.4.0

* Mon Nov 01 2010 Anssi Hannula <anssi@mandriva.org> 1.3.0-3mdv2011.0
+ Revision: 591576
- rebuild for new python

* Sat Sep 04 2010 Anssi Hannula <anssi@mandriva.org> 1.3.0-2mdv2011.0
+ Revision: 575881
- add requirement on python version as the package has files
  in the python version specific directory

* Sat Sep 04 2010 Anssi Hannula <anssi@mandriva.org> 1.3.0-1mdv2011.0
+ Revision: 575786
- new version
- add comment in spec regarding included python files

* Thu Dec 03 2009 Funda Wang <fwang@mandriva.org> 1.2.0-1mdv2010.1
+ Revision: 472923
- New version 1.2.0

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-2mdv2010.0
+ Revision: 436960
- rebuild

* Mon Jan 26 2009 Guillaume Bedot <littletux@mandriva.org> 1.1.0-1mdv2009.1
+ Revision: 333928
- Release 1.1.1950

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 1.0.0-1.svn299.3mdv2009.1
+ Revision: 324172
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-1.svn299.2mdv2009.0
+ Revision: 266475
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 23 2008 Anssi Hannula <anssi@mandriva.org> 1.0.0-1.svn299.1mdv2009.0
+ Revision: 197017
- initial Mandriva release


