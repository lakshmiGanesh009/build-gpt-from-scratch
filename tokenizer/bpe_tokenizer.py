from collections import Counter, defaultdict

class BPETokenizer:

# Initialize Vocabulary
    def __init__(self):
        self.vocab = {}
        self.merges = {}

    def get_stats(self, vocab):
        pairs = defaultdict(int)
        for word, freq in vocab.items():
            symbols = word.split()
            for i in range(len(symbols) - 1):
                pairs[(symbols[i], symbols[i+1])] += freq
        return pairs

# Merge Most Frequent Pair
    def merge_vocab(self, pair, vocab):
        new_vocab = {}
        bigram = " ".join(pair)
        replacement = "".join(pair)
        for word in vocab:
            new_word = word.replace(bigram, replacement)
            new_vocab[new_word] = vocab[word]
        return new_vocab

# Train BPE
    def train(self, corpus, num_merges=10):
        vocab = Counter()
        for word in corpus.split():
            vocab[" ".join(list(word))] += 1
        for i in range(num_merges):
            pairs = self.get_stats(vocab)
            if not pairs:
                break
            best = max(pairs, key=pairs.get)
            vocab = self.merge_vocab(best, vocab)
            self.merges[best] = "".join(best)
        self.vocab = vocab

# Encode
    def encode(self, word):
        tokens = list(word)
        while True:
            pairs = [(tokens[i], tokens[i+1]) for i in range(len(tokens)-1)]
            merge_candidate = None
            for pair in pairs:
                if pair in self.merges:
                    merge_candidate = pair
                    break
            if not merge_candidate:
                break
            new_tokens = []
            i = 0
            while i < len(tokens):
                if i < len(tokens)-1 and (tokens[i], tokens[i+1]) == merge_candidate:
                    new_tokens.append(tokens[i] + tokens[i+1])
                    i += 2
                else:
                    new_tokens.append(tokens[i])
                    i += 1
            tokens = new_tokens
        return tokens

if __name__ == "__main__":
    corpus = "low lower lowest new newer newest"
    tokenizer = BPETokenizer()
    tokenizer.train(corpus, num_merges=50)
    print(tokenizer.encode("lowest"))
