%define debug_package %{nil}

Summary:	A music player for GNOME
Name:		lollypop
Version:	1.4.29
Release:	2
License:	GPLv3+
Group:		Sound
Url:		https://gitlab.gnome.org/World/lollypop/tags
Source0:	https://adishatz.org/lollypop/%{name}-%{version}.tar.xz

BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	appstream-util
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	git
BuildRequires:	meson >= 0.40.0
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(libsoup-2.4)
Requires:	python-dbus
Requires:	python-gi-cairo
Requires:	gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-plugins-ugly
Requires:	typelib(Gst)
Requires:	typelib(GstAudio)
Requires:	typelib(GstPbutils)
Requires:	typelib(GstVideo)
Requires:	typelib(GstTag)
Requires:	typelib(Soup)
Requires:	typelib(TotemPlParser)
# Not imported yet. Disable until it's done (penguin).
#Suggests:	lollypop-portal
#Suggests:	python-pylast
BuildArch:	noarch

%description
Lollypop is a new GNOME music playing application.

%files -f %{name}.lang
%doc AUTHORS
%{_bindir}/%{name}
#{_bindir}/%{name}-cli
%{_libexecdir}/%{name}-sp
%{_datadir}/%{name}
%{_datadir}/metainfo/org.gnome.Lollypop.appdata.xml
%{_datadir}/applications/org.gnome.Lollypop.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.Lollypop.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/org.gnome.Lollypop.SearchProvider.ini
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
%{py3_puresitedir}/%{name}
%doc %{_mandir}/man1/lollypop.1.*
#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome
