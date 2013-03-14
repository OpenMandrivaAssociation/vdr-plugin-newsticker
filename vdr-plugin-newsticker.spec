
%define plugin	newsticker
%define name	vdr-plugin-%plugin
%define version	0.0.4
%define rel	18

Summary:	VDR plugin: Newsticker
Name:		%name
Version:	%version
Release:	%rel
Group:		Video
License:	GPL
URL:		http://www.wontorra.net/staticpages/index.php?page=newsticker
Source:		vdr-%plugin-%version.tar.bz2
Patch1:		vdr-newsticker-0.0.4-gcc4.diff
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi
Requires:	wget
BuildRequires:	dos2unix

%description
This plugin downloads rdf news-feeds and displays them on the tv.

%prep
%setup -q -n %plugin-%version
dos2unix *.[ch]
chmod 0644 README HISTORY
%patch1 -p1 -b .extra
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# alternative directory for downloaded files
var=DOWNLOAD_DIR
param="-o DOWNLOAD_DIR"
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
%vdr_plugin_install

install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}/%{plugin}

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%attr(-,vdr,vdr) %dir %{vdr_plugin_cfgdir}/%{plugin}




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.4-16mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.4-15mdv2009.1
+ Revision: 359341
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.4-14mdv2009.0
+ Revision: 197953
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.4-13mdv2009.0
+ Revision: 197695
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.4-12mdv2008.1
+ Revision: 145149
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-11mdv2008.1
+ Revision: 103171
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-10mdv2008.0
+ Revision: 50021
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-9mdv2008.0
+ Revision: 42107
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-8mdv2008.0
+ Revision: 22759
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4-7mdv2007.0
+ Revision: 90946
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4-6mdv2007.1
+ Revision: 74051
- rebuild for new vdr
- Import vdr-plugin-newsticker

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4-2mdv2007.0
- rebuild for new vdr

* Sun Jul 16 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4-1mdv2007.0
- initial Mandriva release

