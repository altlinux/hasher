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
HELPERS = functions cache_chroot cache_contents hsh hsh-install hsh-run initroot mkaptbox mkchroot rebuild rmchroot
PROGRAMS = hsh hsh-install hsh-run mkaptbox
MAN1PAGES = $(PROGRAMS:=.1)
MAN7PAGES = $(PROJECT).7
TARGETS = functions $(MAN1PAGES) $(MAN7PAGES)

bindir = /usr/bin
datadir = /usr/share
libexecdir = /usr/libexec
mandir = $(datadir)/man
man1dir = $(mandir)/man1
man7dir = $(mandir)/man7
helperdir = $(datadir)/$(PROJECT)
binreldir = $(shell relative $(helperdir) $(bindir)/)
DESTDIR =

HELP2MAN1 = env PATH=":$$PATH" help2man -N -s1 -S '$(PROJECT) $(VERSION)'
INSTALL = install
LN_S = ln -s
MKDIR_P = mkdir -p
TOUCH_R = touch -r

.PHONY:	all symlinks install clean

all: $(TARGETS)

symlinks:
	$(LN_S) -f hsh-run hsh-shell
	$(LN_S) -f hsh-install install

$(MAN1PAGES): functions

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

install: all
	$(MKDIR_P) -m755 $(DESTDIR)$(helperdir)
	$(INSTALL) -p -m755 $(HELPERS) $(DESTDIR)$(helperdir)/
	$(LN_S) hsh-install $(DESTDIR)$(helperdir)/install
	$(MKDIR_P) -m755 $(DESTDIR)$(man1dir)
	$(INSTALL) -p -m644 $(MAN1PAGES) $(DESTDIR)$(man1dir)/
	$(MKDIR_P) -m755 $(DESTDIR)$(man7dir)
	$(INSTALL) -p -m644 $(MAN7PAGES) $(DESTDIR)$(man7dir)/
	$(MKDIR_P) -m755 $(DESTDIR)$(bindir)
	$(LN_S) $(PROGRAMS:%=$(binreldir)/%) $(DESTDIR)$(bindir)/
	$(LN_S) hsh-run $(DESTDIR)$(helperdir)/hsh-shell
	$(LN_S) hsh-run.1 $(DESTDIR)$(man1dir)/hsh-shell.1
	$(LN_S) $(binreldir)/hsh-shell $(DESTDIR)$(bindir)/

clean:
	$(RM) $(TARGETS) hsh-shell install *~ *._
