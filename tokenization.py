# -*- coding: utf-8 -*-
"""Tokenization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uOZqKV7OyQQxlFOnJME_l4WdGa-tnaDj
"""

import nltk

nltk.download('punkt')

paragraph = """
There was once a woman who was very, very cheerful, though she had little to make her so; for she was old, and poor, and lonely. She lived in a little bit of a cottage and earned a scant living by running errands for her 
neighbours, getting a bite here, a sup there, as reward for her services. So she made shift to get on, and always looked as spry and cheery as if she had not a want in the world. Now one summer evening, as she was trotting, 
full of smiles as ever, along the high road to her hovel, what should she see but a big black pot lying in the ditch! "Goodness me!" she cried, "that would be just the very thing for me if I only had something to put in it! 
But I have not! Now who could have left it in the ditch?" And she looked about her expecting the owner would not be far off; but she could see nobody. "Maybe there is a hole in it," she went on, "and that is why it has been 
cast away. But it would do fine to put a flower in for my window; so I will just take it home with me." And with that she lifted the lid and looked inside. "Mercy me!" she cried, fair amazed. "If it is not full of gold pieces. 
Here is luck!" And so it was, brimful of great gold coins. Well, at first she simply stood stock-still, wondering if she was standing on her head or her heels. Then she began saying: "Lawks! But I do feel rich. I feel awful 
rich!"
"""

sentences = nltk.sent_tokenize(paragraph)

sentences

words = nltk.word_tokenize(paragraph)

words

