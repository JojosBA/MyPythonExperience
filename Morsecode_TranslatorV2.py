#The Code is not finished and doesnt worke yet

import pandas as pd
import numpy as np

alphabets_df = pd.read_csv('alphabets_file.csv')
np_alphabets = alphabets_df.to_numpy()

def get_opposite_translation(current_letter):
    a = np.where(alphabets_df == current_letter)
    pos = np.concatenate((a[0],a[1]),axis=0)
    if pos[1] == 1:
        pos[1] = 0
    else:
        pos[1] = 1
    return (np_alphabets[pos[0],pos[1]])

output = ""
user_input = "Test sentence".lower()
for i in user_input:
    output = output +" "+ str(get_opposite_translation(i)) 
print(output)
