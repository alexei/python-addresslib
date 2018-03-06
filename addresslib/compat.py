# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from builtins import str

from email.utils import formataddr, parseaddr


class Address(object):
    def __init__(self, display_name='', username='', domain='', addr_spec=None):
        if addr_spec is not None:
            _display_name, address = parseaddr(addr_spec)
            if _display_name:
                display_name = _display_name
            username, domain = address.split('@')

        self._display_name = str(display_name)
        self._username = username
        self._domain = domain

    @property
    def display_name(self):
        return self._display_name

    @property
    def username(self):
        return self._username

    @property
    def domain(self):
        return self._domain

    @property
    def addr_spec(self):
        return '{}@{}'.format(self.username, self.domain)

    def __repr__(self):
        return '{}(display_name={!r}, username={!r}, domain={!r})'.format(
            self.__class__.__name__,
            self.display_name, self.username, self.domain)

    def __str__(self):
        return formataddr((self.display_name, self.addr_spec))

    def __eq__(self, other):
        if type(other) != type(self):
            return False

        return (self.display_name == other.display_name and
                self.username == other.username and
                self.domain == other.domain)
