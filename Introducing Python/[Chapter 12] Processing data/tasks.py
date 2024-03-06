# 12.1. Create a Unicode string called mystery and assign it the value '\U0001f984'.
# Print mystery and its Unicode name.
import struct
import sys
import unicodedata

sys.stdout.reconfigure(encoding='utf-8')
mystery = '\U0001f984'
print(mystery)
print(unicodedata.name(mystery))

# 12.2 Encode mystery, this time using UTF-8, into the bytes variable pop_bytes.
# Print pop_bytes.
pop_bytes = mystery.encode('UTF-8')
print(pop_bytes)

# 12.3 Using UTF-8, decode pop_bytes into the string variable pop_string. Print
# pop_string. Is pop_string equal to mystery?
pop_string = pop_bytes.decode('UTF-8')
print(pop_string)
pop_string == mystery
print(pop_string == mystery)

# 12.4 When you’re working with text, regular expressions come in very handy. We’ll
# apply them in a number of ways to our featured text sample. It’s a poem titled “Ode
# on the Mammoth Cheese,” written by James McIntyre in 1866 in homage to a seventhousand-pound
# cheese that was crafted in Ontario and sent on an international tour.
# If you’d rather not type all of it, use your favorite search engine and cut and paste the
# words into your Python program, or just grab it from Project Gutenberg. Call the text
# string mammoth.
# Example 12-1. mammoth.txt
mammoth = '''
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
A Jewelry Analogy | 245
The great world's show at Paris.
Of the youth beware of these,
 For some of them might rudely squeeze
 And bite your cheek, then songs or glees
 We could not sing, oh! queen of cheese.
 We'rt thou suspended from balloon,
 You'd cast a shade even at noon,
 Folks would think it was the moon
 About to fall and crush them soon.'''

# 12.5 Import the re module to use Python’s regular expression functions. Use the
# re.findall() to print all the words that begin with c.
import re

pattern = r'\b[Cc]\w*'
re.findall(pattern, mammoth)
print(re.findall(pattern, mammoth))

# 12.6 Find all four-letter words that begin with c.
pattern = r'\b[Cc]\w{3}\b'
re.findall(pattern, mammoth)
print(re.findall(pattern, mammoth))

# 12.7 Find all the words that end with r.
pattern = r'\b\w*r\b'
re.findall(pattern, mammoth)
print(re.findall(pattern, mammoth))

# 12.8 Find all words that contain exactly three vowels in a row.
pattern = r'\b\w*[aeuoiy]{3}[^aeuoiy\s]*\w*\b'
re.findall(pattern, mammoth)
print(re.findall(pattern, mammoth))

# 12.9 Use unhexlify to convert this hex string (combined from two strings to fit on a
# page) to a bytes variable called gif:
# '47494638396101000100800000000000ffffff21f9' +
# '0401000000002c000000000100010000020144003b'
import binascii

hexstr = '47494638396101000100800000000000ffffff21f9' + \
         '0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(hexstr)
len(gif)
print(len(gif))

# 12.10 The bytes in gif define a one-pixel transparent GIF file, one of the most com‐
# mon graphics file formats. A legal GIF starts with the ASCII characters GIF89a. Does
# gif match this?
gif[:6] == b'GIF89a'
print(gif[:6] == b'GIF89a')

# 12.11 The pixel width of a GIF is a 16-bit little-endian integer beginning at byte offset
# 6, and the height is the same size, starting at offset 8. Extract and print these values
# for gif. Are they both 1?
widht, height = struct.unpack('<HH', gif[6:10])
print(widht, height)
