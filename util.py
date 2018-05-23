from copy import deepcopy
class Marker:
    def mark_symbol_node(self, node):
        pass

    def mark_operator_node(self, node):
        pass

class Extractor(Marker):
    def __init__(self):
        self.terms = set()

    def extract_terms_from_kb(self, root_node):
        self.terms = set()
        root_node.traverse(self)
        return self.terms

    def mark_symbol_node(self, node):
        self.terms.add(node.name)

class Model(Marker):
    def __init__(self):
        self.res = {}
        self.table = {}

    def mark_symbol_node(self, node):
        self.res[node] = self.table[node.name]

    def mark_operator_node(self, node):
        # get first value by hash
        first_term = self.res[node.child_nodes[0]]
        if first_term == None:
            self.res[node] = None
        # not term
        elif node.type == 3:
            self.res[node] = not self.res[node.child_nodes[0]]
        else:
            # get second value via hash
            second_term = self.res[node.child_nodes[1]]
            if second_term == None:
                self.res[node] = None
            # bicondition
            elif node.type == 1: 
                self.res[node] =  ((not first_term) or second_term) and ((not second_term) or first_term)
            # implication
            elif node.type == 2:
                self.res[node] =  (not first_term) or second_term
            # or term
            elif node.type == 4:
                self.res[node] = first_term or second_term
            # and term
            elif node.type == 5:
                self.res[node] = first_term and second_term


    def explode(self, index, ind_val):
        model_to_return = Model()
        model_to_return.table = deepcopy(self.table)
        model_to_return.table[index] = ind_val
        return model_to_return

    def ask_true(self, root_node):
        self.res = {}
        root_node.traverse(self)
        return self.res[root_node] == True