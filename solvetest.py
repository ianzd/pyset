#!/usr/bin/env python

""" A couple of simple methods for finding sets

"""

from pyset import Card, choosecards, isaset, builddeck
import hashlib

def isaset_m(cards, memo):
    """ Memoizing wrapper for isaset()

    """

    h = hashlib.md5()

    cards = sorted(cards)
    h.update(str(cards))
    cardhash = h.digest
    
    if cardhash in memo.keys():
        return memo[cardhash]
    else:
        result = isaset(cards)
        memo[cardhash] = result
        return result

def randsolve(cards):
    """ Attempts to find sets through random selection

    """
    trycards = choosecards(cards, 3)
    maxattempts = 100000
    attempts = 1

    while not isaset(trycards) and attempts < maxattempts:
        attempts += 1
        trycards = choosecards(cards, 3)

    if isaset(trycards):
        print "Set found in %d attempts:" % attempts
        print trycards
    else:
        print "No set found in %s attempts." % attempts

def randsolve_m(cards):
    """ Attempts to find sets through random selection using isaset_m

    """
    trycards = choosecards(cards, 3)
    maxattempts = 100000
    attempts = 1

    memo = {}

    while not isaset_m(trycards, memo) and attempts < maxattempts:
        attempts += 1
        trycards = choosecards(cards, 3)

    if isaset(trycards):
        print "Set found in %d attempts:" % attempts
        print trycards
    else:
        print "No set found in %s attempts." % attempts



deck = builddeck()
board = []

board.extend(choosecards(deck, 9, remove=True))

print "Board:"
print board
randsolve(board)
randsolve_m(board)

