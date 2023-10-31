import random

def main():
    combinations = [
        ("single", "past"),
        ("single", "present"),
        ("single", "future"),
        ("plural", "past"),
        ("plural", "present"),
        ("plural", "future"),
    ]

    for _ in range(6): 
        quantity, tense = random.choice(combinations)
        sentence = make_sentence(quantity, tense)
        print(sentence.capitalize())

def make_sentence(quantity, tense):
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    return f"{word} {noun} {verb} {prepositional_phrase}"

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == "single":
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == "single":
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity == "plural":
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    verb = random.choice(verbs)
    return verb

def get_preposition():
    prepositions = [
        "about", "above", "across", "after", "along", "around",
        "at", "before", "behind", "below", "beyond", "by", 
        "despite", "except", "for", "from", "in", "into", 
        "near", "of", "off", "on", "onto", "out", "over", 
        "past", "to", "under", "with", "without"
    ]
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {word} {noun}"

main()
