#!/usr/bin/env python3
"""Task 11 module"""


def schools_by_topic(mongo_collection, topic):
    """
    A Python function that returns the list of school having a specific topic:
    """
    query = { "topic": { "$in": [topic] } }
    return mongo_collection.find(query)