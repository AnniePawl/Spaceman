import random
import sys

# Loop so that people can play again and again!
is_playing = True
while is_playing:

	# Get a random word
	words = ["hello", "hussy"]
	word = words[random.randint(0, len(words) - 1)]

	curr_progress = "_" * len(word)

	# Loop to control specific game
	game_not_over = True
	num_wrong = 0
	while game_not_over:

		# Print out the current progress!
		print()
		for character in curr_progress:
			# this will print out characters without starting new line
			sys.stdout.write(character)
			sys.stdout.write(" ")
		print()

		# Get new guess!
		guess = input("Guess a character: ")

		# Merge current progress with new guess
		if guess in word:
			new_progress = ""
			for i in range(len(word)):
				# Add guessed letter if it's correct.
				if word[i] == guess:
					new_progress += guess
				# Otherwise take current progress character
				else:
					new_progress += curr_progress[i]

			# New progress state, update variable
			curr_progress = new_progress

		else:
			num_wrong += 1

		# Check if they lost. If so, break game loop.
		if num_wrong == 7:
			print()
			print("YOU LOST!")
			print()
			break

		# Check if they won. If so, break game loop.
		if curr_progress == word:
			print()
			print("YOU WON!")
			print()
			break

	# Check if they want to play again.
	play_again = input("Want to play again? [y/n] ")
	is_playing = play_again == "y"
