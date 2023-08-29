# Keyboard Row
- Given an array of strings `words`, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:
- the first row consists of the characters `"qwertyuiop"` ,
- the second row consists of the characters `"asdfghjkl"` , and
- the third row consists of the characters `"zxcvbnm"`.

## Analysis
- At first, I thought I needed a string method to do this, but it turned out that it wasn't necessary
- I did not know you could compare sets with `<=`, which is basically the same as `.issubset()`
- Prior knowledge about `any()` would have been helpful too
- The tuple of sets in the better solution turned out to be quite useful
