# Applied Data Project

The code in this repo takes your Facebook network and uses the MapReduce framework to calculate the PageRank of your friends.  This code was written for a lesson on Big Data at the Startup Institute. The document is structured as follows:

   1. Getting your Facebook friend network data
   2. Parsing the raw information into a clean form
   3. Using MapReduce to calculate the [PageRank](http://en.wikipedia.org/wiki/PageRank) of the friends in your network 

## 1. Getting Your Facebook Information

We're going to use the FB app [Netvizz](https://apps.facebook.com/netvizz/ "Netvizz"), which will allow you to export your friend list and the links between your friends as text files.

First, go to the Netvizz app, authorize it to access your data and get a screen like this:

![Alt text](/images/netvizz1.png)

Select "Personal Network".  this will download you a list of all of your friends along with a list of all the links between your friends.  After selecting "Personal Network" you get the option to download your friends Likes.  Feel free to do so, but it is not necessary for this project, so leave the box unchecked and hit "start"

![Alt text](/images/netvizz2.png)

When you get a choice of files to download, choose the "gdf" file.  The "tab" file does not contain all of the information that we need.

### What do Netvizz files look like?

The ``gdf`` file contains two distinct CSV tables, concatenated together.

The first table contains the "nodes", or the points in the graph.  Each row is one of your friends, and the first line starts with a header ``nodedef>``:

```
nodedef>name VARCHAR,label VARCHAR,sex VARCHAR,locale VARCHAR,agerank INT
409895,Shannon Patel,male,en_US,290
501090,Gwen Rudie,female,en_US,289
1109591,Denis Erkal,male,en_US,288
1909298,Rebecca Devens,,en_US,287
1936250,Jack Crowe,male,en_US,286
...
```

The rows in this part of the file contain values separated by commas:  A unique ID for a person, their name, their sec, their language, and a ranking.  Following this table, there is a line starting ``edgedef>`` and the lines that follow that describe links between your friends

```
edgedef>node1 VARCHAR,node2 VARCHAR
409895,2524813
409895,10132088
409895,61011914
501090,10132088
1109591,2908604
1109591,13301711
...
```

## 2. Preparing the gdf file for use

In this repo there is a source file, ``read_gdf.py`` that takes one of these gdf files and reformats it into some JSON

```
python read_gdf.py my_filename.gdf > my_filename.json
```

The output of this script is a JSON file, each of the top-level keys is the name of one of your friends and the associated values are the lists of friends you share with them:

```
{
  "Andreas Pawlik": [
    "Ben Oppenheimer",
    "Malin Welander",
    ...
    ],
  "Thomas Randall": [
    "Phil Marsden",
    "Richard Tymon",
    "Nathan Butler",
    ...
  ],
  ...
}
```

This file is the input to the MapReduce script.

## 3. Analyzing The Links Between Your Friends

### Installing the scripts

No special installation is needed, as long as you have Python on your machine (you probably do), just clone this repo

### Running the scripts

For testing purposes, there are libraries that allow you to build out ``map`` and ``reduce`` functions on your own machine, and test them in parallel.  We will use ``mincemeat.py``.  To do the mapreduce, you need to run a server (which takes care of the things that MapReduce does, shuttling around data and doing the shuffle) and a client, which runs the map and reduce.

Open up one terminal, change into the directory where the code is installed and run a server:

```
python pagerank.py server --filename=<whatever_my_filename_is>
```

Then in another terminal, run a client

```
python pagerank.py client
```

The server will start printing out some diagnostic information:

```
Server completed run :  0 total PR :  155.1
Server completed run :  1 total PR :  167.79
Server completed run :  2 total PR :  179.211
Server completed run :  3 total PR :  189.4899
Server completed run :  4 total PR :  198.74091
```

The total PageRank will gradually trend towards the number of nodes in your network, when it is pretty much converged the results are accurate.  When the code is finished, it will print out the PageRanks of all of your friends.

