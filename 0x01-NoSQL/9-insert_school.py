#!/usr/bin/env python3
""" function that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """insert new doc based on kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
    
