'''
This program is intented to solve the puzzle, which i met in SWKOTOR2:The Sith Lords
The puzzle is to match top and bottom blocks, each consisting of 8 character,2*4 rows in only 3 rotations
Possible rotations are clockwise and counter-clockwise for left,center and right blocks
Example top block:
3E1D
L7T3
Example bottom block: - to be matched
1E7T
3L3D
Didn't want to bother with math, so random module does the trick.
Code written by Delneg, 11.01.2016 ~15 pm
I was bored =)
'''
import random
def rotate_left_clockwise(block):
    new = [['','','',''],['','','','']]
    new[0][0]=block[1][0]
    new[0][1]=block[0][0]
    new[0][2]=block[0][2]
    new[0][3]=block[0][3]
    new[1][0]=block[1][1]
    new[1][1]=block[0][1]
    new[1][2]=block[1][2]
    new[1][3]=block[1][3]
    return new
def rotate_left_coclockwise(block):
    new = [['','','',''],['','','','']]
    new[0][0]=block[0][1]
    new[0][1]=block[1][1]
    new[0][2]=block[0][2]
    new[0][3]=block[0][3]
    new[1][0]=block[0][0]
    new[1][1]=block[1][0]
    new[1][2]=block[1][2]
    new[1][3]=block[1][3]
    return new
def rotate_center_clockwise(block):
    new = [['','','',''],['','','','']]
    new[0][0]=block[0][0]
    new[0][1]=block[1][1]
    new[0][2]=block[0][1]
    new[0][3]=block[0][3]
    new[1][0]=block[1][0]
    new[1][1]=block[1][2]
    new[1][2]=block[0][2]
    new[1][3]=block[1][3]
    return new
def rotate_center_coclockwise(block):
    new = [['','','',''],['','','','']]
    new[0][0]=block[0][0]
    new[0][1]=block[0][2]
    new[0][2]=block[1][2]
    new[0][3]=block[0][3]
    new[1][0]=block[1][0]
    new[1][1]=block[0][1]
    new[1][2]=block[1][1]
    new[1][3]=block[1][3]
    return new
def rotate_right_clockwise(block):
    new = [['','','',''],['','','','']]
    new[0][0]=block[0][0]
    new[0][1]=block[0][1]
    new[0][2]=block[1][2]
    new[0][3]=block[0][2]
    new[1][0]=block[1][0]
    new[1][1]=block[1][1]
    new[1][2]=block[1][3]
    new[1][3]=block[0][3]
    return new
def rotate_right_coclockwise(block):
    new = [['','','',''],['','','','']]
    new[0][0]=block[0][0]
    new[0][1]=block[0][1]
    new[0][2]=block[0][3]
    new[0][3]=block[1][3]
    new[1][0]=block[1][0]
    new[1][1]=block[1][1]
    new[1][2]=block[0][2]
    new[1][3]=block[1][2]
    return new
def apply_rotation(number,block):
    if number==0:
        return rotate_left_clockwise(block)
    elif number==1:
        return rotate_left_coclockwise(block)
    elif number==2:
        return rotate_center_clockwise(block)
    elif number==3:
        return rotate_center_coclockwise(block)
    elif number==4:
        return rotate_right_clockwise(block)
    elif number==5:
        return rotate_right_coclockwise(block)
def describe_rotation(number):
    if number==0:
        return 'Left-most block clockwise'
    elif number==1:
        return 'Left-most block counter-clockwise'
    elif number==2:
        return 'Center block clockwise'
    elif number==3:
        return 'Center block counter-clockwise'
    elif number==4:
        return 'Right-most block clockwise'
    elif number==5:
        return 'Right-most block counter-clockwise'
def print_block(block):
    print(''.join(block[0])+'\n'+''.join(block[1]))
def loop_throught_rotations(try_limit,income,outcome):
    for i in range(100000):
        print 'Sequence number',i+1
        this_rotatable = list(income)
        rotations = []
        for j in range(try_limit):
            rotation = random.randrange(0,6)
            rotations.append(rotation)
            print 'Rotation number',j+1,' applying '+describe_rotation(rotation)
            print '----'
            print_block(this_rotatable)
            this_rotatable=apply_rotation(rotation,this_rotatable)
            print '----'
            print_block(this_rotatable)
            print '----'
            if this_rotatable==outcome:
                print 'Success! Done in '+str(i+1)+' tries'
                print 'Apply rotations:\n'
                for p in rotations:
                    print describe_rotation(p)
                return

if __name__=='__main__':
    income =   [['3','E','1','D'],['L','7','T','3']]
    outcome =  [['1','E','7','T'],['3','L','3','D']]
    try_limit=3
    loop_throught_rotations(try_limit,income,outcome)
