def cipher(text, shift, mode=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift_alphabet = alphabet[shift:]+alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shift_alphabet + shift_alphabet.upper())
    cipher_text = text.translate(translation_table)
    print(cipher_text)
    
def encrypt(text, shift):
    cipher(text, shift, mode = True)
    
def decrypt(text, shift):
    cipher(text, -shift, mode=False)
    
encrypt("Hello World", 6)
decrypt("Nkrru Cuxrj", 6)
