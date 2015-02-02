# Hack Night Lightning Talk: Intro to Databases w/ Mongo

A quick write-up that follows the content covered in HackNight Mongo ligthning talk


###What the heck is a database? 

Databases are structured sets of information that offer ways to extract and query its content
Some examples of things that use a database:  Course Sniper, Rutgers Student Database, 


###Why do I care?

1. Knowing how to use and make databases for your own purposes expands the possible kinds of applications you can develop.

2. With databases, you can have persistent information even after your program stops running.

3. Knowing how to use a database will make you look cool and everyone will want to be your friend.


###Whats this mongo everyone keeps talking about?

Mongo is an open source, schemaless database system thats great for beginner database-driven projects. It lets you quickly leverage
the advantages of having a database without requiring you to have a strong background in database fundamentals or a set list of
attributes for the things you're storing. In addition to its beginner-friendliness, mongo features some really nice
easy-to-use libraries for a bunch of different programming languages (for this talk, we'll be using pymongo for python)

###Some quick terminology 

mongo shell - an interactive shell for using MongoDB. Here you can view your databases and collections, as well as make queiries. 

document - a data object with different attributes. A document always has an id field

```bash
    {"name": "Tim", "occupation": "enchanter", "salary": 600}

```

collection - a group of documents, or whats known as a table in the world of sql

database - a group of collections, basically the same thing as its sql counterpart


###Messing around in the mongo shell

A good way to get yourself familiar with mongo is to open up the mongo shell and start breaking things
To begin playing with the mongo shell, follow the instructions in the mongo docs [here](http://docs.mongodb.org/v2.2/tutorial/getting-started-with-the-mongo-shell/)
or if you want to experiment in your browser, check out this [link](http://try.mongodb.org/)

Definitely check out the [mongo shell quick reference](http://docs.mongodb.org/v2.2/reference/mongo-shell/) to help you out

Some basic goals to go for as you're getting familiar

1. Make a database
2. Make a collection
3. Insert a document into the collection. You can use the sample document above as an example
4. Display everything stored in your collection


###A quick, simple example using pymongo

You can check out app.py in the repo for a glimpse on what it looks like to interface with mongo through the use of pymongo.
While definitely not everything you'll ever need to know about mongo or pymongo, the code serves as a decent jumping-off point
for things like using a specific database and collection, as well as basic inserting and querying data

###What do I do now?

Now that you've seen some basic ways to use mongo, its time to try it for yourself. 

Go [here](http://docs.mongodb.org/manual/installation/) if you need mongo installed. We'll be around to help with the process.

If you haven't already done 'Messing around in the mongo shell' above, check that out.

If you're ready to start playing with pymongo, you can start by applying what you've done in the mongo shell and try inserting and deleting documents
within a python program.
