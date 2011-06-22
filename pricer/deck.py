#!/usr/bin/env python2

from . import pricer

class Deck(object):
    def __init__(self, maindeck, sideboard):
        self.maindeck = [Card(c) for c in maindeck]
        self.sideboard = [Card(c) for c in sideboard]

    def __len__(self):
        return len(self.cardlist)

    def cardlist(self):
        return self.maindeck + self.sideboard

    def price(self, proxy_count):
        unproxied_count = len(self) - proxy_count
        return sum(sorted([c.price for c in self.cardlist])[:unproxied_count])

class Card(object):
    __borg_state = {}
    def __init__(self, cardname):
        # Borg pattern
        if cardname not in self.__borg_state:
            self.__borg_state[cardname] = {}
        self.__dict__ = self.__borg_state[cardname]

        self.name = cardname
        self._price = None

    @property
    def price(self):
        if self._price is None:
            self._price = pricer.getprice(self.name)
        return self._price

