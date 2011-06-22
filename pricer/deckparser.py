#!/usr/bin/env python2

from . import deck

def parse_deck(filename):
    """
    Parse a file on disk into a Deck object
    """
    deckname = None
    maindeck = []
    sideboard  = []
    with open(filename) as f:
        for line in f:
            if not line:
                continue
            elif line.startswith('//NAME: '):
                deckname = line.split(None, 1)[1]
            elif line.startswith('//'):
                # Line is a comment
                continue
            elif line.startswith('SB: '):
                _, quantity, cardname = line.split(None, 2)
                for i in range(quantity):
                    sideboard.append(deck.Card(cardname))
            else:
                quantity, cardname = line.split(None, 1)
                for i in range(quantity):
                    maindeck.append(deck.Card(cardname))

    return deck.Deck(deckname, maindeck, sideboard)

