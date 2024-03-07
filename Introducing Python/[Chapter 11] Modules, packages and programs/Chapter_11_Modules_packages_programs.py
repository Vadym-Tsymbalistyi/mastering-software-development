import zoo

zoo.hours()

# 11.2. In the interactive interpreter, import the zoo module as menagerie and call its
# hours() function.
import zoo as menagerie

menagerie.hours()

# 11.3 Staying in the interpreter, import the hours() function from zoo directly and call
# it.
from zoo import hours

hours()

# 11.4 Import the hours() function as info and call it.
from zoo import hours as info

info()

# 11.5 Make a dictionary called plain with the key-value pairs 'a': 1, 'b': 2, and
# 'c': 3, and then print it.
plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

# 11.6 Make an OrderedDict called fancy from the same pairs listed in the previous
# question and print it. Did it print in the same order as plain?
from collections import OrderedDict

fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(fancy)

# 11.7 Make a defaultdict called dict_of_lists and pass it the argument list. Make
# the list dict_of_lists['a'] and append the value 'something for a' to it in one
# assignment. Print dict_of_lists['a']
from collections import defaultdict

dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('samething for a')
print(dict_of_lists['a'])
