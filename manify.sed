#
# $Id$
# Copyright (C) 2005  Fr. Br. George <george@altlinux.ru>
# 
# Sed script required for the hasher project manpages creation.
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

/^Options:/,/^Report/{
/^^[[:space:]]*$/a\
Correspondent config file variable, if any, is mentioned by dollar sign\
at the end of option description (\\$like_this).\

/--/{
		h
		s/.*--([[:alnum:]_-]+).*/Var_of_\1/
		s/-/_/g
		x
	}

/;[[:space:]]*$/{
		G
		s/;\n(.*)/\$\{\1\};/
	}
}
