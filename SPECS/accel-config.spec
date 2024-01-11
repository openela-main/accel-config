%global	project_name	idxd-config

Name:		accel-config
Version:	3.5.3
Release:	2%{?dist}
Summary:	Configure accelerator subsystem devices
# The entire source code is under GPLv2 except for accel-config
# library which is mostly LGPLv2.1, ccan/list which is BSD-MIT and
# the rest of ccan which is CC0.
License:	GPLv2 and LGPLv2+ and MIT and CC0
URL:		https://github.com/intel/%{project_name}
Source0:	%{URL}/archive/%{name}-v%{version}.tar.gz

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
BuildRequires:	make

# accel-config is for configuring Intel DSA (Data-Streaming
# Accelerator) subsystem in the Linux kernel. It supports x86_64 only.
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
# All source code of configuration library is LGPLv2.1, except
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
%license licenses/accel-config-licenses accfg/lib/LICENSE_LGPL_2_1
%{_libdir}/lib%{name}.so.*

%files devel
%license Documentation/COPYING
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%files test
%license Documentation/COPYING LICENSE_GPL_2_0
%doc test/README.md
%{_libexecdir}/accel-config/test/*

%changelog
* Tue Apr 18 2023 Jerry Snitselaar <jsnitsel@redhat.com> - 3.5.3-2
- Remove spec file variable that blocked debuginfo build
Resolves: rhz#2153899

* Tue Apr 18 2023 Jerry Snitselaar <jsnitsel@redhat.com> - 3.5.3-1
- Rebase to the 3.5.3 release.
Resolves: rhbz#2153899

* Tue Oct 04 2022 Jerry Snitselaar <jsnitsel@redhat.com> - 3.5.0-1
- Rebase to 3.5.0 release.
Resolves: rhbz#2101609

* Sun Apr 03 2022 Jerry Snitselaar <jsnitsel@redhat.com> - 3.4.6.3-1
- Rebase to 3.4.6.3 release.
Resolves: rhbz#2040077

* Fri Feb 11 2022 Jerry Snitselaar <jsnitsel@redhat.com> - 3.4.2-2
- Rebuild to clear osci test failure.
Resolves: rhbz#1999934

* Tue Oct 05 2021 Jerry Snitselaar <jsnitsel@redhat.com> - 3.4.2-1
- Rebase to 3.4.2 release and add test subpackage.
Resolves: rhbz#1999934

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 3.2-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Jul 02 2021 Jerry Snitselaar <jsnitsel@redhat.com> - 3.2-2
- Fix product version for gating.
Resolves: rhbz#1921368

* Mon Jun 21 2021 Jerry Snitselaar <jsnitsel@redhat.com> - 3.2-1
- Rebase to 3.2 release. Related: rhbz#1921368

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 3.1-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Mar 29 2021 Yunying Sun <yunying.sun@intel.com> - 3.1-1
- Added ix86 support back as 3.1 release fixed it
- Updated to 3.1 release

* Thu Feb 18 2021 Yunying Sun <yunying.sun@intel.com> - 3.0.1-1
- Updated to 3.0.1 release
- Removed ix86 support as so far it supports x86_64 only
- Updated licenses following upstream

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 6 2020 Yunying Sun <yunying.sun@intel.com> - 2.8-1
- Initial Packaging
