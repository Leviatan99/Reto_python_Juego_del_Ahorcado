#Este es un programa para cumplir con el reto final del curso de python interm
import random
import os
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
    print(mensaje)
    introduction.close()    


def select_word(data_set):
    return random.choice(data_set)
    

def run():
    data_set = read_data()
    #print(data_set)

    print(read_introduction())

    word_to_guess = select_word(data_set)
    palabra = random.choice(word_to_guess)
    
    print(word_to_guess)
    print(palabra)
    
if __name__ =='__main__':
    run()