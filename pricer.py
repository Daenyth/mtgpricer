#!/usr/bin/env python2

import json
import urllib
import urllib2


def getprice(cardname):
    cardinfo = getcard(cardname)
    return min(c['price'] for c in cardinfo)

def getcard(cardname):
    url = 'http://blacklotusproject.com/json/?cards=' + urllib.quote(cardname)
    cardinfo = json.load(urllib2.urlopen(url))
    return cardinfo['cards']

