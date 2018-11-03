# tuples are immutable but not constant
# If I understand those terms correctly
x, y, z = 10, 20, 30
tupleExp = (x, y, z)
print(tupleExp)

# not allowed:
# tupleExp[0] = y;

tupleExp = ("ten", "twenty", "thirty")
print(tupleExp)

# construction happens by value, not by reference
tupleExp = (x, y, z)
x = 40
print(tupleExp)


# list items can be of various types
listExp = [1, 'a', "ficken", 2.0]

# and so can dictionary-elements as well as keys:
dictEx1 = {"key1": "value", "key2": 0, 3: "item3"}
dictEx2 = dict(key1 = "value", key2 = 0)
dictEx2['key2'] = dictEx2['key2'] + 1