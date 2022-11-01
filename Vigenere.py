import random
# Aidan Johnson

# adds a space a string every 4 characters to break up the characters
def add_spaces(string):
    array = list(string)
    spaced_string = ""
    for x in range(0, len(array)):
        if x % 4 != 0 or x == 0:
            spaced_string += str(array[x])
        else:
            spaced_string += " " + str(array[x])

    return spaced_string


class Vigenere:

    def __init__(self, seed):

        self.alphabet = 95
        self.min_char = 32
        self.max_char = 125

        random.seed(seed)
        self.rand = random.Random
        self.table = self.generate_table()

# generates a list of alphabets, each index containing every character from ! (33) to ~ (126)
# randomly shuffled
    def generate_table(self):
        table_list = []
        for x in range(0, self.alphabet - 1):
            sub_table = []
            for y in range(0, self.alphabet - 1):
                char = (y + self.min_char) + x

                if char > self.max_char:
                    char -= self.alphabet - 1

                sub_table.append(chr(char))

            random.shuffle(sub_table)
            table_list.append(sub_table)

        return table_list

# TODO: Make decoding work the first time, without needed the second encoding method
# replaces each character in the encoded string with the character associated with the list used to encode it.
    def decode(self, encoded, key_string):
        text = encoded.replace(" ", "")
        key_text = list(key_string)
        encoded_message = ""
        key_iter = 0

        for x in text:
            char = ord(x) - self.min_char

            char_list = self.table[ord(key_text[key_iter % len(key_string)]) - self.min_char]

            char_index = ord(char_list[char]) - self.min_char

            encod_char = char_list[char_index]

            encoded_message += encod_char

            key_iter += 1

        return self.encode(encoded_message, key_string)

# encodes the given plaintext string by replacing each character with the character in the index associated with the
# character in the list associated with a character in the key string in the table
    def encode(self, secret, key_string):
        text = list(secret)
        key_text = list(key_string)
        decoded_message = ""
        key_iter = 0

        for x in text:
            char_list = self.table[ord(key_text[key_iter % len(key_string)]) - self.min_char]

            char = char_list.index(x) + self.min_char

            decoded_message += chr(char)
            key_iter += 1

        return decoded_message


# generates the seed for the random object by summing the total char values of the key string
def generate_seed(key):
    seed = 0

    for char in key:
        seed += ord(char)

    return seed


def main():
    operation = input("Encoding or decoding? ")

    while not operation.casefold().__contains__("encode") and not operation.casefold().__contains__("decode"):
        operation = input("Error: Please enter \"encode\" or \"decode\". ")

    message = input("What are you trying to " + operation + "? ")
    key = input("Enter key. ")

    while key.__contains__(" "):
        key = input("Error: Key may not contain any spaces. Please enter new key. ")

    seed = generate_seed(key)

    cipher = Vigenere(seed)

    if operation.casefold().__contains__("encode"):
        processed_message = cipher.encode(message, key)
        print(operation + "d message: " + add_spaces(processed_message))
    else:
        processed_message = cipher.decode(message, key)
        print(operation + "d message: " + processed_message)
