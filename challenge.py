def rot13(text):
    result = []

    for char in text:
        # Check if character is a letter
        if 'a' <= char <= 'z':
            # Rotate within the range of lowercase letters
            rotated_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            # Rotate within the range of uppercase letters
            rotated_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            # Non-alphabetic characters remain unchanged
            rotated_char = char

        result.append(rotated_char)

    return ''.join(result)

def main():
    while True:
        choice = input("Enter '1' to encrypt/decrypt text using ROT13 or 'q' to quit: ").strip().lower()

        if choice == '1':
            text = input("Enter the text: ").strip()
            result = rot13(text)
            print(f"ROT13 result: {result}\n")
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()


# Define the points for each letter in the English alphabet
letter_points = {
    'E': 1,  'A': 2,  'R': 3,  'I': 4,  'O': 5,  'T': 6,  'N': 7,  'S': 8,  'L': 9,  'C': 10,
    'U': 11, 'D': 12, 'P': 13, 'M': 14, 'H': 15, 'G': 16, 'B': 17, 'F': 18, 'Y': 19, 'W': 20,
    'K': 21, 'V': 22, 'X': 23, 'Z': 24, 'J': 25, 'Q': 26
}

def calculate_score(word):
    # Convert the word to uppercase to match the dictionary keys
    word = word.upper()
    score = 0

    for letter in word:
        if letter in letter_points:
            score += letter_points[letter]

    return score

def main():
    while True:
        word = input("Enter a word to calculate its score (or 'q' to quit): ").strip()

        if word.lower() == 'q':
            print("Goodbye!")
            break

        score = calculate_score(word)
        print(f"The score for the word '{word}' is: {score}\n")

if __name__ == "__main__":
    main()
