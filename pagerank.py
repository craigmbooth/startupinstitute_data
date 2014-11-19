import mincemeat
import argparse
from time import sleep
import json
from data_munging import convert, munge_data

NUMBER_ITERATIONS = 100

def mapfn(k, v):
    """Map function for MapReduce.  See the slides for a description of
    what we're doing here"""
    pass


def reducefn(k, vs):
    """Reduce function for MapReduce.  See the slides for a description of
    what we're doing here"""
    pass


if __name__ == "__main__":

    # Use argparse to collect command line arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=str, choices=["server", "client"],
                        help="Should I be the server or a client")
    parser.add_argument("--filename", type=str, required=False,
                        help="Filename with friend lists")
    args = parser.parse_args()

    if args.target == "server":
        if args.filename is None:
            raise ValueError("If you are the server, need to set filename")

        with open(args.filename, "r") as f:
            data_source = convert(json.load(f))

        s = mincemeat.Server()
        s.datasource = munge_data(data_source, 0.5)

        # Set the map and reduce functions
        s.mapfn = mapfn
        s.reducefn = reducefn

        for i in range(NUMBER_ITERATIONS):
            results = s.run_server(password="changeme")

            total_pr = sum([x[0][1] for x in results.values()])
            print "Server completed run : ", i, "total PR : ", total_pr

            new_results = {}
            for _, v in results.iteritems():
                new_results[v[0]] = v[1:][0]
            s.datasource = new_results

        print sorted(new_results.keys(), key=lambda x: x[1])

    elif args.target == "client":
        for i in range(NUMBER_ITERATIONS):
            client = mincemeat.Client()
            client.password = "changeme"
            client.conn("localhost", mincemeat.DEFAULT_PORT)
            sleep(0.1)
