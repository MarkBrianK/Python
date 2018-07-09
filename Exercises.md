1.	Write a program that reads some integers between 1 and 100 and counts the 
	occurences of each. Here is a sample run of the program:

	Enter integers between 1 and 100: 2 5 6 5 4 3 23 43 2 [ENTER]
	2 occurs 2 times
	3 occurs 1 time
	4 occurs 1 time
	5 occurs 2 times
	6 occurs 1 time
	23 occurs 1 time
	43 occurs 1 time
	
	Note that if a number occurs more than one time, the plural word "times" 
	is used in the output.

2. 	You can shuffle a list using random.shuffle(lst).
	Write your own function without using random.shuffle(lst) to shuffle a 
	list and return the list. Use the following function header:

	def shuffle(lst):

	Write a test program that prompts the user to enter five numbers, invokes 
	the function to shuffle the numbers, and displays the numbers.

3. 	Write a function which implements a selection-sort algorithm by repeatedly 
	finding the smallest number in a list and swapping it with the last one until the list is sorted.

	Write a test program that reads in ten numbers, invokes the function, and displays the sorted numbers.

4. 	Write a sort function that uses the bubble-sort algorithm. The bubble-sort
	algorithm makes several passes through the list. On each pass, successive neighbouring pairs are compared. If a pair is in decreasing order, its values are swapped; otherwise, the values remain unchanged. The technique is called bubble-sort or sinking-sort because the smaller values gradually "bubble" their way to the top and larger values "sink" to the bottom.

	Write a test program that reads in ten numbers, invokes the function, and displays the sorted numbers.

5. 	(Game: Eight Queens) The classic Eight Queens puzzle is to place eight
	queens on a chessboard such that no two queens can attack each other (i.e., no two queens are in the same row, same column, or same diagonal). There are
	many possible solutions. Write a program that displays one such solution. A
	sample output is shown below:
	|Q| | | | | | | |
	| | | | |Q| | | |
	| | | | | | | |Q|
	| | | | | |Q| | |
	| | |Q| | | | | |
	| | | | | | |Q| |
	| |Q| | | | | | |
	| | | |Q| | | | |

6. 	(Game: bean machine) The bean machine, also known as a quincunx or the
	Galton box, is a device for statistics experiments named after English scientist Sir Francis Galton. It consists of an upright board with evenly spaced nails (or pegs) in a triangular pattern, as shown in Figure 10.15.
	Balls are dropped from the opening of the board. Every time a ball hits a nail, it has a 50% chance of falling to the left or to the right. The piles of balls are accumulated in the slots at the bottom of the board

	Write a program that simulates the bean machine. Your program should
	prompt the user to enter the number of the balls and the number of the slots in the machine. Simulate the falling of each ball by printing its path. For example, the path for the ball in Figure 10.15b is LLRRLLR and the path for the ball in Figure 10.15c is RLRRLRR. Display the final buildup of the balls in the slots in a histogram. Here is a sample run of the program:

	Enter the number of balls to drop: [ENTER]
	Enter the number of slots in the bean machine: [ENTER]

	LRLRRLR
	RRLLLRR
	LLRLLRR
	RRLLLLL
	LRLRRLR

		O 
		O 
		OOO 

7. 	(Game: locker puzzle) A school has 100 lockers and 100 students. All lockers
	are closed on the first day of school. As the students enter, the first student,denoted S1, opens every locker. Then the second student, S2, begins with the second locker, denoted L2, and closes every other locker. Student S3 begins with the third locker and changes every third locker (closes it if it was open, and opens it if it was closed). Student S4 begins with locker L4 and changes every fourth locker. Student S5 starts with L5 and changes every fifth locker, and so on, until student S100 changes L100. After all the students have passed through the building and changed the lockers, which lockers are open? Write a program to find your answer.

	(Hint: Use a list of 100 Boolean elements, each of which indicates whether a locker is open (True) or closed (False). Initially, all lockers are closed.)

8. (Game: hangman) Write a hangman game that randomly generates a word and
	prompts the user to guess one letter at a time, as shown in the sample run. Each letter in the word is displayed as an asterisk. When the user makes a correct guess, the actual letter is then displayed. When the user finishes a word, display the number of misses and ask the user whether to continue playing. Create a list to store the words, as follows:

	# Use any words you wish
	words = ["write", "that", "program", ...]

	(Guess) Enter a letter in word ******* > p 	[ENTER]
	(Guess) Enter a letter in word p****** > r 	[ENTER]
	(Guess) Enter a letter in word pr**r** > p 	[ENTER]
		p is already in the word
	(Guess) Enter a letter in word pr**r** > o 	[ENTER]
	(Guess) Enter a letter in word pro*r** > g 	[ENTER]
	(Guess) Enter a letter in word progr** > n 	[ENTER]
		n is not in the word
	(Guess) Enter a letter in word progr** > m 	[ENTER]
	(Guess) Enter a letter in word progr*m > a 	[ENTER]
	The word is program. You missed 1 time

	Do you want to guess another word? Enter y or n>

9. 	(Simulation: coupon collector’s problem) Coupon Collector is a classic 
	statistics problem with many practical applications. The problem is to pick objects from a set of objects repeatedly and find out how many picks are needed for all the objects to be picked at least once. A variation of the problem is to pick cards from a shuffled deck of 52 cards repeatedly and find out how many picks are needed before you see one of each suit. Assume a picked card is placed back in the deck before picking another. Write a program to simulate the number of picks needed to get four cards, one from each suit and display the four cards picked (it is possible a card may be picked twice). Here is a sample run of the program: 

	Queen of Spades
	5 of Clubs
	Queen of Hearts
	4 of Diamonds
	Number of picks: 12

10. (Financial: credit card number validation) Credit card numbers follow
	certain patterns: It must have between 13 and 16 digits, and the number must start with:

	■ 4 for Visa cards
	■ 5 for MasterCard credit cards
	■ 37 for American Express cards
	■ 6 for Discover cards

	In 1954, Hans Luhn of IBM proposed an algorithm for validating credit card numbers. The algorithm is useful to determine whether a card number is entered correctly or whether a credit card is scanned correctly by a scanner. Credit card numbers are generated following this validity check, commonly known as the Luhn checkor the Mod 10 check, which can be described as follows (for illustration, consider the card number 4388576018402626):

	1. Double every second digit from right to left. If doubling of a digit results in a two-digit number, add up the two digits to get a single-digit number.

	4388576018402626
	2 *2 = 4
	2 *2 = 4
	4 *2 = 8
	1 *2 = 2
	6 *2 = 12 (1 + 2 = 3)
	5 *2 = 10 (1 + 0 = 1)
	8 *2 = 16 (1 + 6 = 7)
	4 *2 = 8

	2. Now add all single-digit numbers from Step 1.

	3. Add all digits in the odd places from right to left in the card number.

	4. Sum the results from Steps 2 and 3.

	5. If the result from Step 4 is divisible by 10, the card number is valid; otherwise, it is invalid. For example, the number 4388576018402626 is invalid, but the number 4388576018410707 is valid.
	
	Write a program that prompts the user to enter a credit card number as an integer. Display whether the number is valid or invalid. Design your program to use the following functions:

	# Return true if the card number is valid
	defisValid(number):

	# Get the result from Step 2
	defsumOfDoubleEvenPlace(number):

	# Return this number if it is a single digit, otherwise, return
	# the sum of the two digits
	defgetDigit(number):

	# Return sum of odd place digits in number
	defsumOfOddPlace(number):

	# Return true if the digit d is a prefix for number
	defprefixMatched(number, d):

	# Return the number of digits in d
	defgetSize(d):

	# Return the first k number of digits from number. If the
	# number of digits in number is less than k, return number.
	defgetPrefix(number, k):