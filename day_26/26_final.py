import pandas

data = pandas.read_csv('./day_26/nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(nato_dict)

word = input("Enter a word: ").upper()
result = [nato_dict[letter] for letter in word]
print(result)
# word = Love
# ['Lima', 'Oscar', 'Victor', 'Echo']