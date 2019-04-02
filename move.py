import utils

# MOUVEMENT FRONT
def front(rubik):
    utils.swap(rubik, [17,45,27,6])
    utils.swap(rubik, [14,46,30,7])
    utils.swap(rubik, [11,47,33,8])
    utils.swap(rubik, [24,26,20,18])
    utils.swap(rubik, [22,25,23,19])

def front_rev(rubik):
    utils.swap(rubik, [6,27,45,17])
    utils.swap(rubik, [7,30,46,14])
    utils.swap(rubik, [8,33,47,11])
    utils.swap(rubik, [18,20,26,24])
    utils.swap(rubik, [19,23,25,22])

def front_double(rubik):
    i = 0
    while i < 2:
        front(rubik)
        i += 1

# MOUVEMENT BACK
def back(rubik):
    utils.swap(rubik, [15,51,29,0])
    utils.swap(rubik, [12,52,32,1])
    utils.swap(rubik, [9,53,35,2])
    utils.swap(rubik, [42,44,38,36])
    utils.swap(rubik, [40,43,41,37])

def back_rev(rubik):
    utils.swap(rubik, [0,29,51,15])
    utils.swap(rubik, [1,32,52,12])
    utils.swap(rubik, [2,35,53,9])
    utils.swap(rubik, [36,38,44,42])
    utils.swap(rubik, [37,41,43,40])

def back_double(rubik):
    i = 0
    while i < 2:
        back(rubik)
        i += 1

# MOUVEMENT UP
def up(rubik):
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])

# MOUVEMENT DOWN
def up(rubik):
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])

# MOUVEMENT LEFT
def up(rubik):
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])

# MOUVEMENT RIGHT
def up(rubik):
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])
    utils.swap(rubik, [,,,])
