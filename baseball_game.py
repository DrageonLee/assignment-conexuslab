from random import randint

def generate_numbers():
    numbers = []
    i = 0
    while i < 3 :
        rand_number = randint(1,9)
        if rand_number not in numbers:
            numbers.append(rand_number)
            i+=1
        
    return numbers

print(generate_numbers())