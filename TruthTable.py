from KnowledgeBase import *
from Parser import *
from util import *
import copy
counter = 0
extractor = Extractor()
p = Parser()
initial_model = Model()
def entails(kb, alpha):
    # construct a tree with and delimator
    nodes = kb.clauses
    # guard against no nodes found
    if nodes:
        no_of_nodes = len(nodes)
        if no_of_nodes == 0:
            return None
        elif no_of_nodes == 1:
            return nodes[0]
        elif no_of_nodes >= 2:
            # take and for the last two nodes
            knowledge_base = ANode(nodes[no_of_nodes - 2], nodes[no_of_nodes - 1])
            count = list(range(no_of_nodes - 2))
            count.reverse()

            if len(count) > 1:
                for c in count:
                    knowledge_base = ANode(nodes[c], knowledge_base)
        
    query = p.process(alpha)
    k_s = extractor.extract_terms_from_kb(knowledge_base)
    q_s = extractor.extract_terms_from_kb(query)
    all_symbols = list(k_s.union(q_s))

    return check_all_models(knowledge_base, query, all_symbols, initial_model)

def check_all_models(kb_sentence, query_sentence, symbols_list, model):
    global counter
    symbols_count  = len(symbols_list)
    if symbols_count != 0:
        to_pass = copy.deepcopy(symbols_list)
        extend_symbol = to_pass.pop()
        return check_all_models(kb_sentence, query_sentence, to_pass, model.explode(extend_symbol, True)) and \
                check_all_models(kb_sentence, query_sentence, to_pass, model.explode(extend_symbol, False))
    else:
        if model.ask_true(kb_sentence):
            counter += 1
            return model.ask_true(query_sentence)
        return True

def handle(kb,question):
    
    flag = entails(kb,question)
    if flag:
        print("Yes: {0}".format(counter))
    else:
        print("No")