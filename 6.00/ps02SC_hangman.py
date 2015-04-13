# A hangman game created by MIT professor. Code contains lots of useful structure and application
# for study. The added comments explain what each line does.

import random
import string

WORDLIST_FILENAME = 'hangman_words.txt'


# Returns a list of words from the imported .txt file
def load_words():
	print "Loading word list from file..."
	# opens the .txt file in read only mode
	inFile = open(WORDLIST_FILENAME, 'r', 0)
	# Converts the block of text in the file to a line
	line = inFile.readline()
	# Splits the line into words based on whitespace
	wordlist = string.split(line)
	# A fun output to tell you how many words are in the .txt file
	print len(wordlist), "words loaded."
	return wordlist


# When called it returns a random word choice
def choose_word(wordlist):
	return random.choice(wordlist)


# Iterates through the letters in the target word and creates a string 
# with _ and correclty guesed letters
def partial_word(secret_word, guessed_letters):
	result = ''
	# Iterates through the target word and checks the following...
	for letter in secret_word:
		# If the guessed letter is in target word then the letter will be added to the string
		if letter in guessed_letters:
			result = result + letter
		# If a guessed letter is not in the target word an _ will be added to the string
		else:
			result = result + '_'
	return result


def hangman():
	print "Welcome to the game Hangman!"
	##secret_word = choose_word(wordlist)
	secret_word = 'secret'
	# Interpolates the length of the chosen secret_word in the string
	print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
	num_guesses = 8
	word_guessed = False
	guessed_letters = ''
	available_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
						'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	# Uses the and conditional to check if both statements evaluate to true. Note that
	# the second statement contains a not. If one is false then move to the if statement
	# on line 80.
	while num_guesses > 0 and not word_guessed:
		print '------------'
		# Interpolates the number of guesses
		print "You have " + str(num_guesses) + " guesses left."
		# the open quotes before .join means there will be no space delimitiing the letters
		print "Available letters: " + ''.join(available_letters)
		guess = raw_input("Please guess a letter: ")
		# Tests if the guessed letter is in the list of available letters and that the guess is one
		# letter long.
		if guess not in available_letters and len(guess) == 1:
			print ("Oops! You have already guessed"
				  "that letter: " + partial_word(secret_word, guessed_letters))
		# Tests if the guess is more than one character in length.
		elif len(guess) > 1:
			print ("Oops! Please guess one letter" 
				  "at a time: " + partial_word(secret_word, guessed_letters))
		# Checks if the guessed letter is not in the secret_word. If True then the number of
		# guesses is decresed by one and the guess is removed from the available letters.
		elif guess not in secret_word:
			num_guesses -= 1
			available_letters.remove(guess)
			print "Oops! That letter is not in my word: " + partial_word(secret_word, guessed_letters)
		# If a correct guess is made the letter is removed from available choices and added to
		# guessed letters.
		else:
			available_letters.remove(guess)
			guessed_letters += guess
			print "Good guess: " + partial_word(secret_word, guessed_letters)
		# If the partial word is completely guessed then it should equal the secret word. If so
		# change the value of word_guessed to True.
		if secret_word == partial_word(secret_word, guessed_letters):
			word_guessed= True
	if word_guessed:
		print "Congratulations, you won!"
	else:
		print "Game over..."
		print "The word was " + secret_word


wordlist = load_words()

hangman()