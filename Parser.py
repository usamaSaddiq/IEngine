from Symbols import *
from Node import *
from Analyzer import Analyzer

class Parser():
    def __init__(self):
        self.operators = {1 : BNode, 2 : ImNode , 4 : ONode, 5 : ANode}

    def process(self, str):
        self.analyzer = Analyzer(str)
        return self.process_sentence()

    # refactoring apply
    def process_sentence(self):
        symbol = self.analyzer.get_next_char_to_analyse()
        sentence = None

        # check for a false node
        if symbol.symbol_type == 9:
            sentence = FalseNode()
        # check fot he true node
        elif symbol.symbol_type == 8:
            sentence = TrueNode()
        # check for an variable
        elif symbol.symbol_type == 10:
            sentence = IdNode(symbol.content)
            # check for not term
        elif symbol.symbol_type == 3:
            sentence = self.process_sentence()
            return NtNode(sentence)

        # check for opening bracket        
        elif symbol.symbol_type == 6:
            sentence = self.process_sentence()
            # check fo closing not a bracket otherwise return exception
            expected_symbol = self.analyzer.get_next_char_to_analyse()
            if expected_symbol.symbol_type != 7:
                raise Exception("Unexpected Symbol type")
        else:
            raise Exception("Unexpected Node")
        self.analyzer.populate_marked_index()
        symbol = self.analyzer.get_next_char_to_analyse()

        # check for the next symbol to be an operator to concatenate
        if symbol.symbol_type in {1, 2, 4, 5}:
            sentence2 = self.process_sentence()
            node = self.operators[symbol.symbol_type]
            return node(sentence, sentence2)
        else:
            self.analyzer.change_to_mark()
            return sentence

