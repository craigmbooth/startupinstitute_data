def convert(input):
    """This function takes some sort of dictionary structure and changes unicode
    strings into plain bytestrings.  This is kinda horrible, but it's needed for
    mincemeat.py not to freak out.
    """

    if isinstance(input, dict):
        return {convert(key): convert(value) for
                key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def munge_data(data, initial_pr):
    """Our MapReduce code expects the keys and values to be of the form

    ``(user, pagerank): [list, of, friends]``

    So we need to attach an initial guess at the pagerank to each of our
    nodes."""
    return {(k, initial_pr): v for k, v in data.iteritems()}
