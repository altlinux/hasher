# $Id$

Name: hasher
Version: 0.2
Release: alt1
BuildArch: noarch

Summary: An automated package hasher
License: GPL
Group: Development/Other

Source: %name-%version.tar.gz

Requires: getopt, ash-static, cpio-static, rm-static
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
* Fri Jul 04 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- functions: unset CDPATH.
- rmchroot:
  explicitly remove /var/tmp/ and /usr/src/ as well as /*/.

* Thu Jul 03 2003 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Added apt "copy" source method support.
- Enhanced error diagnostics.

* Mon Jun 30 2003 Dmitry V. Levin <ldv@altlinux.org> 0.0.3-alt1
- Initial revision.
