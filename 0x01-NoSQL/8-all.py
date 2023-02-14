#!/usr/bin/env python3
"""Task 8 module """


def list_all(mongo_collection):
    """ Lists all documents in a collection """
    if not mongo_collection:
        return []
    return mongo_collection.find()