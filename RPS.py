from random import randint
 
tools = ['rock', 'paper','scissors']
i = 0
my_score = 0
enemy_score = 0
name = input('enter your name: ')
while i < 5:
    x = randint(0,2)
    c = tools[x]
    play = input('1)rock \n2)paper \n3)scissors\n')
    if (play == '1'):
        play = tools[0]
    elif (play == '2'):
        play = tools[1]
    elif (play == '3'):
        play = tools[2]
    else:
        print('wrong number choose again..')
    if (play == c):
        print('\n Draw')
        print(name + '  ' + str(my_score) + ' : ' + str(enemy_score) + '   bot \n')
    elif(play == tools[0] and c == tools[1]) or (play == tools[1] and c == tools[2]) or (play == tools[2] and c == tools[0]):
        print('\n' + play + ' vs ' + c)
        enemy_score +=1
        print(name + '  ' + str(my_score) + ' : ' + str(enemy_score) + '   bot \n')
    elif(play == tools[0] and c == tools[2]) or (play == tools[1] and c == tools[0]) or (play == tools[2] and c == tools[1]):
            print('\n' + play + ' vs ' + c)
            my_score +=1
            print(name + '  ' + str(my_score) + ' : ' + str(enemy_score) + '   bot \n')
    if(my_score == 5):
        print('Congrats ' + name + ' you won!')
        i = 6
    elif(enemy_score == 5):
            print('Fuck you ' + name + ' the bot won')
            i = 6
