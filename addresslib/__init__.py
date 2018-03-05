# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from email.parser import Parser
from email.utils import getaddresses
try:
    from email.headerregistry import Address
    text = str
except ImportError:
    from compat import Address
    text = unicode


__all__ = [
    'parse', 'parse_list', 'Address',
]


def parse(s):
    return next(iter(parse_list(s) or []), None)


def parse_list(s):
    s = text(s)
    headers = Parser().parsestr('To: {}'.format(s))
    addresses = []
    address = None
    for display_name, addr_spec in getaddresses(headers.get_all('to', [])):
        if '@' in addr_spec:
            address = Address(display_name=display_name, addr_spec=addr_spec)
        else:
            address = None
        addresses.append(address)
    return addresses
