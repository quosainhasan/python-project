# Function to compute letter frequency
def letter_frequency(sentence):
    frequency_dict = {}

    for char in sentence:
        if char.isalpha():
            char = char.lower()
            frequency_dict[char] = frequency_dict.get(char, 0) + 1

    return frequency_dict

# Get input sentence from the user
user_sentence = input("Enter a sentence: ")

# Compute and print letter frequency
result = letter_frequency(user_sentence)
print("Letter Frequency:")
for letter, frequency in result.items():
    print(f"{letter}: {frequency}")
