import pandas as pd
import numpy as np
import sys

def get_opposite_translation(current_letter):
    a = np.where(alphabets_df == current_letter)
    pos = np.concatenate((a[0],a[1]),axis=0)
    if IsMorse == True:
        pos[1] = 0
    else:
        pos[1] = 1
    return (np_alphabets[pos[0],pos[1]])

alphabets_df = pd.read_csv('alphabets_file.csv')
np_alphabets = alphabets_df.to_numpy()
output = ""
IsMorse = False

Morse_to_Text = str(input("Is the input Morse? The default is False. Answer with - Yes or No:\n")).lower()
if Morse_to_Text == "yes":
    IsMorse = True
elif Morse_to_Text == "no" or Morse_to_Text == "":
    IsMorse = False
else:
    print("wrong input")
    sys.exit()

user_input = str(input("Type in the sentence you want to translate:\n")).lower()

if IsMorse != True:
    for i in user_input:
            output = output + " " + str(get_opposite_translation(i)) 
if IsMorse == True:
    user_input = user_input.split(" ")
    print(user_input)
    for i in user_input:
            output = output + str(get_opposite_translation(i)) 

print(output)
