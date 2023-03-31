#!/usr/bin/env python
# coding: utf-8

# In[15]:


'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''


# In[17]:


def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #set parameters
    letter_shift = ""
    letter = str(letter)
    shift = int(shift)
    
    if 65 < ord(letter) > 90:
        underscore = "_"
        letter_shift = letter_shift + underscore
    
    elif ord(letter) == 32:
        underscore = "_"
        letter_shift = letter_shift + underscore
    
    elif 65 <= ord(letter) <= 90:
        alpha = ((ord(letter) - ord("A")) + shift)% 26
        omega = chr(alpha + ord("A"))
        letter_shift = letter_shift + omega
    
    else:
        pass
    
    return letter_shift 

shift_letter("Z", 1)


# In[18]:


#CAESAR CIPHER
def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    caesar = ""
    

    # convert message to unicode equivalent, shift, and then convert back to message
    for i in range(len(message)):
        character = message[i]
        if character == " ":
            character.replace(" ", "")
            caesar += character
        # since letters are all uppercase, we are only working with unicode from 65-90 
        elif character.isupper():
            caesar += chr((ord(character) + shift-65) % 26 + 65)

    return (caesar)

caesar_cipher("ATTACK AT DAWN BABY", 3)


# In[15]:


#SHIFT BY LETTER
def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #Setting parameters
    kyrie = ""
    letter = str(letter)
    letter_shift = str(letter_shift)
    
    if letter.isupper() and letter_shift.isupper():
        if 65 < ord(letter) > 90:
            underscore = "_"
            kyrie = kyrie + underscore

        elif ord(letter) == 32:
            underscore = "_"
            kyrie = kyrie + underscore

        elif 65 <= ord(letter) <= 90 and ord(letter_shift) != 32:
            alpha = ((ord(letter) - ord("A")) + (ord(letter_shift) - 65)) % 26
            omega = chr(alpha + ord("A"))
            kyrie = kyrie + omega

        else:
            pass
    else:
        kyrie = "error"
        
    return kyrie


shift_by_letter("B", "Z")


# In[16]:


#VIGENERE CIPHER
def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    vigenere = ''
    
    # check if length of key is same length or shorter than message
    if len(key) <= len (message) and key.isupper():
        #repeat keyphrase until matches length of message
        repeats = len(message) // len(key) + 1
        key_repeat = ((key*repeats)[:len(message)])
        
        #convert letters in message to number values
        for i in range(len(message)):
            character = message[i]
            #take care of spaces in message
            if character == " ":
                character.replace (" ", "")
                vigenere += character
            elif character.isupper():
                character_key = key_repeat[i]
                shift = ord(character_key[0]) - ord("A")
                #apply cipher
                vigenere += chr((ord(character) + shift - 65) % 26 + 65)
                
    elif len(key) > len(message):
        vigenere = "Key should be the same length or shorter than the message!"
    elif key.islower():
        vigenere = "Key should be uppercase!"
    
    
    return vigenere

vigenere_cipher("LONGTEXTER", "KEY")


# In[ ]:





# In[ ]:




