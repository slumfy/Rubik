import sys
import move

def shuffle(rubik, inst):
    for idx in range(len(inst)):
        if inst[idx][0] == "F":
            if len(inst[idx]) == 1:
                move.mfront(rubik,0)
            elif inst[idx][1] == "'":
                move.mfront(rubik, 1)
            elif inst[idx][1] == "2":
                move.mfront(rubik, 2)
        if inst[idx][0] == "R":
            if len(inst[idx]) == 1:
                move.mright(rubik,0)
            elif inst[idx][1] == "'":
                move.mright(rubik, 1)
            elif inst[idx][1] == "2":
                move.mright(rubik, 2)
        if inst[idx][0] == "U":
            if len(inst[idx]) == 1:
                move.mup(rubik,0)
            elif inst[idx][1] == "'":
                move.mup(rubik, 1)
            elif inst[idx][1] == "2":
                move.mup(rubik, 2)
        if inst[idx][0] == "B":
            if len(inst[idx]) == 1:
                move.mback(rubik,0)
            elif inst[idx][1] == "'":
                move.mback(rubik, 1)
            elif inst[idx][1] == "2":
                move.mback(rubik, 2)
        if inst[idx][0] == "L":
            if len(inst[idx]) == 1:
                move.mleft(rubik,0)
            elif inst[idx][1] == "'":
                move.mleft(rubik, 1)
            elif inst[idx][1] == "2":
                move.mleft(rubik, 2)
        if inst[idx][0] == "D":
            if len(inst[idx]) == 1:
                move.mdown(rubik,0)
            elif inst[idx][1] == "'":
                move.mdown(rubik, 1)
            elif inst[idx][1] == "2":
                move.mdown(rubik, 2)