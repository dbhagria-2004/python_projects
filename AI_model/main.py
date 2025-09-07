
import torch

print(torch.cuda.is_available())

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("summarization", model="facebook/bart-large-cnn", device=0)
# Summarize a text

response = pipe("this is the best course on transformers I've ever taken. I love it and I recommend it to everyone.")

print(response)