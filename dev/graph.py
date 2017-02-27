# Ryan Donovan (rad9vy)
# graph.py

class Graph:
# ******* Constructor with parameter *******

    def __init__(self, dict):
        self.dict = dict
    #TODO what if no dict provided?

# ******* Get adjacency list of a specified node *******

    def get_adjlist(self, node):
        if node in self.dict:
            return self.dict[node]
        else:
            return None

# ******* is adjacent *******

    def is_adjacent(self, node1, node2):
        if node1 in self.dict and node2 in self.dict:
            if node2 in self.dict[node1]:
                return True
        return False

# ******* Number of Nodes *******

    def num_nodes(self):
        count = 0;
        for k in self.dict.keys():
            count+=1;
        return count;

## ******* str *******

    def __str__(self):
        str1 = str(self.dict)
        print(str1)

# ******* iter *******

    def __iter__(self):
        for i in self.dict.keys():
            yield i;

 # ******* contains *******

    def __contains__(self, node):
        if node in self.dict:
            return True
        return False

# ******* len *******

    def __len__(self):
        count = 0;
        for k in self.dict.keys():
            count += 1;
        return count;

# ******* add node *******

    def add_node(self, node):
        if node in self.dict:
            return False
        else:
            self.dict[node] = []
            return True

# ******* link nodes *******

    def link_nodes(self, node1, node2):
        if node1 == node2:
            return False
        if node1 in self.dict and node2 in self.dict:
            # if they're already adjacent
            if node2 in self.dict[node1] or node1 in self.dict[node2]:
                return False
            else:
                self.dict[node1].append(node2)
                self.dict[node2].append(node1)
                return True
        return False

# ******* unlink nodes *******

    def unlink_nodes(self, node1, node2):
        if node1 == node2:
            return False
        if node1 in self.dict and node2 in self.dict:
            if node2 in self.dict[node1] or node1 in self.dict[node2]:
                self.dict[node1].remove(node2)
                self.dict[node2].remove(node1)
                return True
            else:
                return False
        return False

# ******* delete node *******

    def del_node(self, node):
        if node in self.dict:
            self.dict.pop(node)
            for k in self.dict:
                if node in self.dict[k]:
                    self.dict[k].remove(node)
            return True
        else:
            return False


