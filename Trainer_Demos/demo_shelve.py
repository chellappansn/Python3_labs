#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""
import shelve

movies = { 'joe': ['lotr', 'rocky', 'interstellar'],
           'merrick': ['matrix', 'godfather', 'godfather II'],
           'niteen': ['godfather', '3idiots', 'benjamin button'],
}

tv_series = { 'joe': ['yellowstone', 'luther'],
              'merrick': ['rings of power', 'the penguin'],
              'niteen': ['lost', 'la raina del sue']
}

books = { 'joe': 'the pleasure of finding things out',
          'merrick': 'sherlock holmes',
          'niteen': 'world war z'
}

with shelve.open(r"c:\labs\projects\Python3_labs\Trainer_Demos\medie") as db:
    db['movies'] = movies
    db['tv_series'] = tv_series
    db['books'] = books

with shelve.open(r"c:\labs\projects\Python3_labs\Trainer_Demos\medie") as db:
    print(f"Joe's favourite movies are {db['movies']}")
    print(f"Merrick's favourite tv_seres is {db['tv_series']['merrick'][0]}")
    print(f"Niteen's favourite book is {db['books']['niteen']}")



