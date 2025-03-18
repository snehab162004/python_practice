def scan(sentence):
    lexicon = {
        'north': 'direction', 'south': 'direction', 'east': 'direction',
        'go': 'verb', 'kill': 'verb', 'eat': 'verb',
        'bear': 'noun', 'princess': 'noun',
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

print(scan("go north"))
print(scan("kill the bear"))
print(scan("eat 5 apples"))
