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


EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


def email(address):
    """Check whether a given email address is valid."""

    # Check if value is a list and parse each element
    if isinstance(address, (list, tuple, GeneratorType)):
        result = [email(a) for a in address]
        return result or list()

    return re.match(EMAIL_REGEX, address) is not None


class FilterModule(object):
    """Email validation filters."""

    filter_map = {
        'email': email
    }

    def filters(self):
        return self.filter_map
