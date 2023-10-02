from nltk.tokenize import TweetTokenizer

text = "@TargetZonePT 😡 no he bloody isn't I was upstairs getting changed !"

# Instantiate the tokenizer
tknzr = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)
tknzr1 = TweetTokenizer()

# Tokenize the tweet
tokens = tknzr.tokenize(text)
tokens1 = tknzr1.tokenize(text)
print(tokens1)
print(tokens)