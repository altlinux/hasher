Name: hasher
Version: 1.3.0
Release: alt1

Summary: Modern safe package building technology
License: GPL
Group: Development/Other
Url: ftp://ftp.altlinux.org/pub/people/ldv/hasher
Packager: Dmitry V. Levin <ldv@altlinux.org>
BuildArch: noarch

Source: %url/%name-%version.tar

%define _libexecdir %_prefix/libexec
%define helperdir %_libexecdir/%name-priv

Requires: %helperdir
Requires: getopt, ash-static, cpio-static, find-static
Requires: apt-utils >= 0:0.5.5cnc4.1-alt7
# due to "enable -f /usr/lib/bash/lockf lockf"
Requires: bash-builtin-lockf >= 0:0.2
# due to "readlink -e"
Requires: coreutils >= 0:5.2.1-alt3
# due to "hasher-priv getconf"
Requires: hasher-priv >= 0:1.2.11
# due to prepare_x11_forwarding()
Requires: mktemp >= 1:1.3.1

Obsoletes: pkg-build-utils, libbte

BuildPreReq: help2man

%description
This package contains package hasher user utilities.
See %_docdir/%name-%version/QUICKSTART for details.

%prep
%setup -q

%build
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%_bindir/*
%_mandir/man?/*
%doc FAQ QUICKSTART README apt.conf *.sh

%changelog
* Fri Oct 19 2007 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt1
- Changed utilities to lock workdir by default.
- Changed utilities which operate with prepared chroot to
  deduce subconfig identifier from chroot directory ownership.
- Changed workdir locking algorithm to lock workdir itself.
- Implemented hasher-priv locking.
- hsh, hsh-mkchroot: Choose subconfig identifier randomly
  unless --number option is used.
- Enabled wait-for-lock behavior by default.
  Added --wait-lock/--no-wait-lock options to control wait mode.

* Mon Oct 08 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.9-alt1
- hsh-sh-functions.in (lock_workdir, hasher_exit_handler):
  Do not remove pid file.

* Sat Oct 06 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.8-alt1
- hsh-sh-functions.in (lock_workdir):
  Rewritten locking using lockf bash builtin.
- hsh, hsh-fakedev, hsh-install, hsh-run, hsh-sh-functions.in:
  Added --wait-lock/--no-wait-lock options.

* Tue Sep 18 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.7-alt1
- mkaptbox: If setarch does not support given arch, do not use setarch.
- hsh-rebuild: Added --source-only and --install-only options.
- Redirected chrootuid{1,2} stdin to /dev/null where appropriate.
- hsh-initroot: Replaced non-portable rpminit with raw initialization (#11586).

* Wed Aug 29 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.6-alt1
- hsh-fakedev, hsh-sh-functions.in, mkaptbox:
  Secured readlink(1) usage (ldv).
- Added qemu support (kas).
- mkaptbox:
  Added setarch to apt wrappers (ldv).
- cache-contents-functions:
  Refactored; introduced contents_index_all (at).
- Implemented alternative cache directory support (legion, ldv).
- hsh-sh-functions.in (lock_workdir):
  Rewritten locking using lock files (ldv).
- Run grep in C locale to speedup grep calls (ldv).
- hsh-sh-rebuild-functions:
  Fixed pkg.tar build deps filter (legion, ldv).

* Mon May 21 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.5-alt1
- hsh-initroot: Do not pass --nodeps option to rpmi
  unless some packages were filtered out (avm).
- hasher.7.in: Fixed man section number (#11613).
- hsh-initroot: Fixed --pkg-{init,build}-list=+ support
  (Sergey Kurakin, #11827).
- hsh-fakedev: Implemented fifo support (#11811).

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.4-alt1
- hsh-fakedev: Fixed typo in -g option support (sbolshakov, #11489).

* Sun Apr 08 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt1
- mkaptbox: When copying files from Dir::State::lists,
  take only readable files into account.

* Thu Mar 29 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt1
- mkaptbox: If cdroms.list is not empty,
  copy it and apt indices into aptbox.

* Mon Mar 12 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- hsh-fakedev:
  + Enhanced error diagnostics.
  + Fixed hsh-run(1) invocation to propagate --number and --hasher-priv-dir options.
- hsh-sh-functions.in (opt_check_number):
  + Disallowed numbers starting with zero.
  + Optimized check to avoid execution of extra processes.
  Suggested by Sergey Vlasov.

* Wed Feb 21 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.0-alt1
- Fixed build to use plain "cp -a" for better portability.
- hsh-fakedev: New utility, creates fake device files.
- mkaptbox:
  Disabled creation of internal repository in --without-stuff mode.

* Thu Jan 11 2007 Dmitry V. Levin <ldv@altlinux.org> 1.1.1-alt1
- mkaptbox: Implemented absolute repository path support in --repo
  (Alex Myltsev).
- Fixed required mountpoints calculation regression introduced in
  previous release.

* Thu Jan 04 2007 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt1
- Removed boldface from the NAME section of man pages;
  suggested by Sergey Vlasov.
- Made all hasher utilities available for external use.
- Moved hasher function files to %_bindir/ as well.
- hsh-rebuild:
  Factored out rebuild functions to hsh-sh-rebuild-functions file.
- hsh-sh-cache-contents-functions (create_contents):
  Ignore missing cache/contents/list.new/index file (#9844).
- hsh-shell: Removed redundant --execute and --pty options.
- hsh-install, hsh-rebuild, hsh-run, hsh-shell:
  Deprecated --save-fakeroot option.
- Changed set_workdir() and utilities to allow $workdir to be
  defined in config file instead of command argument, and
  changed default $workdir value to $HOME/hasher;
  suggested by Mikhail Yakshin.
- Updated documentation to reflect these changes.

* Sun Dec 10 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.35-alt1
- apt.conf: Use C-style comments (#10158).
- FAQ: Updated section about remote repositories (#10167).
- functions (create_entry_fakeroot_header): Load/save fakeroot state
  iff /.fakedata exists, regardless of --save-fakeroot value (#10313).

* Mon Sep 04 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.34-alt1
- rebuild:
  + Pass --target option to "rpmbuild -bE" and "rpmbuild -bs" invocations.
  + Honor "rpmbuild -bE" exit code.
- cache_chroot:
  + Invalidate chroot cache in case of fakeroot options change.
- functions, hsh, mkaptbox, rebuild:
  + New options: --repo-bin, --repo-src (legion@).

* Wed May 31 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.33-alt1
- functions, mkaptbox:
  + Changed def_target and current_arch values to whatever rpm decides.

* Thu May 25 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.32-alt1
- hsh, initroot: Implemented --packager option.
- rebuild: Enhanced srpm detection.

* Fri May 12 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.31-alt1
- Changed code to use aptbox wrappers instead of direct apt commands.
- rebuild: make_srpm_from_pkgtar: filter_spec_buildreq: Ignore deps with %% symbol.
- mkaptbox: Create aptbox version of ~/.rpmrc if necessary.
- mkaptbox: Create regenbasedir wrapper.

* Fri May 05 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.30-alt1
- Enhanced $hasher_dir initialization, to make execution of
  hasher placed to exotic custom directory work as designed.
- rebuild: Handle tar packages made by gear utility.

* Mon Apr 10 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.29-alt1
- rebuild:
  + Do not export $target variable in default rebuild script.
- mkaptbox:
  + When creating internal apt.conf, place user apt config after
    internal Dir::State and Dir::Cache, to let users override
    these directories (legion@).
  + Cleanup apt wrappers (legion@).
- Removed keywords used for CVS keyword substitution.

* Tue Feb 21 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.28-alt1
- functions (print_uris): Fixed package download implementation
  to support mixed repos (see #8902).

* Fri Feb 17 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.27-alt1
- cache_chroot: Use find and cpio from host system
  if native tools are not available.
- initroot: Added --pkg-{init,build}-list=+ syntax (closes #9102).
- hsh-run: Added optional argument to --shell option (closes #9103).

* Sun Feb 12 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.26-alt1
- Enhanced manpages, based on idea and implementation
  from George Kouryachy.
- Parametrized default values for most of program options,
  see manpages for details.
- Parametrized rpmi: use $rpmi to override default rpmi.
- rebuild --query-repackage: allow undefined rpm macros
  during repackage.
- hsh-install: honor noinstall_pattern_list parameter like
  in initroot stage.
- Added example apt.conf file to documentation.

* Tue Nov 29 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.25-alt1
- initroot: Adopted "prepare /proc and /sys for potential mount"
  code to work in --save-fakeroot mode.
- hsh: New options: --eager-cleanup/--lazy-cleanup
  (option names suggested by Alexey Rusakov).
  Changed default operation mode to --eager-cleanup.

* Sat Nov 26 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.24-alt1
- rebuild: s/--reply=yes/-f/ (closes #8325).
- cache_chroot, hsh-install: Corrected check for
  adjust_kernel_headers presense before execution.
- Fixed hasher_dir initialization, to make execution of hasher
  placed to custom directory work as designed.
- functions (print_uris): Implemented package download using
  APT::Get::PrintLocalFile option (closes #8121).
- rebuild: Pass target to /.host/rebuild.

* Sun Oct 09 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.23-alt1
- initroot: new option: --pkg-noinstall-pattern-list.
- cache_chroot: fixed workaround for the dev package,
  implemented new initroot's option support.

* Mon Sep 05 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.22-alt1
- Changed default target to $(uname -m).
- Made the package noarch again.
- Updated FSF postal address.

* Sat Aug 13 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.21-alt1
- hsh-run: new options: --pty, --shell.
- hsh-shell: obsoleted by "hsh-run --shell".

* Mon Aug 01 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.20-alt1
- Fixed --number option support which was broken as result of
  previous cleanup.

* Tue Jul 05 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.19-alt1
- hsh-run(1): changed usage semantics.
- functions:
  new functions: parse_xauth_entry, prepare_x11_forwarding.
- hsh-run(1), hsh-shell(1):
  added options to control X11 forwarding.
- Fixed build with make-3.81beta3.
- Cleaned up options parser.

* Fri Jun 17 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.18-alt1
- cache_chroot (create_chroot):
  Fixed grave chroot initialization bug introduced in 1.0.17.

* Sun Jun 12 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.17-alt1
- cache_chroot, cache_contents: save cache validation data
  after cache regeneration.
- mkchroot: create /dev symlinks.
- hsh(1), hsh-shell(1), cache_chroot, initroot, install,
  rebuild, rmchroot: implemented --save-fakeroot option.
- hsh-install(1), hsh-run(1): New programs.

* Fri May 27 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.16-alt1
- rebuild: pass sources as arguments to query-req-prog script.
- cache_chroot: caller user and/or group may exist,
  do not fail when unable to create them.
- Added query-req-prog and rebuild-prog examples.

* Tue May 17 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.15-alt1
- hsh(1): new option: --cleanup-only.
- hsh(1), rebuild: new option: --query-repackage.
- initroot: copy /etc/skel contents to the builder's homedir.
- cache_chroot: create group and passwd entries for caller
  and pseudoroot users.
- functions: new function: show_usage.
- Reduced size of usage messages to necessary minimum.
- Enforced policy on messages format.
- hsh-shell(1): new program.
- FAQ: updated.

* Tue May 03 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.14-alt1
- rebuild: really handle --mountpoints as comma-separated list
  [take 3].
- functions,hsh,mkaptbox,rebuild:
  + new option: --repo (Ivan Fedorov, closes #6739).
- hsh,initroot:
  + new option: --no-repackage-source;
  + repackage source by default.

* Sun Apr 10 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.13-alt1
- Fixed handling of options with file or dir arguments.
- rebuild: really handle --mountpoints as comma-separated list.
- Documented --without-stuff instead of --no-stuff as preferred
  way to build without internal package repository.

* Wed Mar 16 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.12-alt1
- mkaptbox: fixed regression introduced by previous change.

* Tue Mar 15 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.11-alt1
- hsh: handle traps in more portable way.
- rmchroot: chgrp chroot directory itself, too.
- functions/{get_apt_config,read_apt_config}: new functions.
- mkaptbox: use them.

* Tue Jan 25 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.10-alt1
- functions: removed no longer needed "am I root?" sanity check
  (fixes #5869).
- hsh(1), rebuild: implemented --query-req-prog option.

* Mon Jan 03 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.9-alt1
- Changed hasher-priv helper directory to %helperdir,
  updated package dependencies.
- install: export RPM_EXCLUDEDOCS=1 if $exclude_docs is set.
- functions: source user config from ~/.hasher/config if any.
- hsh,initroot,install,rebuild: added --excludedocs option.
- Unhardcoded work limits (fixes #5804).
- Updated documentation:
  + hasher(7): applied fixes from Egor Grebnev;
  + hsh(1), mkaptbox(1): added NAME section.
  + hsh(1): document ~/.hasher/config and ~/.hasher/install/post.

* Thu Nov 11 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0.8-alt1
- hsh: enhanced early diagnostics for invalid source files.

* Tue Nov 09 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0.7-alt1
- cache_contents: fixed find warning.
- mkaptbox: create wrapper for genbasedir.

* Thu Aug 26 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0.6-alt1
- rebuild: enhanced --mountpoints implementation.

* Wed Aug 25 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0.5-alt1
- rmchroot: fixed bug introduced in previous release.

* Thu Aug 19 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0.4-alt1
- rmchroot:
  + increased time limits;
  + when verbose mode is set, be more verbose.
- Updated package dependencies.

* Sun Aug 08 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0.3-alt1
- initroot,install,mkchroot,rebuild,rmchroot:
  + implemented --version parameter.
- rebuild:
  + calculate required mountpoints from installed file dependencies.
- Updated FAQ.

* Tue Aug 03 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt1
- rebuild: run rebuild script as login shell.
- Added multilib support.

* Mon Jul 26 2004 Kachalov Anton <mouse@altlinux.ru> 1.0.1-alt2
- Added libdir, deftarget variables to makefile

* Mon Jul 19 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0.1-alt1
- initroot:
  + removed --no-build option, use --pkg-build-list= instead.
- hsh, initroot:
  + handle comma as package name delimiter in values of the
    --pkg-init-list and --pkg-build-list options.
- hsh:
  + new option: --initroot-only.
- archive_chroot_cache:
  + optimized find/cpio.

* Thu Jul 15 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt1
- Added hasher(7) manpage.
- Added more docs to hsh(1) manpage.
- Updated FAQ.

* Fri Jul 09 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.9.7-alt1
- Implemented mount/umount support.

* Wed Jul 07 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.9.6-alt1
- rebuild:
  + execute sisyphus_check for source package
    before analysis of its build dependencies;
  + execute all sisyphus_check calls inside chroot;
  + execute query for packager inside chroot.
- initroot: added sisyphus_check>=0:0.7.3 to build list.
- README: described this change.
- cache_chroot,initroot,rebuild,rmchroot:
  + Added wlimit hints for each chrootuid call.

* Sat Jul 03 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.9.5-alt1
- cache_chroot: recognize dev_* as dev-*, too.

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
