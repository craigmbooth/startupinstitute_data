from collections import defaultdict
import argparse
import json

def read_gdf(filename):
    """Reads a gdf file that was given to us by netvizz and parses it into
    a dictionary where there is one key for each of your friends and the
    value associated with that key is a list of your friends who they are
    friends with.

    Note that we rely on the convention that there is a line starting with
    ``nodedef>`` that marks the start of the nodes lines, and another starting
    with ``edgedef>`` that marks the start of the edges."""

    # Read the file into a list, one line per element:
    with open(filename, "r") as f:
        lines = f.readlines()

    nodes = False
    edges = False

    friends = {}
    friend_links = defaultdict(list)

    nodes = True
    for line in lines:
        if line.startswith("nodedef"):
            continue   #Do not parse this line, it is a header
        elif line.startswith("edgedef"):
            nodes = False
            continue   #Do not parse this line, it is a header

        if nodes:
            # If we're on the nodes, each line has this form:
            # ID, Name, sex, lang, rank.
            # Build a dictionary mapping ID to name
            line_parts = line.split(",")
            friends[line_parts[0]] = line_parts[1]
        else:
            # If we're on the edges, each line just contains two IDs, noting
            # that these two friends are friends with one another.  We need
            # to put this in the output structure twice because FB friendship
            # is a two-way connection
            line_parts = line.replace("\n", "").split(",")
            friend_links[str(friends[line_parts[0]])].append(
                str(friends[line_parts[1]]))
            friend_links[str(friends[line_parts[1]])].append(
                str(friends[line_parts[0]]))
    return friend_links

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str,
                        help="Filename of gdf file to parse")
    args = parser.parse_args()
    parsed_file = read_gdf(args.filename)

    print json.dumps(parsed_file, indent=2)
