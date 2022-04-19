import argparse


def delta_small(c):
    return ord(c) - ord('a')


def delta_Big(c):
    return ord(c) - ord('A')

def caesar_cipher_encryption(fin, shift):
    fout = ''
    for symbol in fin:
        if 'a' <= symbol <= 'z':
            fout += chr(ord('a') + (delta_small(symbol) + shift) % 26)
        elif 'A' <= symbol <= 'Z':
            fout += chr(65 + (delta_Big(symbol) + shift) % 26)
        else:
            fout += symbol
    return fout


def caesar_cipher_decryption(fin, shift):
    fout = ''
    for symbol in fin:
        if 'a' <= symbol <= 'z':
            fout += chr(97 + (delta_small(symbol) - shift) % 26)
        elif 'A' <= symbol <= 'Z':
            fout += chr(65 + (delta_Big(symbol) - shift) % 26)
        else:
            fout += symbol
    return fout


def Vigenere_cipher_encryption(fin, key_word):
    key_word = key_word.lower()
    index_letter = 0
    fout = ''
    for symbol in fin:
        if 'a' <= symbol <= 'z':
            fout += chr(97 + (delta_small(symbol) + delta_small(key_word[index_letter])) % 26)
        elif 'A' <= symbol <= 'Z':
            fout += chr(65 + (delta_Big(symbol) + delta_small(key_word[index_letter])) % 26)
        else:
            fout += symbol
        index_letter = (index_letter + 1) % (len(key_word) - 1)
    return fout


def Vigenere_cipher_decryption(fin, key_word):
    key_word = key_word.lower()
    index_letter = 0
    fout = ''
    for symbol in fin:
        if 'a' <= symbol <= 'z':
            fout += chr(97 + (delta_small(symbol) - delta_small(key_word[index_letter])) % 26)
        elif 'A' <= symbol <= 'Z':
            fout += chr(65 + (delta_Big(symbol) - delta_small(key_word[index_letter])) % 26)
        else:
            fout += symbol
        index_letter = (index_letter + 1) % (len(key_word) - 1)
    return fout


def Vername_cipher_encryption(fin, fkey):
    fout = ''
    if len(fin) != len(fkey):
        raise ValueError("Тексты должны быть одной длины!")
    else:
        for i in range(len(fin) - 1):
            fout += chr(32 + (ord(fin[i]) ^ ord(fkey[i])))
        return fout


def Vername_ciphe_decryptione(fin, fkey):
    fout = ''
    if len(fin) != len(fkey):
        raise ValueError("Тексты должны быть одной длины!")
    else:
        for i in range(len(fin) - 1):
            fout += chr(((ord(fin[i]) - 32) ^ ord(fkey[i])))
        return fout


def frequency_analysis(fin):
    best = ''
    best_diff = -1
    ideal_frequency = [0.817, 0.149, 0.278, 0.425, 1.27, 0.223, 0.202, 0.609, 0.697, 0.015, 0.077, 0.403, 0.241, 0.675,
                       0.751, 0.193, 0.01, 0.599, 0.633, 0.906, 0.276, 0.098, 0.236, 0.015, 0.197, 0.0005]
    arr = [0] * 26
    for key in range(26):
        new_message = caesar_cipher_decryption(fin, key)
        for i in range(len(new_message)):
            if 'a' <= new_message[i] <= 'z' or 'A' <= new_message[i] <= 'Z':
                letter_now = new_message[i].lower()
                arr[delta_small(letter_now)] += 1
        for i in range(26):
            arr[i] = arr[i] / len(new_message)
        diff = 0
        for i in range(26):
            diff += (arr[i] - ideal_frequency[i]) ** 2
        if best_diff < 0 or best_diff > diff:
            best = new_message
            best_diff = diff
    return best

    for symbol in fin_new:
        if 'a' <= symbol <= 'z':
            arr[ord(symbol) - 97] += 1
    max_index = 0
    for i in range(26):
        if arr[i] < arr[max_index]:
            max_index = i
    key = abs(max_index + 97 - 101) % 26
    return caesar_cipher_decryption(fin, key)


parser = argparse.ArgumentParser(description="wooow")
parser.add_argument('action', type=str)
parser.add_argument('algorithm', type=str)
parser.add_argument('-k', '--key', type=str)
parser.add_argument('fin', type=str)
parser.add_argument('fout', type=str)
args = parser.parse_args()
if args.action == 'encode':
    if args.algorithm == 'caesar':
        file_in = open(args.fin)
        file_to_str = file_in.read()
        shift = int(args.key)
        file_out = open(args.fout, 'w')
        file_out.write(caesar_cipher_encryption(file_to_str, shift))
        file_in.close()
        file_out.close()
    elif args.algorithm == 'Vigenere':
        file_in = open(args.fin)
        file_to_str = file_in.read()
        file_key = open(args.key)
        key_to_str = file_key.read()
        file_out = open(args.fout, 'w')
        print(key_to_str, len(key_to_str))
        file_out.write(Vigenere_cipher_encryption(file_to_str, key_to_str))
        file_in.close()
        file_out.close()
        file_key.close()
    else:
        file_in_1 = open(args.fin)
        file_to_str_1 = file_in_1.read()
        file_in_2 = open(args.key)
        file_to_str_2 = file_in_2.read()
        file_out = open(args.fout, 'w')
        file_out.write(Vername_cipher_encryption(file_to_str_1, file_to_str_2))
        file_in_1.close()
        file_in_2.close()
        file_out.close()
else:
    if args.algorithm == 'caesar':
        file_in = open(args.fin)
        file_to_str = file_in.read()
        shift = int(args.key)
        file_out = open(args.fout, 'w')
        file_out.write(caesar_cipher_decryption(file_to_str, shift))
        file_in.close()
        file_out.close()
    elif args.algorithm == 'Vigenere':
        file_in = open(args.fin)
        file_to_str = file_in.read()
        file_key = open(args.key)
        key_to_str = file_key.read()
        file_out = open(args.fout, 'w')
        file_out.write(Vigenere_cipher_decryption(file_to_str, key_to_str))
        file_in.close()
        file_out.close()
        file_key.close()
    elif args.algorithm == 'Vername':
        file_in_1 = open(args.fin)
        file_to_str_1 = file_in_1.read()
        file_in_2 = open(args.key)
        file_to_str_2 = file_in_2.read()
        file_out = open(args.fout, 'w')
        file_out.write(Vername_ciphe_decryptione(file_to_str_1, file_to_str_2))
        file_in_1.close()
        file_in_2.close()
        file_out.close()
    else:
        file_in = open(args.fin)
        file_to_str = file_in.read()
        file_out = open(args.fout, 'w')
        file_out.write(frequency_analysis(file_to_str))
        file_in.close()
        file_out.close()

