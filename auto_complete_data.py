
#@dataclass
class AutoCompleteDataClass:

    def __init__(self, completed_sentence, source_text, source_line, offset, score):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.source_line = source_line
        self.offset = offset
        self.score = score
    # methods that you need to define by yourself
