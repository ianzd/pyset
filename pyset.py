#!/usr/bin/env python

import random
import argparse
import sys
import fileinput

class Card ():
    """ Each card in Set has four properties: Color, shape, shading and number
    of symbols. 

    """

    def __init__(self,color,shape,shading,number):
        self.color = color
        self.shape = shape
        self.shading = shading
        self.number = number

    def __repr__(self):
        return str(self.getprops())

    def getprops(self):
        return (self.color,self.shape,self.shading,self.number)

def debugp(message):
    try:
        if args.debug:
            print message
    except NameError:
        pass


def choosecards(deck, number, remove=False):
    """ From a deck, return a list of randomly chosen cards of length "number"
        If remove=True, delete the cards from the deck when chosen


    """

    random.seed()
    selected = []
    while len(selected) < number:
        debugp ("We have %d cards so far." % len(selected))
        newcard = random.choice(deck)
        if not newcard in selected:
            debugp("Adding to set: ")
            debugp(newcard.getprops())
            selected.append(newcard)
            if remove:
                deck.remove(newcard)
        else:
            debugp ("******** Drew duplicate:")
            debugp (newcard.getprops())
            sys.exit
            pass
    debugp ("We have %d cards." % len(selected))
    return selected

def isaset(cards):
    """ Given three cards, return True if they are a set and False if not

    """

    if len(cards) != 3:
        debugp ('A set must be three cards. I was \
        passed %d.' % (len(cards)))
        return False
    uniquecolors = len(set([c.color for c in cards]))
    uniqueshapes = len(set([c.shape for c in cards]))
    uniqueshading = len(set([c.shading for c in cards]))
    uniquenumbers = len(set([c.number for c in cards]))
    if 2 in [uniquecolors, uniqueshapes, uniqueshading, uniquenumbers]:
        return False
    else:
        return True

def builddeck():
    """ Build a standard Set deck of 81 cards

    """

    deck = []
    for color in ('blue', 'red', 'green'):
        for shape in ('oval','diamond','squiggle'):
            for shading in ('solid', 'stripped', 'empty'):
                for number in range(1,4):
                    deck.append(Card(color,shape,shading,number))
    return deck

def parse_options():
    parser = argparse.ArgumentParser('testing');
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--testrun', action='store_true')
    args = parser.parse_args()
    return args

def testrun():
    """ Build a new deck and choose three cards at random until a set
        is found.

    """

    deck = builddeck()
    debugp ("The deck is %d cards." % (len(deck)))
    selected = choosecards(deck,3)
    tries = 1
    while not isaset(selected):
        debugp("Not a set.")
        selected = choosecards(deck,3)
        tries += 1
    print "Got it after %d tries!" % tries
    for c in selected:
        print c

    
if __name__ == '__main__':
    args = parse_options()
    if args.testrun:
        testrun()
        exit
