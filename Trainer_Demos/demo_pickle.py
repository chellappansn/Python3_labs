#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO PRESERVE ONE PYTHON object
# (data + structure) to a file using the pickle module.
"""
    Docstring:
"""
import pickle
import pprint
import gzip # Other modules for compressing/archiving bz2, shutil, tarfile

movies = { 'joe': ['lotr', 'rocky', 'interstellar'],
           'merrick': ['matrix', 'godfather', 'godfather II'],
           'niteen': ['godfather', '3idiots', 'benjamin button'],
           'brad': ['jaws', 'star wars', 'rocky'],
           'mahendran': ['top gun', 'terminator', 'rambo']
}

# Open PICKLE file for WRITING in BINARY mode.
# with open(r"c:\labs\projects\Python3_labs\Trainer_Demos\movies.p", mode="wb") as fh_out:
with gzip.open(r"c:\labs\projects\Python3_labs\Trainer_Demos\movies.pgz", mode="wb") as fh_out:
    # pickle.dump(movies, fh_out, protocol=5) # Pickle Protocol (0-5, 0=ASCII, 1-5=BINARY)
    # pickle.dump(movies, fh_out, protocol=pickle.HIGHEST_PROTOCOL)  # Default=4
    pickle.dump(movies, fh_out, protocol=pickle.DEFAULT_PROTOCOL)  # Highest=5

# Open PICKLE file for READING in BINARY mode.
# with open(r"c:\labs\projects\Python3_labs\Trainer_Demos\movies.p", mode="rb") as fh_in:
with gzip.open(r"c:\labs\projects\Python3_labs\Trainer_Demos\movies.pgz", mode="rb") as fh_in:
    films = pickle.load(fh_in)

pprint.pprint(movies)
print("-" * 60)
pprint.pprint(films)