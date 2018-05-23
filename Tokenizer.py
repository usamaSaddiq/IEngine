class Tokenizer:
    def __init__(self, input):
        self.input = input
        self.current_position = 0
        self.marked_index = -1

    def decrement_position(self):
        if self.current_position != 0:
            self.current_position -= 1
    
    def populate_marked_index(self):
        self.marked_index = self.current_position

    def jump_spaces(self):
        for x in range(100):
            symbol = self.next_char()
            if symbol == None:
                break
            elif not symbol.isspace():
                self.decrement_position()
                break
    
    def change_to_mark(self):
        if self.marked_index == -1:
            raise Exception("Attempt to rollback with no mark")
        else:
            self.current_position = self.marked_index

    def next_char(self):
        try:
            symbol = self.input[self.current_position]
            self.current_position += 1
            return symbol
        except Exception as ie:
            return None

    def predict(self, expected):
        read = self.next_char()
        if read != expected:
            raise Exception("Expected the following charachter in telled clause '" + expected + "' got " + read + "\n Exiting with code 1")
