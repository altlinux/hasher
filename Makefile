#
# $Id$
# Copyright (C) 2003  Dmitry V. Levin <ldv@altlinux.org>
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
HELPERS = functions initroot install mkaptbox mkchroot rebuild rmchroot
PROGRAMS = hsh

bindir = /usr/bin
libexecdir = /usr/share
helperdir = $(libexecdir)/$(PROJECT)
DESTDIR =

MKDIR_P = mkdir -p
INSTALL = install

.PHONY:	all install clean

all:

install: all
	$(MKDIR_P) -m755 $(DESTDIR)$(bindir)
	$(INSTALL) -p -m755 $(PROGRAMS) $(DESTDIR)$(bindir)/
	$(MKDIR_P) -m755 $(DESTDIR)$(helperdir)
	$(INSTALL) -p -m755 $(HELPERS) $(DESTDIR)$(helperdir)/

clean:

