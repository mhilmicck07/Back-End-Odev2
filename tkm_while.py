import random

score_user = 0 
score_cpu = 0

while True:

        secenek = random.choice(('tas','kagit','makas'))
        # print(secenek)

        user = input('Bir seçenek giriniz: ')

        
        if (user == 'makas' and secenek == 'makas') or (user == 'kagit' and secenek == 'kagit') or (user == 'tas' and secenek == 'tas'):
            print('Durum Berabere')
        elif (user == 'kagit' and secenek == 'makas') or (user == 'makas' and secenek == 'tas') or (user == 'tas' and secenek == 'kagit'):
            print('Computer Wins!')
            score_cpu += 1
            print(score_cpu)
            print(score_user)
        elif (user == 'makas' and secenek == 'kagit') or (user == 'tas' and secenek == 'makas') or (user == 'kagit' and secenek == 'tas'):
            print('User Wins!')
            score_user += 1
            print(score_cpu)
            print(score_user)
        else:
            print('I want to Play Game!')

        if score_cpu == 3 or score_user == 3:
            play_again = input('Yeni oyun? (e/h)')
            if play_again.lower() == 'e': 
                print('Game Starts Soon!')
                score_cpu = 0
                score_user = 0
            else:
                print('Game Over!')
                break

