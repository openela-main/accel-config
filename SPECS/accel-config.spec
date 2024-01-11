%global	project_name	idxd-config

Name:		accel-config
Version:	3.5.3
Release:	1%{?dist}
Summary:	Configure accelerator subsystem devices
# The entire source code is under GPLv2 except for accel-config
# library which is mostly LGPLv2, ccan/list which is BSD-MIT and
# the rest of ccan which is CC0.
License:	GPLv2 and LGPLv2+ and MIT and CC0
URL:		https://github.com/intel/%{project_name}
Source0:	%{URL}/archive/%{name}-v%{version}.tar.gz
Patch0: 0001-testing-vercheck.patch

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires:	gcc
BuildRequires:	autoconf
BuildRequires:	asciidoc
BuildRequires:	xmlto
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libkmod)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	systemd

# accel-config is for configuring Intel DSA (Data-Streaming
# Accelerator) subsystem in the Linux kernel. It supports x86 only.
ExclusiveArch:	%{ix86} x86_64

%description
Utility library for configuring the accelerator subsystem.

%package devel
Summary:	Development files for libaccfg
License:	LGPLv2+
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package libs
Summary:	Configuration library for accelerator subsystem devices
# All source code of configuration library is LGPLv2, except
# ccan/list which is BSD-MIT and the rest of ccan/ which is CC0.
License:	LGPLv2+ and MIT and CC0
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description libs
Libraries for %{name}.

%package test
Summary:        Tests for accel-config
License:        GPLv2
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description test
Tests for accel-config command.

%prep
%autosetup -p1 -n %{project_name}-%{name}-v%{version}

%build
echo %{version} > version
./autogen.sh
%configure --disable-static --disable-silent-rules --enable-test
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%check
make check

%files
%license Documentation/COPYING licenses/BSD-MIT licenses/CC0
%license licenses/accel-config-licenses LICENSE_GPL_2_0
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_sysconfdir}/%{name}/contrib/configs/*

%files libs
%doc README.md
%license Documentation/COPYING licenses/BSD-MIT licenses/CC0
%license licenses/libaccel-config-licenses accfg/lib/LICENSE_LGPL_2_1
%{_libdir}/lib%{name}.so.*

%files devel
%license Documentation/COPYING
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%files test
%license Documentation/COPYING LICENSE_GPL_2_0
#%doc test/README.md
%{_libexecdir}/accel-config/test/*

%changelog
* Tue Apr 18 2023 Jerry Snitselaar <jsnitsel@redhat.com> - 3.5.3-1
- Rebase to 3.5.3 release.
resolves: rhbz#2153898

* Sun Oct 16 2022 Jerry Snitselaar <jsnitsel@redhat.com> - 3.5.0-1
- Rebase to the 3.5.0 release.
resolves: rhbz#2101608

* Thu Oct 06 2022 Jerry Snitselaar <jsnitsel@redhat.com> - 3.4.8-1
- Rebase to 3.4.8 release.
resolves: rhbz#2101608

* Sun Apr 03 2022 Jerry Snitselaar <jsnitsel@redhat.com> - 3.4.6.3-1
- Rebase to 3.4.6.3 release.
resolves: rhbz#2040076

* Thu Sep 09 2021 Jerry Snitselaar <jsnitsel@redhat.com> - 3.4.2-1
- Rebase to 3.4.2 and add test subpackage.
resolves: rhbz#1971910

* Tue May 18 2021 Jerry Snitselaar <jsnitsel@redhat.com> - 3.1-1
- Rebase to 3.1 release.
resolves: rhbz#1920762

* Fri Nov 6 2020 Yunying Sun <yunying.sun@intel.com> - 2.8-1
- Initial Packaging
