class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.strip().split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words

if __name__ == "__main__":
    input_text = str(input("Enter a sentence"))
    reverser = StringReverser(input_text)
    print(reverser.reverse_words()) 