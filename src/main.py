from lexical import Lexical

txt = input('enter text...')
lexical = Lexical(txt)

print("Verbs in text: ", lexical.get_verbs())
print("Names: ", lexical.get_pople_names())