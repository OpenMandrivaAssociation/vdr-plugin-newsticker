%define plugin	newsticker

Summary:	VDR plugin: Newsticker
Name:		vdr-plugin-%plugin
Version:	0.0.4
Release:	20
Group:		Video
License:	GPL
URL:		http://www.wontorra.net/staticpages/index.php?page=newsticker
Source:		vdr-%plugin-%{version}.tar.bz2
Patch1:		vdr-newsticker-0.0.4-gcc4.diff
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi
Requires:	wget
BuildRequires:	dos2unix

%description
This plugin downloads rdf news-feeds and displays them on the tv.

%prep
%setup -q -n %plugin-%{version}
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
%doc README HISTORY
%attr(-,vdr,vdr) %dir %{vdr_plugin_cfgdir}/%{plugin}




