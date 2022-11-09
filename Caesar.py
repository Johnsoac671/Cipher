class Caesar:

    def __init__(self, offset):
        self.offset = offset

    def set_offset(self, offset):
        self.offset = offset

    def encode(self, plaintext):
        encoded_string = ""
        for char in plaintext:
            encoded_char = ord(char) + self.offset

            if encoded_char > 122:
                encoded_char = 96 + (encoded_char - 122)

            encoded_string += chr(encoded_char)

        return encoded_string

    def decode(self, encoded_text):
        decoded_string = ""
        for char in encoded_text:
            decoded_char = ord(char) - self.offset

            if decoded_char < 97:
                decoded_char = 122 - (96 - decoded_char)

            decoded_string += chr(decoded_char)

        return decoded_string
