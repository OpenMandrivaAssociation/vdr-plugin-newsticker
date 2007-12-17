
%define plugin	newsticker
%define name	vdr-plugin-%plugin
%define version	0.0.4
%define rel	11

Summary:	VDR plugin: Newsticker
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.wontorra.net/staticpages/index.php?page=newsticker
Source:		vdr-%plugin-%version.tar.bz2
Patch1:		vdr-newsticker-0.0.4-gcc4.diff
BuildRequires:	vdr-devel >= 1.4.1-6
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

%vdr_plugin_params_begin %plugin
# alternative directory for downloaded files
var=DOWNLOAD_DIR
param="-o DOWNLOAD_DIR"
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}/%{plugin}

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%attr(-,vdr,vdr) %dir %{_vdr_plugin_cfgdir}/%{plugin}


