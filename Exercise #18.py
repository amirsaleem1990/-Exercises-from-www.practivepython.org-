# Exercise #18
'''
Create a program that will play the “cows and bulls” game with the user. The game works
like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every
digit that the user guessed correctly in the correct place, they have a “cow”. For every
digit the user guessed correctly in the wrong place is a “bull.” Every time the user
makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the
correct number, the game is over. Keep track of the number of guesses the user makes
throughout teh game and tell the user at the end.
Say the number generated by the computer is 1038. An example interaction could look like
this:
Welcome to the Cows and Bulls Game! 
Enter a number: 
>>> 1234
2 cows, 0 bulls
>>> 1256
1 cow, 1 bull
Until the user guesses the number.
'''
def cows_and_bulls():
    from random import randint as r
    a = [str(r(0,9)) for i in range(4)]
    qq = a[:]; z = ['' for i in range(4)]; b = list(); c = list(); count = 0
    print('Welcome to cows and bulls Game!')
    while qq != z:
        d = input('\nEnter a 4 digit number: \t'); count += 1
        for i in range(4):
            if d[i] in qq:
                if d[i] == qq[i]: c.append('cow'); qq[i] = ''
            else: b.append('bull')
        print(str(len(c))+' cow,' + str(len(b)) + ' bull')
    print('\n[Congragulation! you guessed the correct number in ' + str(count) + ' turns')
    aa = input('\nAre you want to play this game once more? \n[y/n]')
    if aa.lower() == 'y': print(cows_and_bulls())
    else: print('\nTake care.. bye bye'); return ' '
    

print(cows_and_bulls())
            
            
    
    
