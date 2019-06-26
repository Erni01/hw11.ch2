# 11. You are given a string.
# In the first line, print the third character of this string.
# In the second line, print the second to last character of this string.
# In the third line, print the first five characters of this string.
# In the fourth line, print all but the last two characters of this string.
# In the fifth line, print all the characters of this string with even indices
# (remember indexing starts at 0, so the characters are displayed starting with the first).
# In the sixth line, print all the characters of this string with odd indices
# i.e. starting with the second character in the string).
# In the seventh line, print all the characters of the string in reverse order.
# In the eighth line, print every second character of the string in reverse order, starting from the last one.
# In the ninth line, print the length of the given string.


text = str(input("Enter some text: "))
print(text[2], "\n",
      text[1:], "\n",
      text[0:5], "\n",
      text[:-2], "\n",
      text[0::2], "\n",
      text[0], "\n",
      text[::-1], "\n",
      text[-1::-2], "\n",
      len(text), sep="")