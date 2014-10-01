# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       less

# >> macros
# << macros

Summary:    A text file browser similar to more, but better
Version:    468
Release:    1
Group:      Applications/Text
License:    GPLv3+
URL:        http://www.greenwoodsoftware.com/less/
Source0:    %{name}-%{version}.tar.xz
Source1:    lesspipe.sh
Source2:    less.sh
Source3:    less.csh
Source100:  less.yaml
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
The less utility is a text file browser that resembles more, but has
more capabilities.  Less allows you to move backwards in the file as
well as forwards.  Since less doesn't have to read the entire input file
before it starts, less starts up more quickly than text editors (for
example, vi). 

You should install less because it is a basic utility for viewing text
files, and you'll use it frequently.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
autoreconf

chmod -R a+w *
chmod 644 *.c *.h LICENSE README
# << build pre

%configure --disable-static

# >> build post
make CC="gcc $RPM_OPT_FLAGS -D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64" datadir=%{_docdir}
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%make_install
# << install pre

# >> install post
# splitted post-install part by auto-parsing
strip -R .comment $RPM_BUILD_ROOT/%{_bindir}/less
mkdir -p $RPM_BUILD_ROOT/etc/profile.d
install -p -c -m 755 %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}
install -p -c -m 644 %{SOURCE2} $RPM_BUILD_ROOT/etc/profile.d
install -p -c -m 644 %{SOURCE3} $RPM_BUILD_ROOT/etc/profile.d
ls -la $RPM_BUILD_ROOT/etc/profile.d


# << install post

%files
%defattr(-,root,root,-)
# >> files
%doc LICENSE
/etc/profile.d/*
%{_bindir}/*
%{_mandir}/man1/*
# << files