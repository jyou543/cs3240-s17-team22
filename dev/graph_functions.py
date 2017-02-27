# Ryan Donovan (rad9vy)
# graph_functions

from graph import Graph

def is_complete(grph):
    if isinstance(grph,Graph):
        if grph.num_nodes() <=1:
            return True
        else:
            for n in grph.dict:
                for k in grph.dict:
                    if (not grph.dict[n].__contains__(k)) and n != k:
                        return False
        return True
    else:
        raise TypeError("Parameter is of the wrong type")

def nodes_by_degree(grph):
    if isinstance(grph, Graph):
        tups = []
        for n in grph.dict:
            degree = len(grph.dict[n])
            tups.append([n, degree])
        tups = sorted(tups, key = lambda x:x[1])
        tups.reverse()
        return tups
    else:
        raise TypeError("Parameter is of the wrong type")
