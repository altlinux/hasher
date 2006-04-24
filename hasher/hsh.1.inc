.\" Copyright (C) 2003-2006  Dmitry V. Levin <ldv@altlinux.org>
.\" 
.\" Additional documentation for the hsh command.
.\"
.\" This file is free software; you can redistribute it and/or modify
.\" it under the terms of the GNU General Public License as published by
.\" the Free Software Foundation; either version 2 of the License, or
.\" (at your option) any later version.
.\" 
.\" This program is distributed in the hope that it will be useful,
.\" but WITHOUT ANY WARRANTY; without even the implied warranty of
.\" MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
.\" GNU General Public License for more details.
.\" 
.\" You should have received a copy of the GNU General Public License
.\" along with this program; if not, write to the Free Software
.\" Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA.

[NAME]
\fBhsh\fR \- build package using hasher utilities

[OPTIONS]
.TP
.BR \-\-with\-stuff " / " \-\-without\-stuff
Controls whether to use results of previous builds stored in
.IR <path\-to\-workdir> /repo
during setup of new build environment.
Default is to use this stuff.
.TP
\fB\-\-number\fR=\fINUMBER\fR
Choose subconfig identifier (positive integer).  By default, simultaneous
builds are not allowed, so user can do at most single build in every
point of time.  To overcome this restriction, additional pseudouser
pairs should be created by
.BR hasher\-useradd (8).
The subconfig identifier defines the pair to use.
.TP
\fB\-\-mountpoints\fR=\fILIST\fR
Defines list of known mount points.  Every build dependence which belongs
to this list will be mounted.  If some mount point is not explicitly
allowed in
.BR hasher\-useradd.conf (5),
build will fail.

[FILES]
.B ~/.hasher/config
- user config file sourced by all hasher utilities; uses shell syntax.
.TP
.B ~/.hasher/install/post
- postinstall script;
.B mkchroot
copies it into chroot, and
.B install
executes the copy at the end of package installation transaction.
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
.B lockdir
- lock directory, handled internally by
.BR hsh .
.TP
.B repo
- package repository, contains build results.

[SEE ALSO]
.BR mkaptbox (1),
.BR hsh\-install (1),
.BR hsh\-run (1),
.BR hasher\-useradd.conf (5),
.BR hasher (7),
.BR hasher\-useradd (8).
