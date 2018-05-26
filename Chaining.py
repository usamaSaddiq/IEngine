from KnowledgeBase import *
from Parser import *
from Node import *
from util import *

default = None
trail = []

class Chaining:
    def __init__(self):
        self.sum = {}
        self.infered = {}
        self.agenda = []
        self.facts = []
    class HC:
        def __init__(self, knowledge_base):
            self.rhs = default
            self.lhs = self.rhs
            self.validate_terms(knowledge_base)

        def validate_terms(self,kb):
            if kb.type == 10:
                self.rhs = kb
                self.lhs = []
            elif kb.type != 2 and kb.type != 5:
                raise Exception("Knowledge base has an illegal horn clause. \n Exiting with code 1")
            else:
                self.rhs = kb.child_nodes[1]
                extractor = Extractor()
                all_symbols = extractor.extract_terms_from_kb(kb.child_nodes[0])
                self.lhs = []
                while len(all_symbols) > 0:
                    self.lhs.append(IdNode(all_symbols.pop()))

        def __eq__(self, other):
            return isinstance(other, HC)
            if self.head != other.head:
                return False
            if len(self.lhs) != len(other.lhs):
                return False
            for i in range(len(self.lhs)):
                if self.lhs[i] != other.lhs[i]:
                    return False
            return True

    def get_bchain(self,kb,question):
        question = Parser().process(question)        
        terms = []
        for clause in kb.clauses:
            terms.append(self.HC(clause))

        for term in terms:
            if len(term.lhs) == 0:
                self.facts.append(term.rhs)

        self.agenda.append(question)
        to_process = []
        while(len(self.agenda) > 0):
            p = self.agenda.pop()
            trail.insert(0,p)            
            if not p in self.facts:
                for term in terms:
                    if p == term.rhs:
                        for t in term.lhs:
                            to_process.append(t)
                if len(to_process) == 0:
                    return False,trail
                else:
                    for node in to_process:
                        if not node in trail:
                            self.agenda.append(node)

        return True,trail
            
    def get_fchain(self, kb, question):
        question = Parser().process(question)
        terms = []
        for clause in kb.clauses:
            terms.append(self.HC(clause))

        for term in terms:
            self.infered[term.rhs] = False
            if len(term.lhs) == 0:
                self.sum[term.rhs] = 0
                self.facts.append(term.rhs)
            for symbol in term.lhs:
                self.infered[symbol] = False
            self.sum[term.rhs] = len(term.lhs)

        while len(self.facts) > 0:
            p = self.facts.pop()
            trail.append(p)            
            if not self.infered[p]:
                self.infered[p] = True
                for term in terms:
                    if p in term.lhs:
                        self.sum[term.rhs] -= 1
                        if self.sum[term.rhs] == 0:
                            if term.rhs == question:
                                trail.append(question)
                                return True,trail
                            self.facts.append(term.rhs)
        return False,trail