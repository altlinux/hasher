#
# Copyright (C) 2003-2007  Dmitry V. Levin <ldv@altlinux.org>
# 
# Makefile for the hasher project.
#
# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA.
#

PROJECT = hasher
VERSION = $(shell sed '/^Version: */!d;s///;q' hasher.spec)
ALIASES = hsh-shell
AUTO_FUNCTIONS = hsh-sh-functions
HELPERS = hsh-buildreq-filter hsh-rpmi-print-files
FUNCTIONS = $(AUTO_FUNCTIONS) hsh-sh-cache-chroot-functions hsh-sh-cache-contents-functions hsh-sh-rebuild-functions
PROGRAMS = hsh hsh-fakedev hsh-initroot hsh-install hsh-mkchroot hsh-rebuild hsh-rmchroot hsh-run mkaptbox
MAN1PAGES = $(PROGRAMS:=.1) $(ALIASES:=.1)
MAN7PAGES = $(PROJECT).7
MANPAGES = $(MAN1PAGES) $(MAN7PAGES)
HTMLPAGES = $(MANPAGES:=.html)
TARGETS = $(MANPAGES)

bindir = /usr/bin
datadir = /usr/share
libexecdir = /usr/libexec
mandir = $(datadir)/man
man1dir = $(mandir)/man1
man7dir = $(mandir)/man7
DESTDIR =

CP = cp -a
HELP2MAN1 = env "PATH=.:$$PATH" help2man -N -s1 -S '$(PROJECT) $(VERSION)'
INSTALL = install
LN_S = ln -s
MAN2HTML = man2html -r
MKDIR_P = mkdir -p
TOUCH_R = touch -r

.PHONY:	all install clean

all: $(TARGETS)

hsh-shell: hsh-run
	$(LN_S) -f $< $@

$(MAN1PAGES): $(AUTO_FUNCTIONS)

$(MAN7PAGES):

%: %.in
	sed \
		-e 's,@VERSION@,$(VERSION),g' \
		-e 's,@libexecdir@,$(libexecdir),g' \
		<$< >$@
	$(TOUCH_R) $< $@
	chmod --reference=$< $@

%._: % manify.sed
	sed -rf manify.sed <$< >$@
	chmod --reference=$< $@

%.1: %._ %.1.inc
	$(HELP2MAN1) -i $(<:._=).1.inc ./$< >$@
	sed -i 's/^\.B $</.B $(<:._=)/' $@

%.html: %
	$(MAN2HTML) $< >$@
	sed -i -e '/^Content-type: /d' -e '/^Time: /d' -e '/index\.html/d' \
		-e 's,HREF="\.\./man./\(hsh\|hasher\.\|mkaptbox\),HREF="\1,g' \
		-e 's,<A HREF="\.\./man./[^/]\+\.html">\([^<]\+\)</A>,\1,g' \
		-e 's,<A HREF="mailto:[^"]\+">\([^@<]\+@[^<]\+\)</A>,\1,' \
		-e 's,\(@altlinux\)\.[a-z]\+,\1,' \
		-e 's,.*\(man2html\).*,\1,' \
		$@

html: $(HTMLPAGES)

install: all
	$(MKDIR_P) -m755 $(DESTDIR)$(bindir)
	$(INSTALL) -pm644 $(FUNCTIONS) $(DESTDIR)$(bindir)/
	$(INSTALL) -pm755 $(HELPERS) $(PROGRAMS) $(DESTDIR)$(bindir)/

	$(MKDIR_P) -m755 $(DESTDIR)$(man1dir)
	$(INSTALL) -pm644 $(MAN1PAGES) $(DESTDIR)$(man1dir)/

	$(MKDIR_P) -m755 $(DESTDIR)$(man7dir)
	$(INSTALL) -pm644 $(MAN7PAGES) $(DESTDIR)$(man7dir)/

	$(CP) $(ALIASES) $(DESTDIR)$(bindir)/

clean:
	$(RM) $(TARGETS) $(HTMLPAGES) $(ALIASES) $(AUTO_FUNCTIONS) *~ *._
