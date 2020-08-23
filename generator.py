"""
File name : generator.py
Author's name : NOUSHIG CHITJIAN
Student Number : 301117936
File description : Assignment4 / this wil generate and display sentences using simple grammar
and vocabulary. Words are chosen at random.
Program: COMP 301
Date : Aug.22,2020
"""

import random
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL","AIRPORT","BEACH","CAR","DOCTOR","EVENING","FAMILY")
verbs = ("AGREE", "BORROW", "CALL","DANCE","ENJOY","FLY","GIVE","HELP","IDENTIFY","KEEP")
prepositions = ("ABOUT", "BEFORE","CONSIDERING","DURING","EXCEPT","FOR","IN","LIKE","OPPOSITE","PLUS")
conjunctions = ("FOR","AND","NOR","BUT","OR","YET","SO")
adjectives = ("ALIVE","BEAUTIFUL","CLEVER","DELICIOUS","EARLY","FANCY","GENTLE","HAPPY","IMPORTANT","KIND")

"""this function Define a single new function getWords. This function should expect a filename as an argument."""
def getWords(fileName):
    """opens the file as a read mode and assigns it to the openWords"""
    openWords = open(fileName, "r")
    """The temporary list"""
    tempList = []
    """This will read the strings in the openWords and assigns them to the readWords"""
    readWords = openWords.read()
    """This will split the strings by " "  and assigns them to (word)""" 
    word = readWords.split()
    """This will put the (word) into the temporary list"""
    tempList = [word]
    """This will change the list to a >>>tuple<<< and assigns it to the words"""
    words = tuple(tempList) 
    """This will return the tuple"""
    return words

def sentence():
    """This will build and return a sentences with a independent clauses and conjunctions."""
    """This will put the independent clauses and the conjuctions by 50% of Chance after a independent sentece"""
    OIClause = ""
    IClauseChance = random.randrange(100) +1
    if(IClauseChance >50) :
        OIClause = random.choice(conjunctions)+ " "+ nounPhrase() + " " + verbPhrase()    
    return nounPhrase() + " " + verbPhrase() + " " + OIClause

def nounPhrase():
    """This will build and return a noun phrase with an adjective"""
    """This will put the adjective by 50 % of Chance before a noun"""
    OAdjective = ""
    adjectiveChance = random.randrange(100) +1
    if(adjectiveChance > 50):
        OAdjective = random.choice(adjectives)    
    return random.choice(articles) + " " + OAdjective +" " + random.choice(nouns)

def verbPhrase():
    """This will build and return a verb phrase."""
    """This will put the prepositional Phrase by 50% of Chance after a verbPhrase"""
    OPrepPhrase = ""
    prepPhraseChance = random.randrange(100) + 1
    if(prepPhraseChance > 50):
        OPrepPhrase =prepositionalPhrase()    
    return random.choice(verbs) + " " + nounPhrase() + " " + OPrepPhrase

def prepositionalPhrase():
    """This will build and return a prepositional phrase."""
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

    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

"""Main function will be implemented"""
if __name__ == "__main__":
    main()
