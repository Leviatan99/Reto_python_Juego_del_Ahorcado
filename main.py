#Este es un programa para cumplir con el reto final del curso de python intermedio
import random
import os
import unidecode

def read_data():
    words = []
    with open('./data.txt','r',encoding='utf-8') as f:
        for line in f:
            words.append(line)
    new_words = [line[:-1] for line in words]

    return new_words


def read_introduction():
    introduction = open ('ahorcado3.txt','r')
    mensaje = introduction.read()
    introduction.close()
    return mensaje    


def select_word(data_set):
    return random.choice(data_set)


def normalize(data_Set):
    new_data_set = [unidecode.unidecode(word) for word in data_Set]
    return new_data_set


def upper_word(word_to_guess):
    word_upper = word_to_guess.upper()
    return word_upper


def word_slices(word_to_guess):
    if len(word_to_guess) > 4 :
        word_to_print_1 = word_to_guess[0]
        word_to_print_2 = word_to_guess[4]
        word_to_print_3 = word_to_guess[-1]

def win():
    winning_message = open ('win_1.txt','r')
    mensaje = winning_message.read()
    winning_message.close()
    return mensaje

def run():
    data_set = read_data()
    print(read_introduction())
    data_set = normalize(data_set)
    
    tuplas_list_data_Set = list(enumerate(data_set))
    tupla_word_to_guess = select_word(tuplas_list_data_Set)
    word_to_guess = tupla_word_to_guess[1]
    
    len_word_to_guess = len(word_to_guess)
    list_len_word_to_guess = list(len_word_to_guess*'_')
    print(list_len_word_to_guess)

    agregar_elemento = list_len_word_to_guess.insert(1,'hola')

    print(list_len_word_to_guess)


    print( upper_word( word_to_guess))

    print(tupla_word_to_guess)



    
if __name__ =='__main__':
    run()