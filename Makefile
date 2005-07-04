#
# $Id$
# Copyright (C) 2003-2005  Dmitry V. Levin <ldv@altlinux.org>
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
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#

PROJECT = hasher
VERSION = $(shell grep ^Version: hasher.spec |head -1 |awk '{print $$2}')
HELPERS = functions cache_chroot cache_contents hsh hsh-install hsh-run hsh-shell initroot mkaptbox mkchroot rebuild rmchroot
PROGRAMS = hsh hsh-install hsh-run hsh-shell mkaptbox
MAN1PAGES = $(PROGRAMS:=.1)
MAN7PAGES = $(PROJECT).7
TARGETS = functions $(MAN1PAGES) $(MAN7PAGES)

deftarget = $(shell uname -m)
bindir = /usr/bin
datadir = /usr/share
libexecdir = /usr/libexec
mandir = $(datadir)/man
man1dir = $(mandir)/man1
man7dir = $(mandir)/man7
helperdir = $(datadir)/$(PROJECT)
binreldir = $(shell relative $(helperdir) $(bindir)/)
DESTDIR =

HELP2MAN1 = help2man -N -s1
INSTALL = install
LN_S = ln -s
MKDIR_P = mkdir -p
TOUCH_R = touch -r

.PHONY:	all install clean

all: $(TARGETS)

$(MAN1PAGES): functions

$(MAN7PAGES):

%: %.in
	sed \
		-e 's,@VERSION@,$(VERSION),g' \
		-e 's,@deftarget@,$(deftarget),g' \
		-e 's,@libexecdir@,$(libexecdir),g' \
		<$< >$@
	$(TOUCH_R) $< $@
	chmod --reference=$< $@

%.1: % %.1.inc
	$(HELP2MAN1) -i $@.inc ./$< >$@

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

clean:
	$(RM) $(TARGETS) *~
