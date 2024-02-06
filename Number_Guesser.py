import random

def main():

    again = input('If you want to start press ENTER')
    while again == '':
        number = random.randint(0, 100)
        answer = int(input('Guess the number ? it is between 0 and 100'))
        score = 1
        while number != answer:
            if number > answer:
                print('The number is higher.')
            else:
                print('The number is lower')
            answer = int(input('tray again > '))
            score += 1
        print(f'Correct, the number is {number}.')
        if score == 1:
            print(f'It took you {score} try.')
        else:
            print(f'It took you {score} tries.')
        again = input('If you want to play again press ENTER. Else typ EXIT.')
        if again != '':
            break


if __name__ == '__main__':
    try:
        while main():
            pass
    except KeyboardInterrupt:
        exit()