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