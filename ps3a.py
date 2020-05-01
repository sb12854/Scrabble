# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# 
from perm import *
import random
import string

##WORD ZOOLOGIST WAS ADDED, SO IT SAYS 83668 NOT 83667 WORDS 

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,\
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,\
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
##print SCRABBLE_LETTER_VALUES[('f')] 

WORDLIST_FILENAME = "words.txt"

f = open("words.txt","r") 

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    import string 
    """
    Returns the score for a word. Assumes the word is a
    valid word.

	The score for a word is the sum of the points for letters
	in the word multiplied by the length of the word, plus 50
	points if all n letters are used on the first go.

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    s = 0 
    c = 0
    word.lower() 
    for c in range (len(word)):
        s+=SCRABBLE_LETTER_VALUES[(word[c])]
    s*=len(word)
    if c == (n-1): ##as we count beginning from 1 (natural number) 
        s+=50
    return s
 
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

 

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
 
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
	In other words, this assumes that however many times
	a letter appears in 'word', 'hand' has at least as
	many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word = word.lower() ##YOU CAN'T JUST WRITE word.lower() HERE 
    for i in range(len(word)):
        for j in hand.keys():
            if word[i]==j and hand[j]==1: ##word[i] is the key;                                          
                del hand[j] ##MUST CHECK IF THE VALUE IS 1 OR NOT
            elif word[i]==j and hand[j]!=1: ##OR PERHAPS ALWAYS DEDUCT ONE, THEN DELETE
                             ##THOSE WITH A 0
                ##NOT elif hand[j]!=1:!!!
                hand[j]-=1  
                break 
    return hand ##TYPE IS NONE IF THIS IS OMITTED

def string(hand):
    s = "" 
    for element in hand:
        for i in range(hand[element]):
            s+=element
            s+= ' ' 
    return s
def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen

def occinstr(char,string):
    occinstr = 0
    for i in string: 
        if (i==char):
            occinstr+=1
    return occinstr
 
def toHand(string):
    hand = {}          
    c=0
    for i in range(len(string)): 
        if string[i] != ' ':    
            hand[string[i]] = occinstr(string[i],string)    
    return hand 

def is_valid_word(word, hand, word_list): 
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    truth = 0 
    f = open ("words.txt","r") ##THIS MUST BE IN HERE
    for x in enumerate(f):
        for i in x:
            if type(i) == str and i.strip().lower()==word.strip().lower():
                truth+=1 
            
    if truth == 0: 
        return False 

    for i in word:
        for j in hand.keys():
                if i == j and occinstr(j,word) > hand[j]:
                    return False
                elif i == j:    
                    truth+=1 
    if truth <= len(word): ##THIS MUST NOT BE INDENTED 
        return False
    return True

def comp_choose_word(hand, word_list):
    """
    Given a hand and a word_list, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all possible 
    permutations of lengths 1 to HAND_SIZE.
   
    If all possible permutations are not in word_list, return None.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # Create an empty list to store all possible permutations of length 1 to HAND_SIZE
    possibleWords = []

    # For all lengths from 1 to HAND_SIZE (including! HAND_SIZE):
    for length in range(1, calculate_handlen(hand)+1):
        # Get the permutations of this length 
        # And store the permutations in the list we initialized earlier
        #  (hint: don't overwrite the list - you want to add to it)
        possibleWords.extend(get_perms(hand, length))

    # Create a new variable to store the maximum score seen so far (initially 0)
    score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    maxWord = None

    # For each possible word permutation:
    for word in possibleWords:
        # If the permutation is in the word list:
        if word in word_list:
##            print get_word_score(word)
##            print max(score,get_word_score(word))
##            print "score1: ", score 
##            score = max(score,get_word_score(word))
##            print "score2: ", score 
##            if score == get_word_score(word):
##                maxWord = word
            p_score = get_word_score(word, HAND_SIZE)
            # If the word's score is larger than the maximum score seen so far:
            if  p_score >  maxScore:
                # Save the current score and the current word as the best found so far
                maxScore =  p_score
                maxWord = word
    print "score: ", score             
    return maxWord  

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1,'l':1,'e':1,'f':1}
 
def play_hand(hand, word_list):
    score = 0 ##SHOULD BE IN THE FUNCTION DEFINITION
    word = '' 
    i = random.randrange(1,calculate_handlen(hand)) 

    randomstring = ''.join(random.sample(string(hand),i))

    if (hand != SCRABBLE_LETTER_VALUES):
        randomstring = string(hand)  
        
    print "The hand is: ",
    
    for i in randomstring:
        if i != ' ': 
            print i, 
    randomhand = toHand(randomstring) 
    print
    stored = ''
    ##x = toHand(string(randomhand)+word)
    ##print "randomhand: ", randomhand 
    ##print "x333: ",x
    ##print is_valid_word(word,randomhand,f)
    ##WHAT HAPPENS IF YOU PUT WORD=RAW_INPUT() HERE? 
    while (calculate_handlen(randomhand)>0 and word != '.'):
    ##if (score!=0): 
    ##print is_valid_word(word,randomhand,f)
        word=raw_input().strip() ##THIS SHOULD BE IN THE LOOP, IN THIS ORDER 
        stored+=word.strip('.')
        if (calculate_handlen(randomhand)==0 or word == '.'): ##SEEMS REDUNDANT BUT NECESSARY
            print "Your score is ", score
            ##print "randomhand: ", randomhand
            ##print "word: ",word 
            ##print "x333: ",toHand(string(randomhand)+stored)
            return toHand(string(randomhand)+stored)
        while (is_valid_word(word,randomhand,f) == False and calculate_handlen(randomhand)>0): ##THIS UPDATES THE HAND
            print "Please enter a valid word" 
            word=raw_input().lower() 
            stored+=word.strip('.')
            if (calculate_handlen(randomhand)==0 or word == '.'):
                ##print "Your score is ", score
                ##print "randomhand: ", randomhand 
                ##print "x333: ",toHand(string(randomhand)+stored)
                return toHand(string(randomhand)+stored)
        print "The updated hand is: ", string(update_hand(randomhand,word)) ##DO NOT UPDATE AGAIN 
        temp = score 
        score+=get_word_score(word,(calculate_handlen(randomhand)+len(word)))
        print "Your score is ", score
 

