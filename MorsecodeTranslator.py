letters = {
          'a': '.-',   'b': '-...', 'c': '-.-.', 'd': '-..',  'e': '.',    'f': '..-.',  'g': '--.',   'h': '....',
          'i': '..',   'j': '.---', 'k': '-.-',  'l': '.-..', 'm': '--',   'n': '-.',    'o': '---',   'p': '.--.',
          'q': '--.-', 'r': '.-.',  's': '...',  't': '-',    'u': '..-',  'v': '...-',  'w': '.--',   'x': '-..-',
          'y': '-.--', 'z': '--..', ' ': '|',    '1': '.----','2': '..---','3': '...--', '4': '....-', '5': '.....',
          '6': '-....','7': '--...','8': '---..','9': '----.','0': '-----','.': '.-.-.-','?': '..--..','!': '-.-.--',
          ',': '--..--'
          }

morse =   {
          '.-':    'a', '-...': 'b', '-.-.': 'c', '-..':   'd', '.':    'e', '..-.':  'f', '--.':   'g', '....':   'h',
          '..':    'i', '.---': 'j', '-.-':  'k', '.-..':  'l', '--':   'm', '-.':    'n', '---':   'o', '.--.':   'p',
          '--.-':  'q', '.-.':  'r', '...':  's', '-':     't', '..-':  'u', '.. -':  'v', '.--':   'w', '-..-':   'x',
          '-.--':  'y', '--..': 'z', '|':    ' ', '.----': '1', '..---':'2', '...--': '3','....-':  '4',  '.....': '5',
          '-....': '6','--...': '7', '---..':'8',  '----.':'9','-----': '0', '.-.-.-':'.', '..--..':'?',  '-.-.--':'!',
          '--..--':',',
          }

Morse = 0
Text = 0
morse_items_in_list = ()

def split(morse_user_input): 
    return [char for char in morse_user_input]

def Convert(string): 
    li = list(string.split(" ")) 
    return li

while Morse == 0 and Text == 0:  
    print("Gib \"morse\" ein um Text in Code um zu wandeln gib \"text\" ein um Code in Text zu wandeln.")
    choose = input(str(""))
    choose = choose.lower()
    
    if choose == str("morse"):
        Morse = Morse + 1

    elif choose == str("text"):
        Text = Text + 1
    
    else:
        print("Falsche angabe \n")
        


if Morse == 1: 
    print("Geben sie ihren Text ein!")
    morse_user_input = input(str(""))
    
    morse_user_input = morse_user_input.lower()
    
    needed_letters = {}
    for k,v in letters.items():
        for i in morse_user_input:
            if i==k:
                needed_letters[k] = v
            
            
    morse_count = 0
    morse_items_in_list = len(morse_user_input)
    
    while morse_items_in_list != morse_count:
        print(needed_letters[morse_user_input[morse_count]] + " ", end="")
        morse_count = morse_count + 1

if Text == 1:
    print("Geben sie ihren Code ein!")
    text_user_input = input(str(""))
    
    converted_text_user_input = (Convert(text_user_input))
    text_count = 0
    text_items_in_list = len(converted_text_user_input)
    
    while text_items_in_list > text_count:
        print(morse[converted_text_user_input[text_count]] + "", end="")
        text_count = text_count + 1