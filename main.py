"""
Quick documentation
AES -   XOR on each state byte and round key byte
        for each round (defined by key)
            change each bate with another from lookup table
            shift rows by it's number
            multiply each column linearly
        repeat all till last round
        do steps "for each round" without multiplication

Blowfish -  Algorithm splits the 32-bit input into four eight-bit quarters, and uses the quarters as input to the S-boxes
            The S-boxes accept 8-bit input and produce 32-bit output
            The outputs are added modulo 2^32 and XORed to produce the final 32-bit output

DES -   First text is separated in 64 bit block (for making it easier for machines to encript it)
        Algorithm with 16 cycles works on two 32 bit sized sides of block and does the Feistel's functions on them,
        then two parts are combined in 64 bit block
        Lastly makes final permutation

RSA -

DSA - Validates hash object with public key and signature (made out of hash object + private key)


sources:
https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
https://pypi.org/project/des/
https://pycryptodome.readthedocs.io/en/latest/src/cipher/blowfish.html

# pip install pycryptodome
# pip install des
# pip install rsa
"""

__author__ = "Kamil Skrzypkowski, Andrzej Mrozik"

from AES import *
from DES import *
from BlowFish import *
from RSA import *
from DSA import *


def ask_for_data(key_bit_size=8):
    """
    Gathers data from user and pass them to factory \n
    INPUT - <int> (default = 8) encoding function key bit size\n
    RETURN - <bytearray> key and <bytes> message
    """
    while True:
        print("Tell me the ", key_bit_size, "-bit key")
        key = str(input(">"))
        if len(key) < key_bit_size:
            print("The key is to short")
            print()

        elif len(key) > key_bit_size:
            print("The key is too long")
            print()

        else:
            break

    while True:
        print("Tell me your message")
        message = str(input(">"))

        if len(message) < 1:
            print("There is no message to encrypt")
            print()
        else:
            break

    key, message = key_n_message_factory(key, message)
    return key, message


def key_n_message_factory(key, message):
    """
    Factory that takes key and message and converts them into <byte> and <bytearray> \n
    INPUTS - <str> key, <str> message
    RETURNS - <bytearray> key, <bytes> message
    """
    key_bytearray = bytearray()
    key_bytearray.extend(map(ord, key))

    message_bytes = bytes(message, 'utf-8')

    return key_bytearray, message_bytes


def message_back_to_string(message):
    """
    Factory that converts message back to strings \n
    INPUTS - <bytes> message
    RETURNS - <str> message
    """
    message = str(message)
    message = message[2:-1]

    return message


def ask_for_data_asy():
    """
    Functiona that asks for data used by asymetric algorythms
    INPUTS - none
    RETURNS - <str> message
    """
    print("Tell me you's message")
    message = input(">")
    return message


if __name__ == '__main__':

    while True:
        print("What type of cipher do you want? \n"
              "1.Symetric\n"
              "2.Asymetric \n"
              "0.Exit")
        console_in = input(">")

        # Symetric
        if console_in == "1" or console_in == "Symetric" or console_in == "s":
            print("What cipher function you want to use? \n"
                  "1.DES \n"
                  "2.Blowfish \n"
                  "3.AES \n"
                  "0.Exit")
            console_in = input(">")

            if console_in == "1" or console_in == "DES" or console_in == "des":

                # DES
                key, message = ask_for_data()
                szyfr_des = DES_encode(key, message)
                print("Zaszyfrowana wiadomosc: ")
                print(szyfr_des)
                message = DES_decode(key, szyfr_des)
                print("Odszyfrowana wiadomosc: " + message_back_to_string(message))
                print()

            elif console_in == "2" or console_in == "BlowFish" or console_in == "Blowfish" or console_in == "blowfish":

                # BlowFish
                key, message = ask_for_data()
                szyfr_bf = Bf_encode(key, message)
                print("Zaszyfrowana wiadomosc: ")
                print(szyfr_bf)
                message = Bf_decode(key, szyfr_bf)
                print("Odszyfrowana wiadomosc: " + message_back_to_string(message))
                print()

            elif console_in == "3" or console_in == "AES" or console_in == "aes":

                # AES
                key, message = ask_for_data(16)
                nonce, szyfr_aes = AES_encode(key, message)
                print("Zaszyfrowana wiadomosc: ")
                print(szyfr_aes)
                message = AES_decode(key, nonce, szyfr_aes)
                print("Odszyfrowana wiadomosc: " + message_back_to_string(message))
                print()

        # Asymetric
        elif console_in == "2" or console_in == "Asymetric" or console_in == "a":
            print("What cipher function you want to use? \n"
                  "1.RSA \n"
                  "2.DSA")
            console_in = input(">")

            if console_in == "1" or console_in == "RSA" or console_in == "rsa":
                print("RSA")
                rsa = RSA()

                message = ask_for_data_asy()

                encoded = rsa.encrypt(message)
                print("Message encoded", encoded)

                decoded = rsa.decrypt(encoded)
                print("Message decoded: ", decoded)

            elif console_in == "2" or console_in == "DSA" or console_in == "dsa":
                print("DSA")
                message = ask_for_data_asy()

                dsa = DSA(message)

                signature = dsa.sign()
                verify(dsa.get_public_key(), dsa.get_hash_object(), signature)

        # Exiting
        elif console_in == "0" or console_in == "Exit" or console_in == "exit" \
                or console_in == "EXIT" or console_in == "e":
            break

        else:
            print("Nie ma takiej opcji")
