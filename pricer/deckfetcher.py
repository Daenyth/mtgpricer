#!/usr/bin/env python2

import re
import urllib2

from BeautifulSoup import BeautifulSoup, SoupStrainer


def get_tourneys(limit=10):
    """
    Return links to the most recent `limit` tourneys listed on morphling.de

    This function only scrapes the first page of tourney results
    """
    archive_url = 'http://morphling.de/top8archives.php?format=1&sorting=DESC'
    strainer = SoupStrainer('a', href=re.compile('top8decks.php'))
    soup = BeautifulSoup(urllib2.urlopen(archive_url))

    # Increase limit by 20 because the headers contain 10 each of vintage and legacy results
    return soup.findAll(strainer, limit=limit+20)[20:]

def get_deck_links(tourney_url):
    """
    Return links to all .dec files in the top 8 of a tournament

    tourney_url: The url of the tournament listing on morphling.de
    """
    soup = BeautifulSoup(urllib2.urlopen(tourney_url))
    strainer = SoupStrainer('a', href=re.compile('decks/appr/.*\.dec$'))
    return soup.findAll(strainer)

