import string 


alphabet = list(string.ascii_lowercase)

def encode(message, shift):
    new_message = ""
    for letter in message:
        if letter in alphabet:
            index_position = alphabet.index(letter)
            new_position = (index_position + shift) % 26
            new_letter = alphabet[new_position]
            new_message += new_letter
        else:
            new_message += letter
    return new_message 

def decode(message, shift):
    new_message = ""
    for letter in message:
        if letter in alphabet:
            index_position = alphabet.index(letter)
            new_position = (index_position - shift) % 26
            new_letter = alphabet[new_position]
            new_message += new_letter
        else:
            new_message += letter
    return new_message 

picker = (input("Choose between decoder and encoder").lower())
message = list(input("This is the encoder please insert your message:").lower())
shift = int(input("This is the encoder please insert your shift:"))

result_encode = encode(message, shift)
result_decode = decode(message, shift)

if picker == "encoder": 
    print (result_encode)
elif picker == "decoder":
    print (result_decode)
else: 
    print ("You didn't choose encoder or decoder!")