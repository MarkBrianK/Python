# def fizzbuzz(n):
#     result = []

#     for i in range(1,n+1):
#         add = ''

#         if i%3 ==0:
#             add += 'fizz'

#         if i % 5 == 0:
#             add += 'buzz'

#         if add == '':
#             result.append(i)
#         else:
#          result.append(add)

#     print(result)

# fizzbuzz(100)

# def squared(n):

#     result=[]

#     for i in range(1,n+1):
#         sqr = i ** 2
#         result.append(sqr)





#     print(result)

# squared(20)

# def bottles(number):
#     print(f'{number} green bottles sitting on the wall')

# def main():
#     num = input("Enter the number of bottles on the wall:")
#     bottles(num)

# if __name__  == "__main__":
#     main()


# def generate_fibonacci(n):
#     result = []
#     a, b = 0, 1
#     while len(result) < n:
#         result.append(b)
#         a, b = b, a + b
#     return result

# def main():
#     n = 20  # We want the first 20 numbers
#     fibonacci_sequence = generate_fibonacci(n)
#     print("The first 20 numbers in the Fibonacci sequence are:")
#     print(fibonacci_sequence)

# if __name__ == "__main__":
#     main()
# def main():
#     while True:
#         try:
#             input_numbers = input("Enter the numbers separated by spaces: ")
#             numbers = list(map(float, input_numbers.split()))
#             if numbers:
#                 break
#             else:
#                 print("Please enter at least one number.")
#         except ValueError:
#             print("Invalid input. Please enter valid numbers separated by spaces.")

#     count = len(numbers)
#     total = sum(numbers)
#     mean = total / count

#     print(f"The total of the entered numbers is: {total}")
#     print(f"The mean (average) of the entered numbers is: {mean}")

# if __name__ == "__main__":
#     main()

# import random

# def generate_question():
#     operators = ['+', '-', '*']
#     a = random.randint(1, 9)
#     b = random.randint(1, 9)
#     operator = random.choice(operators)

#     if operator == '+':
#         correct_answer = a + b
#     elif operator == '-':

#         correct_answer = a - b
#     else:  # operator == '*'
#         correct_answer = a * b

#     return a, operator, b, correct_answer

# def ask_question(a, operator, b):
#     question = f"{a} {operator} {b} = "
#     while True:
#         try:
#             user_answer = int(input(question))
#             return user_answer
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# def main():
#     correct_count = 0
#     total_questions = 10

#     for _ in range(total_questions):
#         a, operator, b, correct_answer = generate_question()
#         user_answer = ask_question(a, operator, b)

#         if user_answer == correct_answer:
#             print("Correct!")
#             correct_count += 1
#         else:
#             print(f"Incorrect. The correct answer is {correct_answer}.")

#     print(f"\nYou got {correct_count} out of {total_questions} correct.")

# if __name__ == "__main__":
#     main()



