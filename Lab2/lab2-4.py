'''
Encrypt a text file using the Ceaser cipher (shift 5).

1. Write the program to encrypt the text file (case insenstive) into cipher text
2. Write the program to decrypt the cipher text to plain text(normal text- case insensitive)

This program is for ENCRYPTING
'''

# Function to read input file from disk
def read_file(file_name):
    file = open(file_name,)
    file_content = file.read()
    file.close()
    return(file_content)

# Function to write new file to disk
def write_file(file_name, file_content):
    file = open(file_name, 'w')
    file.write(file_content)
    file.close()

# Function to do the encryption of text
def encrypt_string(input_file):
    new_string = ''
# Lets go over all characters from input file
    for char in input_file:
# Will convert all characters to ASCII code
        asc_char = ord(char)
# Check if the characters are in scope of alphabet
        if (    (asc_char >= 97 and asc_char <= 122)
            or  (asc_char >= 65 and asc_char <= 90)
        ):
# Will shift all the characters for 5 places if the are part of an alphabet
            new_asc_char = asc_char + 5
# Check if the characters did not fall out from alphabet scope, and if thay did, give those new value starting from beginnig
            if (    (new_asc_char >= 91 and new_asc_char <= 96)
                or  (new_asc_char >= 123)
            ):
                new_asc_char = new_asc_char - 26
# Convert the ASCII codes back to characters
            new_char = chr(new_asc_char)
# Build a string from the new characters
            new_string = new_string + new_char
        else:   # don't shift the characters if thay are not part of an alphabet
            new_asc_char = asc_char
            new_char = chr(new_asc_char)
            new_string = new_string + new_char
    return(new_string)



#############
# Work area #
#############

file_content = read_file(input('Enter decrypted file name : '))

encrypted_text = encrypt_string(file_content)

write_file(input('Enter new file name where encrypted content will be stored : '), encrypted_text)

print('Current file content is :\n',file_content)
print('New file content is :\n', encrypted_text)
