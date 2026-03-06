class SimpleTokenizer:

    def __init__(self):
        self.word2id = {}
        self.id2word = {}

    def build_vocab(self, text):

        words = text.split()

        vocab = sorted(set(words))

        for i, word in enumerate(vocab):
            self.word2id[word] = i
            self.id2word[i] = word

    def encode(self, sentence):

        return [self.word2id[word] for word in sentence.split()]

    def decode(self, tokens):

        return " ".join(self.id2word[token] for token in tokens)


if __name__ == "__main__":

    text = "I love AI and I love building AI systems"

    tokenizer = SimpleTokenizer()

    tokenizer.build_vocab(text)

    encoded = tokenizer.encode("I love AI")

    print("Encoded:", encoded)

    print("Decoded:", tokenizer.decode(encoded))