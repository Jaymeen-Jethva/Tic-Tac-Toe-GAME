import numpy as np
# CREATING BASE 
base = np.ones((3,3),dtype=str)
for i in range(3):
    for j in range(3):
        base[i][j]='_'

# GAME LAYOUT & PLAYER NAME
print('\n\n\n')
print('#'*10,'\tT I C   T A C   T O E\t','#'*10,'\n','_'*50,'\n\n')
p1name = input('Player 1 Name : ')  # with O
p2name = input('Player 2 Name : ')  # with X
print(f'\n{p1name} is having "O" \n{p2name} is having "X"\n')

## WHAT TO INPUT KIND OF USER MANUAL FOR PLAYERS
print('Enter the 1 for first row in row section same way enter 2 for Second and 3 for Third')
print('Enter the 1 for first column in row section same way enter 2 for Second and 3 for Third\n')

# FUNCTION FOR TAKING THE INPUTS FROM THE USER
def inp():
    m=input('Enter the Row No. : ')
    n=input('Enter the Column No. : ')
    if not (m.isdigit() and n.isdigit()):
        print('\n\t*****\tERRORRRRR\t*****\nPlease Enter The Integer Value\n')
        return inp()
    elif m.isalpha() or n.isalpha():
        print('\n\t*****\tERRORRRRR\t*****\nPlease Enter The Integer Value\n')
        return inp()
    elif int(m) not in [1,2,3] or int(n) not in [1,2,3]:
        print('\n\t*****\tERRORRRRR\t*****\nPlease Enter The Value Between 1 to 3\n')
        return inp()
    else:
        return (int(m),int(n)) 

# OUT OF INDEX ERROR MESSAGE FUNCTION
def outOfIndex():
    print('\n\t*****\tERRORRRRR\t*****\nYou have already Entered the Value in that box\nPlease try again\n')


# TAKING 4 INPUTS THEN WE WILL START CHECKING FOR WINNER
c=0
choice=[]
while c<4:
    print(f'{p1name} Enter the position of cell')
    t = inp()
    while t in choice:
        outOfIndex()
        t = inp()
    choice.append(t)
    m,n=t
    base[m-1][n-1] = 'O'
    print('\n',base,'\n\n')
    c+=1

    print(f'{p2name} Enter the position of cell')
    t = inp()
    while t in choice:
        outOfIndex()
        t = inp()
    choice.append(t)
    m,n=t
    base[m-1][n-1] = 'X'
    print('\n',base,'\n\n')
    c+=1

## THE MAIN GAME FUNCTION STARTS
def gamecheck(arr):
    # FOR DIAGONALS
    if arr[0][0] == 'O' and arr[1][1] == 'O' and arr[2][2] == 'O':
        return 'O'
    elif arr[0][0] == 'X' and arr[1][1] == 'X' and arr[2][2] == 'X':
        return 'X'
    elif arr[0][2] == 'O' and arr[1][1] == 'O' and arr[2][0] == 'O':
        return 'O'         
    elif arr[0][2] == 'X' and arr[1][1] == 'X' and arr[2][0] == 'X':
        return 'X'
    # FOR ROWS
    for i in range(3):
        cntO=0
        cntX=0
        for j in range(3):
            if arr[i][j] == 'O':
                cntO+=1
            elif arr[i][j] == 'X':
                cntX+=1
        if cntO == 3:
            return 'O'
        elif cntX == 3:
            return 'X'
    # FOR COLUMN
    for i in range(3):
        cntO=0
        cntX=0
        for j in range(3):
            if arr[j][i] == 'O':
                cntO+=1
            elif arr[j][i] == 'X':
                cntX+=1
        if cntO == 3:
            return 'O'
        elif cntX == 3:
            return 'X'
    return None    
## THE MAIN GAME FUNCTION ENDS

## RUNNING THE GAME FUNCTION UNTILL SOMEONE WINS THE GAME
winner='Tie'
win = True
while win and c<9:
    if gamecheck(base) == 'O':
        winner = p1name
        break
    elif gamecheck(base) == 'X':
        winner = p2name
        break
    print(f'{p1name} Enter the position of cell')
    t = inp()
    while t in choice:
        outOfIndex()
        t = inp()
    choice.append(t)
    m,n=t
    base[m-1][n-1] = 'O'
    print('\n',base,'\n\n')
    c+=1

    if c == 9:         #############################################   BREAK
        break

    if gamecheck(base) == 'O':
        winner = p1name
        break
    elif gamecheck(base) == 'X':
        winner = p2name
        break
    print(f'{p2name} Enter the position of cell')
    t = inp()
    while t in choice:
        outOfIndex()
        t = inp()
    choice.append(t)
    m,n=t
    base[m-1][n-1] = 'X'
    print('\n',base,'\n\n')
    c+=1

## PRINTING THE WINNER
print()
print('_'*50)
if winner == 'Tie':
    print('\n\n','*'*10,'THIS GAME IS TIE','*'*10)
else:
    print('\n\n','*'*10,f'### CONGRATULATIONS ###','*'*10)
    print('\n','*'*10,f'{winner} IS THE WINNER','*'*10)
print('\n','_'*50)
