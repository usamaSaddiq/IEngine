from KnowledgeBase import *
from Parser import *
from Node import *
from util import *

default = None
trail = []
class FC:
    def __init__(self):
        self.sum = {}
        self.infered = {}
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

    def get_chain(self, kb, question):
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

kb = KnowledgeBase()
kb.feed_sentence("p2=> p3")
kb.feed_sentence("p3=> p1")
kb.feed_sentence("c => e")
kb.feed_sentence("p1=>d")
kb.feed_sentence("(b&e) => f")
kb.feed_sentence("(f&g) => h")
kb.feed_sentence("(p1&p3) => c")
kb.feed_sentence("p2")
kb.feed_sentence("b")
kb.feed_sentence("a")

# kb.feed_sentence("(a <=> (c => ~d)) & b & (b => a)")
# kb.feed_sentence("f & g")
# kb.feed_sentence("c")

# kb.feed_sentence("p1&p2&p3 => p4")
# kb.feed_sentence("p5&p6 => p4")
# kb.feed_sentence("p1 => p2")
# kb.feed_sentence("p1&p2 => p3")
# kb.feed_sentence("p5&p7 => p6")
# kb.feed_sentence("p1")
# kb.feed_sentence("p4")
question_sentence = Parser().process("d")

fc = FC()
result,trace = fc.get_chain(kb, question_sentence)

if result == True:
    print("Yes: ", end="")    
    for t in trace:
        print(t.name + " ", end="")
else:
    print("No")