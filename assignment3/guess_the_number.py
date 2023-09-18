min_num = 0
max_num = 1001

while True:
    guess = int((max_num + min_num) / 2)
    print(guess, flush=True)
    reponse = input()
    if reponse == 'correct':
        break
    if reponse == 'higher':
        min_num = guess
    if reponse == 'lower':
        max_num = guess


