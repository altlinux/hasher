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
HELPERS = functions cache_chroot cache_contents initroot install mkaptbox mkchroot rebuild rmchroot
PROGRAMS = hsh
MAN1PAGES = hsh.1

bindir = /usr/bin
libexecdir = /usr/share
mandir = /usr/share/man
man1dir = $(mandir)/man1
helperdir = $(libexecdir)/$(PROJECT)
DESTDIR =

MKDIR_P = mkdir -p
INSTALL = install
HELP2MAN1 = help2man -N -s1

.PHONY:	all install clean

all: $(MAN1PAGES)

%.1: %
	$(HELP2MAN1) ./$< > $@

install: all
	$(MKDIR_P) -m755 $(DESTDIR)$(bindir)
	$(INSTALL) -p -m755 $(PROGRAMS) $(DESTDIR)$(bindir)/
	$(MKDIR_P) -m755 $(DESTDIR)$(helperdir)
	$(INSTALL) -p -m755 $(HELPERS) $(DESTDIR)$(helperdir)/
	$(MKDIR_P) -m755 $(DESTDIR)$(man1dir)
	$(INSTALL) -p -m644 $(MAN1PAGES) $(DESTDIR)$(man1dir)/

clean:

