#
# The sed script required for the hasher project manpages creation.
#
# Copyright (C) 2005  Fr. Br. George <george@altlinux.ru>
# Copyright (c) 2005-2022  Dmitry V. Levin <ldv@altlinux.org>
# All rights reserved.
#
# SPDX-License-Identifier: GPL-2.0-or-later
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
