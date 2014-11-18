Applied Data Project
====================

We're going to use MapReduce to do PageRank on your Facebook followers

Getting Your Facebook Information
---------------------------------

We're going to use the tool Netvizz, which will allow you to export your friend list and the links between them as text files.

First, go to the Netvizz app



<write the walkthrough of netvizz here>

Download the gdf file.

What do Netvizz files look like?
--------------------------------

The first lines contain the "nodes", or the points in the graph.  Each row is one of your friends:

```
nodedef>name VARCHAR,label VARCHAR,sex VARCHAR,locale VARCHAR,agerank INT
409895,Shannon Patel,male,en_US,290
501090,Gwen Rudie,female,en_US,289
1109591,Denis Erkal,male,en_US,288
1909298,Rebecca Devens,,en_US,287
1936250,Jack Crowe,male,en_US,286
...
```

Then half way down the file, there is a line starting ``edgedef>`` and then the links between your friends

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
