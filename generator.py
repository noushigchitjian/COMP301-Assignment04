"""
Program: generator.py
Generates and displays sentences using simple grammar
and vocabulary. Words are chosen at random.
"""

import random
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL","AIRPORT","BEACH","CAR","DOCTOR","EVENING","FAMILY")
verbs = ("AGREE", "BORROW", "CALL","DANCE","ENJOY","FLY","GIVE","HELP","IDENTIFY","KEEP")
prepositions = ("ABOUT", "BEFORE","CONSIDERING","DURING","EXCEPT","FOR","IN","LIKE","OPPOSITE","PLUS")
conjunctions = ("FOR","AND","NOR","BUT","OR","YET","SO")
adjectives = ("ALIVE","BEAUTIFUL","CLEVER","DELICIOUS","EARLY","FANCY","GENTLE","HAPPY","IMPORTANT","KIND")


def getWords(fileName):
    
    openWords = open(fileName, "r")
    
    tempList = []
    
    readWords = openWords.read()
     
    word = readWords.split()
    
    tempList = [word]
    
    words = tuple(tempList) 
    
    return words

def sentence():
    
    OIClause = ""
    IClauseChance = random.randrange(100) +1
    if(IClauseChance >50) :
        OIClause = random.choice(conjunctions)+ " "+ nounPhrase() + " " + verbPhrase()    
    return nounPhrase() + " " + verbPhrase() + " " + OIClause

def nounPhrase():
    
    OAdjective = ""
    adjectiveChance = random.randrange(100) +1
    if(adjectiveChance > 50):
        OAdjective = random.choice(adjectives)    
    return random.choice(articles) + " " + OAdjective +" " + random.choice(nouns)

def verbPhrase():
    
    OPrepPhrase = ""
    prepPhraseChance = random.randrange(100) + 1
    if(prepPhraseChance > 50):
        OPrepPhrase =prepositionalPhrase()    
    return random.choice(verbs) + " " + nounPhrase() + " " + OPrepPhrase

def prepositionalPhrase():
    
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    noun = input("Please enter the file that has the nouns: ")
    verb = input("Plaese enter a file that has the verbs: ")    
    preposition = input("Please enter a file that has the prepositions: ")
    article = input("Please enter a file that has the articles: ")    
    adjective = input("Please enter a file that has the adjectives: ")
    noun = getWords(noun)
    verb = getWords(verb)
    preposition = getWords(preposition)
    article = getWords(article)    
    adjective = getWords(adjective)
    print(noun)
    print(verb)
    print(preposition)
    print(article)    
    print (adjective)

    
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())


if __name__ == "__main__":
    main()
