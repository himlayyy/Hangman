#!usr/bin/env python
from words import words_list
print(len(words_list))
clean = [words for words in words_list if "-" not in words]
print(len(clean))
print(len(max(clean, key=len)))






