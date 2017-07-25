my_dict = {'a': 2, 3: ['x', 'y'], 'joe': 'smith'}

dict_value_view = my_dict.values()
print(dict_value_view, type(dict_value_view))   # view & view type

for value in dict_value_view:                  # view iteration
    print(value)

my_dict['new key'] = 'new value'
print(dict_value_view)                  # view updated

dict_key_view = my_dict.keys()
print(dict_key_view)

# membership test; count words in a string
sentence = "to be or not to be"
words = sentence.split()            # returns a list
print(type(words))

word_count = {}
"""
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# print(word_count)

print(len(word_count))

same as above, but using exceptions
for word in words:
    try:
        word_count[word] += 1
    except KeyError:
        word_count[word] = 1
print(word_count)
"""
# same as above, but get method
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

