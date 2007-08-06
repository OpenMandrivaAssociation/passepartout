%define version 0.5
%define release 1mdk

Name:		passepartout
Summary:	Desktop Publishing for X (PAO)
Version:	%{version}
Release:	%{release}
Url:		http://www.stacken.kth.se/project/pptout/
Source0:	http://www.stacken.kth.se/project/pptout/files/%{name}-%{version}.tar.bz2
Source1:	%{name}-48.png
Source2:	%{name}-32.png
Source3:	%{name}-16.png
Group:		Publishing
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libxml++1.0-devel >= 1.0.0
BuildRequires:	gtkmm2.0-devel
BuildRequires:	libgnomecanvasmm2.0-devel
BuildRequires:	fam-devel
Requires:	ghostscript
Requires:	libxslt-proc

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

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# ugly hack to put docs in the right dir
mv $RPM_BUILD_ROOT%{_docdir}/%{name} docdir

# fix symlinks pointing to BuilRoot
#ln -sf %{_datadir}/xml/%{name}/docbook.xslt docdir/
#ln -sf %{_datadir}/xml/%{name}/docbook.xslt docdir/examples/
#ln -sf %{_datadir}/xml/%{name}/xhtml.xslt docdir/
#ln -sf %{_datadir}/xml/%{name}/xhtml.xslt docdir/examples/

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} << EOF
?package(%{name}): command="%{_bindir}/%{name}" icon="%{name}.png" section="Office/Publishing" title="Passepartout" longtitle="Desktop Publishing for X (PAO)" needs="x11"
EOF

install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -D -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING INSTALL NEWS docdir/*
%{_bindir}/*
%{_datadir}/xml/%{name}
%{_mandir}/man1/*

%{_menudir}/%{name}
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
