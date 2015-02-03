#!/usr/bin/python

from flask import json, jsonify
from pymongo import MongoClient # the library we'll be using to do mongo things
from key import api_key
import requests


client = MongoClient()          # method that establishes the connection to the mongo client

db = client['yo']               # use the 'yo' database'. If none exists, pymongo will make a new one named yo

hackathons = db['hackathons']   # gets the hackathons collection from the yo database. This is what we'll use
                                # to insert and retrieve documents

def yo_all(token):
    requests.post("http://api.justyo.co/yoall/", 
                  data={'api_token': token})

def update_events():
    r = requests.get(
        "http://hackerleague.org/api/v1/hackathons.json")
    for event in r.json():
        if event.get('location').get('state') == "New York":    # is the event in new york?

            update_collection(event)                            # if so, call update

def update_collection(event):
    entry = hackathons.find_one({"name": event['name']})        # we query the mongo collection to see if our event is already saved

    if entry is None:                                           # if the event is not in the database, then add it and yo everyone

        hackathons.insert({"name" : event['name']})             # add the event to the collection
        yo_all(api_key)

update_events()
