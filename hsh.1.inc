$Id$

/show this text and exit/
.SS "Working directory contents:"
.TP
aptbox
\- created automatically by 
.BR mkaptbox (1),
required for apt.
.TP
cache
\- build environment and rpm database cache, created automatically
by initroot.
.TP
chroot
\- build environment, created automatically by mkchroot.
.TP
lockdir
\- lock directory, handled internally by
.BR hsh .
.TP
repo
\- package repository, contains build results.
.SH OPTIONS
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
.BR \-\-repackage\-source
Controls whether to repackage source package during build together with
binary packages.  Default is to package binary packages only.
.TP
\fB\-\-mountpoints\fR=\fILIST\fR
Defines list of known mount points.  Every build dependence which belongs
to this list will be mounted.  If some mount point is not explicitly
allowed in
.BR hasher\-useradd.conf (5),
build will fail.

[SEE ALSO]
.BR mkaptbox (1),
.BR hasher\-useradd.conf (5),
.BR hasher (7),
.BR hasher\-useradd (8).
