# Mail Merge Project


#TODO: Create a letter using starting_letter.txt 
import os
print(os.getcwd())


with open('./day_24/Mail_project/Input/Letter/starting_letter.txt', 'r') as letter:
    texts = letter.read()
    lines_left = texts.split('[name]')
    dear = lines_left[0]
    behind = lines_left[1]

with open('./day_24/Mail_project/Input/Names/invited_names.txt', 'r') as names:
    contents = names.read() 
    #for each name in invited_names.txt
    will_invite_names = contents.split('\n')

for name in will_invite_names:
    #Replace the [name] placeholder with the actual name.
    changed_name = texts.replace("[name]", name)

    #Save the letters in the folder "ReadyToSend".
    file_name = "letter_for_" + name + "." + "txt"
    result = './day_24/Mail_project/Output/ReadyToSend/' + file_name
    with open(result, 'x') as new_file:
        new_file.write(changed_name + behind)
