class Sentence:
    def __init__(self, subject, verb, obj):
        self.subject = subject
        self.verb = verb
        self.object = obj

    def __str__(self):
        return f"{self.subject} {self.verb} {self.object}"

def scan(sentence):
    lexicon = {
        'north': 'direction', 'south': 'direction', 'east': 'direction',
        'go': 'verb', 'kill': 'verb', 'eat': 'verb',
        'bear': 'noun', 'princess': 'noun', 'honey': 'noun',
        'the': 'stop', 'in': 'stop', 'of': 'stop'
    }

    words = sentence.split()
    result = []

    for word in words:
        if word in lexicon:
            result.append((lexicon[word], word))
        elif word.isdigit():
            result.append(('number', int(word)))
        else:
            result.append(('error', word))

    return result

def parse_sentence(word_list):
    if len(word_list) < 3:
        raise ValueError("Incomplete sentence!")

    subject = word_list[0][1]  
    verb = word_list[1][1]      
    obj = word_list[2][1]      

    return Sentence(subject, verb, obj)

words = scan("bear eat honey")
sentence = parse_sentence(words)
print(sentence)
