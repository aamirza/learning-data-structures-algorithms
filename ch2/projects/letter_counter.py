"""Write a Python program that inputs a document and then outputs a bar-chart plot of the frequencies of each alphabet
character that appears in that document."""


def alphabet_counter(file):
    alphabet_letters = [chr(letter) for letter in range(ord('a'), ord('z')+1)]

    letter_count = {letter: 0 for letter in alphabet_letters}
    with open(file, 'r') as f:
        for line in f:
            for char in line:
                if char != ' ' and char.lower() in alphabet_letters:
                    letter_count[char.lower()] += 1

    print("-"*50)
    for letter, count in letter_count.items():
        print(f"{letter} - {'|' * count}")


if __name__ == "__main__":
    alphabet_counter("./letter_counter_demo.txt")
