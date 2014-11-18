Applied Data Project
====================

We're going to use MapReduce to do PageRank on your Facebook followers

Getting Your Facebook Information
---------------------------------

We're going to use the tool [Netvizz](https://apps.facebook.com/netvizz/ "Netvizz"), which will allow you to export your friend list and the links between your friends as text files.

First, go to the Netvizz app, authorize it to access your data and get a screen like this:

![Alt text](/images/netvizz1.png)

Select "Personal Network".  this will download you a list of all of your friends along with a list of all the links between your friends.  After selecting "Personal Network" you get the option to download your friends Likes.  Feel free to do so, but it is not necessary for this project, so leave the box unchecked and hit "start"

![Alt text](/images/netvizz2.png)

When you get a choice of files to download, choose the "gdf" file.  The "tab" file does not contain all of the information that we need.

What do Netvizz files look like?
--------------------------------

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

Preparing the Netvizz file for use
----------------------------------

In this repo 
