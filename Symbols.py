class Symbol:
    def __init__(self, symbol_type, content):
        self.symbol_type = symbol_type
        self.content = content

    def __eq__(self, other):
        if not isinstance(other, Symbol):
            return False

        return self.content == other.content and self.type == other.type

    def __str__(self):
        return "Symbol(" + str(self.type) + ", '" + self.content + "')"

def get_symbol_type_name(type):
    if type == 0:
        return "EOL"
    if type == 1:
        return "Bicondition"
    if type == 2:
        return "Implication"
    if type == 3:
        return "Not"
    if type == 4:
        return "Or"
    if type == 5:
        return "And"
    if type == 6:
        return "Opening bracket"
    if type == 7:
        return "Closing bracket"
    if type == 8:
        return "True"
    if type == 9:
        return "False"
    if type == 10:
        return "Identifier"

class ESymbol(Symbol):
    def __init__(self):
        super().__init__(0, "")
class OSymbol(Symbol):
    def __init__(self):
        super().__init__(4, "\\/")

class BSymbol(Symbol):
    def __init__(self):
        super().__init__(1, "<=>")

class ImSymbol(Symbol):
    def __init__(self):
        super().__init__(2, "=>")

class LSymbol(Symbol):
    def __init__(self):
        super().__init__(6, "(")

class RSymbol(Symbol):
    def __init__(self):
        super().__init__(7, ")")

class TSymbol(Symbol):
    def __init__(self):
        super().__init__(8, "TRUE")

class FSymbol(Symbol):
    def __init__(self):
        super().__init__(9, "FALSE")

class IDSymbol(Symbol):
    def __init__(self, name):
        super().__init__(10, name)

class NSymbol(Symbol):
    def __init__(self):
        super().__init__(3, "~")

class ASymbol(Symbol):
    def __init__(self):
        super().__init__(5, "&")

