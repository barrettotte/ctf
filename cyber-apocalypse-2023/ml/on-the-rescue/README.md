# on-the-rescue

TODO: review writeup

> The archeologist finally found the ancient vessel. 
> Utilizing the alien technology he managed to breach in the central computational unit and learn the reason behind their visit on Earth millions of years ago. 
> A message appeared. 
> It was all a desperate plan for the survival of their kind.

HTB discord

```py
import torch
import random
import torch.nn as nn
from torch.nn import functional as F

class BigramLanguageModel(nn.Module):

    def __init__(self, vocab_size):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, vocab_size)

    def forward(self, idx, targets=None):

        logits = self.token_embedding_table(idx) 
        
        if targets is None:
            loss = None
        else:
            B, T, C = logits.shape
            logits = logits.view(B*T, C)
            targets = targets.view(B*T)
            loss = F.cross_entropy(logits, targets)

        return logits

# Load the pre-trained model
model_dict = torch.load('bigram_model.pt')
model_tensor = list(model_dict.values())[0]

# Define the vocabulary used by the model
vocab = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}\n")

# Create a new instance of the BigramLanguageModel class
model = BigramLanguageModel(len(vocab))

# Initialize the embedding layer with the pre-trained tensor
with torch.no_grad():
    model.token_embedding_table.weight.copy_(model_tensor)

# Set the model to evaluation mode
model.eval()

# Use the model to generate text
text = ""
prev_token = random.choice(vocab)
while len(text) < 1000:
    with torch.no_grad():
        input_tensor = torch.LongTensor([[vocab.index(prev_token)]])
        output = model(input_tensor)
        logits = output[0, -1, :]
        probs = F.softmax(logits, dim=-1)
        prev_token = random.choices(vocab, weights=probs.tolist())[0]
        text += prev_token
print(text)
```

## Attempt

pytorch

```sh
pip3 install torch

strings bigram_model.pt
# token_embedding_table.weightq
```

- https://pytorch.org/tutorials/beginner/saving_loading_models.html
- https://github.com/L1aoXingyu/pytorch-beginner/blob/master/06-Natural%20Language%20Process/N-Gram.py
- https://towardsdatascience.com/implementing-a-character-level-trigram-language-model-from-scratch-in-python-27ca0e1c3c3f
- https://towardsdatascience.com/language-modeling-with-lstms-in-pytorch-381a26badcbf
