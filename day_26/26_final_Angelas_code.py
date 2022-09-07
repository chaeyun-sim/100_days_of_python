import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
ouput_list = [phonetic_dict[letter] for letter in word]
print(ouput_list)