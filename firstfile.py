# this is a comment
# default shortcut zum commenten/uncommenten ist <Ctrl + "/">
# (was auf deutschen Tastaturen nicht gut geht --> das "/" am Numpad funzt)

''' this kind of multi-line comment
should actually not be used (for normal comment-y type stuff) '''

""" use double quotes
instead """

print("hallo")

# seems like input() reads the typed-in stuff as a String
boolean = input("type something that will be evaluated:")

# and also seems like (non-empty) strings evaluate to True
if (boolean):
    print("input eval'd to True")

inlineIf = "condition true" if boolean == "False" else "condition false"
