#
# $Id$
# Copyright (C) 2003, 2004  Dmitry V. Levin <ldv@altlinux.org>
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
HELPERS = functions cache_chroot cache_contents hsh initroot install mkaptbox mkchroot rebuild rmchroot
PROGRAMS = hsh mkaptbox
MAN1PAGES = $(PROGRAMS:=.1)
TARGETS = $(PROGRAMS) $(MAN1PAGES)

bindir = /usr/bin
libexecdir = /usr/share
mandir = /usr/share/man
man1dir = $(mandir)/man1
helperdir = $(libexecdir)/$(PROJECT)
binreldir = $(shell relative $(helperdir) $(bindir)/)
DESTDIR =

HELP2MAN1 = help2man -N -s1
INSTALL = install
LN_S = ln -s
MKDIR_P = mkdir -p

.PHONY:	all install clean

all: $(TARGETS)

%: %.in
	sed -e 's/@VERSION@/$(VERSION)/g' <$< >$@
	chmod a+x $@

%.1: %
	$(HELP2MAN1) ./$< > $@

install: all
	$(MKDIR_P) -m755 $(DESTDIR)$(helperdir)
	$(INSTALL) -p -m755 $(HELPERS) $(DESTDIR)$(helperdir)/
	$(MKDIR_P) -m755 $(DESTDIR)$(man1dir)
	$(INSTALL) -p -m644 $(MAN1PAGES) $(DESTDIR)$(man1dir)/
	$(MKDIR_P) -m755 $(DESTDIR)$(bindir)
	$(LN_S) $(PROGRAMS:%=$(binreldir)/%) $(DESTDIR)$(bindir)/

clean:
	$(RM) $(TARGETS) *~
