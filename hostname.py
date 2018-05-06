#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2017 Mohamed El Morabity
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not,
# see <http://www.gnu.org/licenses/>.


import re
from types import GeneratorType


# https://stackoverflow.com/a/20204811
HOSTNAME_REGEX = r'(?=^.{1,253}$)(^(((?!-)[a-zA-Z0-9-]{1,63}(?<!-))|' \
                 r'((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,63})$)'


def hostname(host):
    """Check whether a given hostname is valid according to the following conditions:
       * Hostnames are composed of a series of labels concatenated with dots. Each label is 1 to 63
         characters long, and may contain:
         - the ASCII letters a-z (in a case insensitive manner),
         - the digits 0-9,
         - and the hyphen ('-').
       * Additionally:
         - labels cannot start or end with hyphens (RFC 952)
         - labels can start with numbers (RFC 1123)
         - max length of ascii hostname including dots is 253 characters (not counting trailing dot)
           (http://blogs.msdn.com/b/oldnewthing/archive/2012/04/12/10292868.aspx)
         - underscores are not allowed in hostnames (but are allowed in other DNS types)
       * some assumptions:
         - TLD is at least 2 characters and only a-z
         - TLD is optional
    """

    # Check if value is a list and parse each element
    if isinstance(host, (list, tuple, GeneratorType)):
        result = [hostname(h) for h in host]
        return result or list()

    return re.match(HOSTNAME_REGEX, host) is not None


class FilterModule(object):
    """Hostname validation filters."""

    filter_map = {
        'hostname': hostname
    }

    def filters(self):
        return self.filter_map
