import random 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words_list = ['love',
'low',
'machine',
'make',
'male',
'man',
'manager',
'map',
'mark']

#chosen word randomly
chosen_word = random.choice(words_list)
#print(chosen_word)

#show like a blanks
display = []
for _ in range(len(chosen_word)):
  display += "_"
print(display)

lives = 6
end_of_game = False
while not end_of_game:
#user can guess a letter
  guess = input("Guess a letter:").lower()
  
  #is the letter in the word? so show the position of it.
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter 
  print(display)

  #if the lives decrease:
  if guess not in chosen_word:
    lives -= 1 
    if lives == 0:
      end_of_game = True
      print("YOU LOSE!")

  #if the all letters are known.
  if "_" not in display:
    end_of_game = True
    print("YOU WIN!")

  print(stages[lives]) #hangman 
  