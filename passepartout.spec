%define version 0.7.0
%define release %mkrel 1

Name:		passepartout
Summary:	Desktop Publishing for X (PAO)
Version:	%{version}
Release:	%{release}
Url:		http://www.stacken.kth.se/project/pptout/
Source0:	http://www.stacken.kth.se/project/pptout/files/%{name}-%{version}.tar.bz2
Source1:	%{name}-48.png
Source2:	%{name}-32.png
Source3:	%{name}-16.png
Patch0:		passepartout-0.7.0-buildfix.patch
Group:		Publishing
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libxml++1-devel >= 1.0.0
BuildRequires:	gtkmm2.4-devel
BuildRequires:	libgnomecanvasmm2.6-devel
BuildRequires:	fam-devel
Requires:	ghostscript
BuildRequires:	libxslt-proc docbook-dtd412-xml

%description
Passepartout is an Open Source Desktop Publishing application for the
X Windows environment.
The goal of this project is to create a system capable of producing
pre-press material of professional quality, but also to be a useful tool
for any enthusiast with access to a printer.
The main focus is on making it easy for the user to create publications with
a flexible layout, typical examples being magazines, brochures and leaflets.

Passepartout is still in the early stages of development, but it is already
quite usable.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -D -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png

mkdir -p %buildroot%{_datadir}/applications
cat > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Passepartout
Comment=Desktop Publishing for X (PAO)
Exec=passepartout
Icon=passepartout
Type=Application
Categories=GTK;Office;Publishing;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%files
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING INSTALL NEWS
%{_bindir}/*
%{_datadir}/xml/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
