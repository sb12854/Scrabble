# 6.00 Problem Set 3B Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Solutions
# Collaborators : <your collaborators>
# Time spent    : <total time>

from ps3a import *
import time
from perm import *


# Problem #6A: Computer chooses a word
#
#
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
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    maxWord = None

    # For each possible word permutation:
    for word in possibleWords:
        # If the permutation is in the word list:
        if word in word_list:
            # Get the word's score
            p_score = get_word_score(word, calculate_handlen(hand))
            # If the word's score is larger than the maximum score seen so far:
            if  p_score >  maxScore:
                # Save the current score and the current word as the best found so far
                maxScore =  p_score
                maxWord = word 
##    print "Score: ",maxScore
##    print "Word: ",maxWord 
    return maxWord

##hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1,'l':1,'e':1,'f':1}
##f = open("words.txt","r") 
##comp_choose_word(hand,f) 
##
##def comp_play_hand(hand,word_list):
##    c=0
##    score = 0 ##SHOULD BE IN THE FUNCTION DEFINITION
##    word = '' 
##    i = random.randrange(1,calculate_handlen(hand)) 
##
##    randomstring = ''.join(random.sample(string(hand),i))
##    randomhand = toHand(randomstring) 
##
##    while calculate_handlen(randomhand)>0 and c <300:
##        c+=1
##        word = comp_choose_word(randomhand, word_list)
##        print "word: ", word  
##        if word == None:
##            print "No more words"
##            return 
##        update_hand(randomhand,word)
##    
##comp_play_hand(SCRABBLE_LETTER_VALUES,f)
 
### Problem #6B: Computer plays a hand
###
###
## 
def comp_play_hand(hand, word_list):
     
    ##original_handlen = calculate_handlen(hand)
    total = 0
    while calculate_handlen(hand) > 0:
        print 'Current Hand:',string(hand) 
        computerWord = comp_choose_word(hand, word_list)
        if computerWord == None:
            break	
        else:
            update_hand(hand,computerWord)
            print "Word: ",computerWord
            total+=get_word_score(computerWord,calculate_handlen(hand))
            print "score: ",total
    print "FINIS"         

            
##            point = get_word_score(computerWord, original_handlen) # calculate points
##            total += point # add points to total
##            print '"%s" earned %d points. Total: %d points' % (computerWord, point, total)# display points and total
##            hand = update_hand(hand, computerWord) # update hand
##
##    print 'No more valid words. Total score: %d points.' % total


#
# Problem #6C: Playing a game
#
##def play_game(word_list): 
##    c=0
##    input = ''
##    ##x = {} YOU CAN CHECK FOR X = {} IF YOU INITIALLY ENTER R BUT HOW
##    print "Enter n, r, or e"
##    input = raw_input().lower().strip()
##    print "Enter u or c"
##    input2 = raw_input().lower().strip()
##    
##    if input2 == 'u': 
##        if(input == 'e'):
##            return
##        while (input != 'e'):
##            c+=1
##            ##print "xw: ", x
##            if(input == 'n' or c==1):
##                ##print "c: ", c
##                x = play_hand(SCRABBLE_LETTER_VALUES,f) ##carries out function automatically with assignment
##            if (input == 'r' and c!=1): 
##                play_hand(x,f)
##            print "Enter n, r, or e"
##            ##print "x3: ", x
##            input = raw_input().lower() 
##        print('Goodbye!')
##
##    if input2 == 'c': 
##        comp_play_hand(hand, word_list)
##

def play_game(word_list):
    hand = deal_hand(HAND_SIZE)
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        while cmd != 'n' and cmd != 'r' and cmd != 'e':
            print "Invalid command."
            cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        if cmd == 'e':
            break 
 
        player = raw_input('Enter u to have yourself play, c to have the computer play: ')
        while player != 'u' and player != 'c':
            print "Invalid command."
            player = raw_input('Enter u to have yourself play, c to have the computer play: ')

        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
        if player == 'u':
            play_hand(hand, word_list)
        else:
            comp_play_hand(hand, word_list)


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    print "Goodbye!"

    
