from art import logo

print(logo)

dic = { 'A' : '.-',
	'B' : '-...',
	'C' : '-.-.',
	'D'  : '-..',
	'E'    : '.',
	'F' : '..-.',
	'G'  : '--.',
	'H' : '....',
	'I'   : '..',
	'J' : '.---',
    'K'  : '-.-',
	'L' : '.-..',
	'M'   : '--',
	'N'   : '-.',
	'O'  : '---',
	'P' : '.--.',
	'Q' : '--.-',
	'R'  : '.-.',
	'S'  : '...',
	'T'    : '-',
	'U'  : '..-',
	'V' : '...-',
	'W'  : '.--',
	'X' : '-..-',
	'Y' : '-.--',
	'Z' : '--..' }

is_continue = True

def MorseConverter(word):
    morse_convert = ''
    for letter in word:
        try:
            morse_convert += dic[letter] + ' '
        except:
            morse_convert += ''
    return print(f"Your result is : {morse_convert}")

while is_continue:
    word = input('Type your word : ').upper()
    MorseConverter(word)

    again_check = input('\nDo you want to do it again?\nType "y" if yes, other keys if no. ')
    print('\n')
    if again_check != 'y':
        print("Good Bye!")
        is_continue = False