from Tokenizer import Tokenizer
from Symbols import *

class Analyzer(Tokenizer):
    def __init__(self, input):
        super().__init__(input)
        self.data = {"~" : NSymbol, "&" : ASymbol, "\\/" : OSymbol, "TRUE" : TSymbol, "FALSE" : FSymbol}

    def get_next_char_to_analyse(self):
        # jump the spaces and get to the next charachter
        self.jump_spaces()
        char = self.next_char()
        # check for or operator
        if char == '~':
            return NSymbol()
        if char == '\\':
            self.predict('/')
            return OSymbol()
        # check for and operator            
        if char == '&':
            return ASymbol()
        # check for opening paranthesis operator
        if char == '(':
            return LSymbol()
        # check for closing paranthesis
        if char == ')':
            return RSymbol()
        # check for bicondition
        if char == '<':
            self.predict('=')
            self.predict('>')
            return BSymbol()
        # check for implication
        if char == '=':
            self.predict('>')
            return ImSymbol()
        # check for end of line
        if char == None:
            return ESymbol()
        # charchter is a symbol
        if char.isalpha():
            self.decrement_position()
            return self.get_identifier()
        
        raise Exception("Unexpected symbol " + char)

    def get_identifier(self):
        content = self.next_char()
        for iterator in range(100):
            char = self.next_char()
            if char != None and char.isalnum():
                content += char
            else:
                if char != None:
                    self.decrement_position()
                break
        
        unknown_identifier = self.data.get(content)
        if not unknown_identifier:
            return IDSymbol(content)  
        return unknown_identifier()

