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

def judgement(number, answer) :
    strike = 0
    ball = 0
    i = 0

    while i < len(number):
        if number[i] == answer[i] :
            strike += 1
        elif number[i] in answer :
            ball += 1
        i+=1

    if strike != False and ball != False :
        return f'{strike} strike, {ball} ball'
    elif strike != False:
        return f'{strike} strike'
    elif ball !=  False:
        return f'{ball} ball'
    else : 
        return '낫싱'

def baseball_game():
    number = generate_numbers()
    
    while True :
        game = judgement(number, get_numbers())
        print(game)
        if game == '3 strike' :
            print('3개의 숫자를 모두 맞추셨습니다! 게임 종료')
            break

    againOrNot = int(input('게임을 새로 시작하려면1, 종료하려면 2를 입력하세요.'))
    if againOrNot == 1 :
        return baseball_game()
    elif againOrNot == 2 :
        return '게임 종료. 안녕히 가세요.'
    else :
        return againOrNot

print(baseball_game())