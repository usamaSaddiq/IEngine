from Parser import *
from Node import *

class KnowledgeBase:
    """
    Knowledge base that stores information in propositional logic
    """
    def __init__(self):
        self.clauses = []
        self.parser = Parser()

    def feed_sentence(self, data):
        sentence = self.parser.process(data)
        self.clauses.append(sentence)

    def read_and_feed(self, data):
        for d in data:
            self.feed_sentence(d)


kb = KnowledgeBase()
# kb.feed_sentence("p2=> p3")
# kb.feed_sentence("p1=>d")
# kb.feed_sentence("c => e")
# kb.feed_sentence("b&e => f")
# kb.feed_sentence("f&g => h")
# kb.feed_sentence("p1&p3 => c")
# kb.feed_sentence("a")
# kb.feed_sentence("b")
# kb.feed_sentence("p2")
# p5&p6 => p4; p1 => p2; p1&p2 => p3; p5&p7 => p6; p1; p4;
# (a <=> (c => ~d)) & b & (b => a); c; ~f \/ g;
kb.feed_sentence("(a <=> (c => ~d)) & b & (b => a)")
kb.feed_sentence("f & g")
kb.feed_sentence("c")
# kb.feed_sentence("p1&p2&p3 => p4")
# kb.feed_sentence("p5&p6 => p4")
# kb.feed_sentence("p1 => p2")
# kb.feed_sentence("p1&p2 => p3")
# kb.feed_sentence("p5&p7 => p6")
# kb.feed_sentence("p1")
# kb.feed_sentence("p4")
print("ok")
