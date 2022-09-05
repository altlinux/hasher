.\" Additional documentation for the hsh command.
.\"
.\" Copyright (C) 2003-2022  Dmitry V. Levin <ldv@altlinux.org>
.\" All rights reserved.
.\"
.\" SPDX-License-Identifier: GPL-2.0-or-later

[NAME]
hsh \- build package using hasher utilities

[OPTIONS]
.TP
.BR \-\-with\-stuff " / " \-\-without\-stuff
Controls whether to use results of previous builds stored in
.IR <path\-to\-workdir> /repo
during setup of a new build environment.  Default is to use this stuff.
($no_stuff);
.TP
.BR \-\-number = \fINUMBER
Choose a subconfig identifier (positive integer).  By default, simultaneous
builds are not allowed, so user can do at most a single build in every
point of time.  To overcome this restriction, an additional pseudouser
pairs should be created by
.BR hasher\-useradd (8).
The subconfig identifier defines the pair to use.  Additionally, when
\fINUMBER\fR starts with slash character, it specifies a directory
to deduce the subconfig identifier from.
($number);
.TP
.BR \-\-mountpoints = \fILIST
Comma-separated list of known mount points.  Every build dependency that
belongs to this list will be mounted.  If some mount point is not explicitly
allowed in
.BR hasher\-priv.conf (5),
then the build will fail.
($known_mountpoints);

[FILES]
.B ~/.hasher/config
- user config file sourced by all hasher utilities; uses shell syntax.
.TP
.B ~/.hasher/install/post
- postinstall script;
.B mkchroot
copies it into chroot, and
.B install
executes the copy at the end of the package installation transaction.
.TP
Working directory contents:
.TP
.B aptbox
- created automatically by
.BR mkaptbox (1),
required for apt.
.TP
.B cache
- build environment and rpm database cache, created automatically
by initroot.
.TP
.B chroot
- build environment, created automatically by mkchroot.
.TP
.B pid
- pid file, handled internally by
.BR hsh .
.TP
.B repo
- package repository, contains the build results.

[SEE ALSO]
.BR mkaptbox (1),
.BR hsh\-initroot (1),
.BR hsh\-install (1),
.BR hsh\-mkchroot (1),
.BR hsh\-rebuild (1),
.BR hsh\-rmchroot (1),
.BR hsh\-run (1),
.BR hasher\-priv.conf (5),
.BR hasher (7),
.BR hasher\-useradd (8).
