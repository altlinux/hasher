.\" Copyright (C) 2021  Arseny Maslennikov <arseny@altlinux.org>
.\"
.\" Additional documentation for the hsh-copy command.
.\"
.\" SPDX-License-Identifier: GPL-2.0-or-later

[NAME]
hsh\-copy \- put specified file or directory inside hasher chroot

[NOTES]
The current implementation of hsh\-copy(1) uses cpio(1) to transfer file
object trees inside the chroot, so if cpio cannot reproduce a particular inode
attribute, it will not be present in the destination file.

[EXAMPLES]
.PP
\fBExample\ \&1.\ \&Set /etc/resolv\&.conf in the chroot, then run a shell inside in the host\&'s netns\fR
.sp
.nf
$ printf '%s\\n' 'nameserver 2001:db8::53' > resolv\&.conf
$ hsh-copy --rooter --workdir $TMP/hasher resolv\&.conf /etc
$ share_network=1 hsh-shell --workdir $TMP/hasher
.fi
.PP
\fBExample\ \&2.\ \&Copy the user's various rc files to builder's $HOME in the chroot\fR
.sp
.nf
$ hsh-copy --workdir $TMP/hasher ~/\&.gitconfig ~/\&.vimrc ~/\&.zshrc \&.
$ hsh-copy --workdir $TMP/hasher ~/\&.vim \&.vim
.fi

[SEE ALSO]
.BR hsh-run (1),
.BR hsh (1).
