# $Id$

Name: hasher
Version: 0.5.1
Release: alt1
BuildArch: noarch

Summary: An automated package hasher
License: GPL
Group: Development/Other

Source: %name-%version.tar.gz

Requires: getopt, ash-static, cpio-static, find-static
Requires: hasher-priv, apt >= 0.5.5cnc4.1-alt5

Obsoletes: pkg-build-utils, libbte

%description
This package provides package hasher utilities.

%prep
%setup -q

%install
%make_install install DESTDIR=$RPM_BUILD_ROOT

%files
%_bindir/*
%_datadir/*
%doc README

%changelog
* Sun Sep 07 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt1
- hsh:
  + implemented locking.
- mkaptbox:
  + implemented more rigorous apt-config error checking.
- initroot:
  + create /dev/log socket.

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5-alt1
- functions:
  + relaxed umask: 077 -> 022.
- initroot:
  + fixed nprocs initialization (#0002861, imz).

* Mon Aug 11 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt1
- rmchroot:
  + install .host programs if required;
  + use "find -delete" instead of "rm -rf".
- mkaptbox:
  + added --target option (#0002817);
  + added --apt-config option.
- hsh:
  + pass --target and --apt-config to mkaptbox.

* Wed Jul 30 2003 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Added "adjust_kernel_headers --first" support.
- rmchroot:
  + explicitly remove /var/lib/texmf/ as well.

* Fri Jul 04 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- functions: unset CDPATH.
- rmchroot:
  + explicitly remove /var/tmp/ and /usr/src/ as well as /*/.

* Thu Jul 03 2003 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Added apt "copy" source method support.
- Enhanced error diagnostics.

* Mon Jun 30 2003 Dmitry V. Levin <ldv@altlinux.org> 0.0.3-alt1
- Initial revision.
