import torch
import torch.nn as nn

class TokenEmbedding(nn.Module):

    def __init__(self, vocab_size, embed_dim):
        super().__init__()

        self.embedding = nn.Embedding(vocab_size, embed_dim)

    def forward(self, token_ids):

        return self.embedding(token_ids)


# Example usage
vocab_size = 100
embed_dim = 16

model = TokenEmbedding(vocab_size, embed_dim)

tokens = torch.tensor([1, 5, 20, 4])

output = model(tokens)

print(output)
print(output.shape)