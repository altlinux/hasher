# $Id$

Name: hasher
Version: 0.0.1
Release: alt1
BuildArch: noarch

Summary: A Package Hasher
License: GPL
Group: Development/Other

Source: %name-%version.tar.gz

Requires: getopt, ash-static, cpio-static, rm-static
Requires: pkg-build-priv >= 0.2.1

%description
This package provides package hasher utilities.

%prep
%setup -q

%install
%make_install install DESTDIR=$RPM_BUILD_ROOT

%files
%_bindir/*
%_datadir/*

%changelog
* Mon Jun 30 2003 Dmitry V. Levin <ldv@altlinux.org> 0.0.1-alt1
- Initial revision.
