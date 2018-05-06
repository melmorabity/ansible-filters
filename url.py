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


from types import GeneratorType

from ansible.errors import AnsibleFilterError
from ansible.module_utils.six.moves.urllib.parse import urlparse


def _urlparse(url, attribute=None):
    """Parse a URL into six components, returning a 6-tuple. This corresponds to the general
    structure of a URL: scheme://netloc/path;parameters?query#fragment."""

    # Check if value is a list and parse each element
    if isinstance(url, (list, tuple, GeneratorType)):
        result = [_urlparse(u, attribute) for u in url]
        return result or list()

    try:
        parsed = urlparse(url)
    except ValueError:
        raise AnsibleFilterError('Malformated URL')

    if attribute:
        try:
            return getattr(parsed, attribute)
        except AttributeError:
            raise AnsibleFilterError('Invalid attribute {}'.format(attribute))

    return {'scheme': parsed.scheme, 'netloc': parsed.netloc, 'path': parsed.path,
            'params': parsed.params, 'query': parsed.query, 'fragment': parsed.fragment,
            'username': parsed.username, 'password': parsed.password, 'hostname': parsed.hostname,
            'port': parsed.port}


class FilterModule(object):
    """URL manipulation filters."""

    filter_map = {
        'urlparse': _urlparse
    }

    def filters(self):
        return self.filter_map
