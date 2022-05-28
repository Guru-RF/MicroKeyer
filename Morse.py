# setup encode and decode
encodings = {}
def encode(char):
    global encodings
    if char in encodings:
        return encodings[char]
    elif char.lower() in encodings:
        return encodings[char.lower()]
    else:
        return '#'

decodings = {}
def decode(char):
    global decodings
    if char in decodings:
        return decodings[char]
    else:
        return '#'

def MAP(pattern, letter):
    decodings[pattern] = letter
    encodings[letter] = pattern


MAP('.-', 'a');
MAP('-...', 'b');
MAP('-.-.', 'c');
MAP('-..', 'd');
MAP('.', 'e')
MAP('..-.', 'f');
MAP('--.', 'g');
MAP('....', 'h');
MAP('..', 'i');
MAP('.---', 'j')
MAP('-.-', 'k');
MAP('.-..', 'l');
MAP('--', 'm');
MAP('-.', 'n');
MAP('---', 'o')
MAP('.--.', 'p');
MAP('--.-', 'q');
MAP('.-.', 'r');
MAP('...', 's');
MAP('-', 't')
MAP('..-', 'u');
MAP('...-', 'v');
MAP('.--', 'w');
MAP('-..-', 'x');
MAP('-.--', 'y')
MAP('--..', 'z')

MAP('.----', '1');
MAP('..---', '2');
MAP('...--', '3');
MAP('....-', '4');
MAP('.....', '5')
MAP('-....', '6');
MAP('--...', '7');
MAP('---..', '8');
MAP('----.', '9');
MAP('-----', '0')

MAP('.-.-.-', '.')  # period
MAP('--..--', ',')  # comma
MAP('..--..', '?')  # question mark
MAP('-...-', '=')  # equals, also /BT separator
MAP('-....-', '-')  # hyphen
MAP('-..-.', '/')  # forward slash
MAP('.--.-.', '@')  # at sign

MAP('-.--.', '(')  # /KN over to named station
MAP('.-.-.', '+')  # /AR stop (end of message)
MAP('.-...', '&')  # /AS wait
MAP('...-.-', '|')  # /SK end of contact
MAP('...-.', '*')  # /SN understood

