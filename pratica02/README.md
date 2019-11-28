# README
This document will serve as my notes for the following lab class. Anything worth mentioning will be said here, and this has been made for future studying or revision sessions

## Set up MongoDB
[Installing MongoDB](https://hevodata.com/blog/install-mongodb-on-ubuntu/)
After installing, start it by using the command 

>$ sudo systemctl enable mongod 	
>$ sudo systemctl start mongod 	
>$ mongo

The first command will automatically start mongo db throughout reboots.
The second will start the mongo server for this session.
The keyword mongo will connect the terminal to the server.

## Experimenting with MongoDB
#### MongoDB commands
The MongoDB commands native commands are pretty straightforward:
> show dbs shows all your databases
> use db changes your database to db
> db.dropDatabase will drop the current database
> db.insert will insert into the database

Interestingly enough, use db will create a new database if it doesn't recognize the name, but that db won't immediately show up on the showdb command, since as it was just created it has no information yet, and showdb will only show databases with actual documents and information.
Consequently, if you try to drop your current database, while having just created it, it will send an exception as the current database hasn't been recognized yet.

As for queries, syntax is a bit awkward at the beginning, with some weird nuances to it, mostly on the find and remove functions.
For instance, a simple *and* query turns into a mouthful a the likes of:

> db.collecation.find( {
> 	      $and: [
> 	        	 {key1: value1}, {key2:value2}
> 	      ]  })

All around a bit unfriendly to me as a beginner at mongodb.

The pre built functions however are pretty straight forward, things like counting and sorting are made very easy.
For instance, if I wanted to get the top *something* in a collection within the db, I would simply have to do:
> db.collection.find().sort(*something*:1).limit(1)

## 2.2 Queries with MongoDB
### Introduction
The first command to use is to actually build the database we're going to work with
``mongoimport --db cbd --collection rest --drop --file <path/>restaurants.json``
It's a pretty big command, that seems to do a lot of things automatically:
	Starting with the import, this will clearly import something to the server, not much needs to be said here
	Then we do --db cbd, which will create the database cbd, which we'll use to work on our queries
	Followed by the --collection rest: in the cbd database we'll be creating a collection rest;
	The --drop command seems to drop the database in case there is one, this allows the user to use this command multiple times without having to deal with the duplicate database error
	Finally the --file path/restaurants.json will tell mongo which file to import to the database

### Queries
Find is actually a pretty interesting function, the first arguments are the conditions to which the documents have to appear, while the second argument is the attributes I want to appear.
Also, found a caveat to this, as the _id will appear if I don't tell it to explicitly disappear.
Search a field within a field is done simply by:
	``field1.field2``
Searching a field within an array is done automatically so that if *at least one* follows the condition, the whole document passes.
To check if a certain field is either smth_1 or smth_2, you just need to use the *$in* operator, using an array composed of [smth_1, smth_2]
Regular expressions seems to have a different syntax from what I was accustomed with: further study should be done to memorize how to use it.
To check if **all** elements of an array go through a certain condition, it's better to check if any element **doesn't** go through the condition, usando o $not $elemMatch. MongoDB doesn't seem to have a simple function for **all**.
Sort method sorts by ascending order if key:1, descending if key:-1
Notes on query #21:
	First it was needed to reach the scores, inside the grades object: we needed to $unwind the grades object;
	After that we made a new group, with id:name and avg_score the average of scares;
	Finally we found the wanted restaurants using the $match

## Notes on Functions
### Introduction
We start by having to simply to get a pre-made function done by the Teacher (populatePhones.js) by using the mongo command:
``load("<pasta da sua área de trabalho>/populatePhones.js") ``

### Analizing the Populate Phone Function
```
> populatePhones
function (country, start, stop) {

  var prefixes = [21, 22, 231, 232, 233, 234 ];
  for (var i = start; i <= stop; i++) {

    var prefix = prefixes[(Math.random() * 6) << 0]
    var countryNumber = (prefix * Math.pow(10, 9 - prefix.toString().length)) + i;
    var num = (country * 1e9) + countryNumber;
    var fullNumber = "+" + country + "-" + countryNumber;

    db.phones.insert({
      _id: num,
      components: {
        country: country,
        prefix: prefix,
        number: i
      },
      display: fullNumber
    });
    print("Inserted number " + fullNumber);
  }
  print("Done!");
}
```
So first thing to note is the way the declare the type of variable to be used, using a simple var, followed by the actual name of the variable.	

## Notes on PyMongo
It was pretty straightforward, the functions and interactions with a pymongo aren't much different from the regular Mongo.
To use pymongo and pick the database and collection, these lines need to be included
```
from pymongo include *
cli = MongoClient()
database = cli["cbd"]
collection = database["rest"]
```
After this, any mongo function is carried out as normal

## Free Theme Database
For the last exercise, we were free to choose a database with a theme of our choosing, and carry out a lot of different queries to further get to know the MongoDB module
From this public [git](https://github.com/ozlerhakan/mongodb-json-files/tree/master/datasets), I was able to have a bunch of different datasets to choose from to work with my queries. That said, I decided to use the document grades.json.
I decided as a personal preference to use mongo scripts to build my queries, instead of an API.
The queries are in the document CBD_L205_89156.md
> Written with [StackEdit](https://stackedit.io/).



