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

def get_numbers():
    number = input("숫자를 입력해 주세요 : ")
    num_list = []
    if len(set(number)) != 3 or len(number) !=3:
        print("세가지 숫자를 각각 다르게 다시 입력해 주세요! ")
        return get_numbers()
    for i in range(3):
        num_list.append(int(number[i]))
    
    return num_list

print(get_numbers())