# $Id$

Name: hasher
Version: 0.9.9.4
Release: alt1
BuildArch: noarch

Summary: An automated package hasher
License: GPL
Group: Development/Other

Source: %name-%version.tar.bz2

Requires: getopt, ash-static, cpio-static, find-static
Requires: hasher-priv, apt >= 0.5.5cnc4.1-alt7
Requires: sisyphus >= 0.5.3-alt1

Obsoletes: pkg-build-utils, libbte

BuildPreReq: help2man

%description
This package provides package hasher utilities.

%prep
%setup -q

%build
%make_build

%install
%make_install install DESTDIR=$RPM_BUILD_ROOT

%files
%_bindir/*
%_datadir/%name
%_mandir/man?/*
%doc FAQ QUICKSTART README

%changelog
* Thu Jun 24 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.9.4-alt1
- functions/print_uris, rebuild, hsh:
  + separate user-defined arguments from command options.

* Wed Jun 23 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.9.3-alt1
- cache_contents, initroot: fix potential breakage
  introduced in previous release.

* Tue Jun 22 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.9.2-alt1
- all:
  + fixed "echo" usage;
  + fixed error handling in "while read" constructions.
- initroot:
  + added support for exotic package filenames.

* Sun Jun 13 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.9.1-alt1
- mkaptbox: include custom apt.conf (if any) to header
  of the generated apt.conf file.
- Minor changes:
  + mkchroot: create chroot/.out with mode 1770 and group gid2.
  + rmchroot: chmod chroot/.out, too.
  + copy_chroot_incoming(): call purge_chroot_in() before copying.
  + do not call purge_chroot_in() before copy_chroot_incoming().

* Tue Feb 03 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.9-alt1
- hsh,rebuild: implemented --rebuild-prog option.
- hsh,install: implemented --pkg-init-list/--pkg-build-list options.
- Added: FAQ, QUICKSTART.

* Sat Jan 31 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.8-alt1
- mkaptbox:
  + added --no-uptdate option;
  + enabled --update mode by default;
  + implemented creation of the apt wrappers in aptbox;
  + added mkaptbox(1) manpage;
  + added %_bindir/mkaptbox symlink.
- Optimized getopt handling code.
- Updated README.

* Tue Jan 13 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.7-alt1
- functions: fixed bug introduced by apt_prefix support.
- create_contents: optimize --no-contents-indices case.
- initroot,cache_chroot: implemented --no-build option.

* Thu Jan 08 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.6-alt1
- functions/print_uris: enhanced error diagnostics.
- functions,mkaptbox,hsh: implemented apt_prefix support.
- functions,initroot,install,rebuild:
  define and export TMPDIR="$HOME/tmp" inside build chroot,
  to ease tracking of illegal /tmp use issues.
- Added hsh(1) manpage.

* Thu Dec 04 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.5-alt1
- mkchroot:
  + install postin program ($HOME/.hasher/install/post
    if available) into /.host/;
- install: execute /.host/postin if available.

* Wed Nov 26 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.4-alt1
- Make use of new rpm-build-4.0.4-alt28 features:
  + initroot: define %%_rpmbuild_clean to 0 in .rpmmacros.
  + initroot,hsh: new option: --repackage-source.

* Sun Nov 02 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.3-alt1
- Extended sisyphus_check support.
- Updated README.

* Mon Oct 27 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.2-alt1
- initroot: changed default packager to hasher@localhost.
- rebuild: pass packager through .rpmmacros.

* Thu Oct 23 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.1-alt1
- Include files inside /etc/ in content index.

* Fri Oct 17 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9-alt1
- Fixed Usage() in all scripts.
- Added sisyphus_check support and enabled it by default.

* Wed Oct 15 2003 Dmitry V. Levin <ldv@altlinux.org> 0.8.4-alt1
- initroot: install all locales by default.
- Updated README.

* Mon Oct 06 2003 Dmitry V. Levin <ldv@altlinux.org> 0.8.3-alt1
- install: call ldconfig after install.
- initroot: be more verbose about filelist generation errors.

* Sun Oct 05 2003 Dmitry V. Levin <ldv@altlinux.org> 0.8.2-alt1
- Added -q/--quiet option.
- install,cache_chroot: be more verbose by default.

* Mon Sep 22 2003 Dmitry V. Levin <ldv@altlinux.org> 0.8.1-alt1
- initroot: manifest hasher via defining __BTE macro
  to "hasher" (#3008).
- Spelling fixes (s/indeces/indices/g).

* Wed Sep 17 2003 Dmitry V. Levin <ldv@altlinux.org> 0.8-alt1
- Implemented initial chroot caching.
- Implemented contents indices caching.
- Implemented support of several contents indices.
  Content indeces are enabled by default, use
  --no-contents-indices option to disable this feature.

* Thu Sep 11 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7-alt1
- Enhanced --no-stuff support.
- Fixed --number support.

* Mon Sep 08 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt1
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
- Updated README.

* Fri Jul 04 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- functions: unset CDPATH.
- rmchroot:
  + explicitly remove /var/tmp/ and /usr/src/ as well as /*/.
- Updated README.

* Thu Jul 03 2003 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Added apt "copy" source method support.
- Enhanced error diagnostics.

* Mon Jun 30 2003 Dmitry V. Levin <ldv@altlinux.org> 0.0.3-alt1
- Initial revision.
