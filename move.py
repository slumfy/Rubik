import utils

# MOUVEMENT FRONT
def front(rubik):
    utils.swap(rubik, [17,47,27,6])
    utils.swap(rubik, [14,46,30,7])
    utils.swap(rubik, [11,45,33,8])
    utils.swap(rubik, [18,20,26,24])
    utils.swap(rubik, [19,25,21,23])

def front_rev(rubik):
    utils.swap(rubik, [6,27,47,17])
    utils.swap(rubik, [7,30,46,14])
    utils.swap(rubik, [8,33,45,11])
    utils.swap(rubik, [24,26,20,18])
    utils.swap(rubik, [23,21,25,19])

def front_double(rubik):
    i = 0
    while i < 2:
        front(rubik)
        i += 1

def mfront(rubik, x):
	if x == 0:
		front(rubik)
	elif x == 1:
		front_rev(rubik)
	elif x == 2:
		front_double(rubik)

# MOUVEMENT BACK
def back(rubik):
    utils.swap(rubik, [15,53,29,0])
    utils.swap(rubik, [12,52,32,1])
    utils.swap(rubik, [9,51,35,2])
    utils.swap(rubik, [42,44,38,36])
    utils.swap(rubik, [41,39,43,37])

def back_rev(rubik):
    utils.swap(rubik, [0,29,53,15])
    utils.swap(rubik, [1,32,52,12])
    utils.swap(rubik, [2,35,51,9])
    utils.swap(rubik, [36,38,44,42])
    utils.swap(rubik, [37,43,39,41])

def back_double(rubik):
    i = 0
    while i < 2:
        back(rubik)
        i += 1

def mback(rubik, x):
	if x == 0:
		back(rubik)
	elif x == 1:
		back_rev(rubik)
	elif x == 2:
		back_double(rubik)

# MOUVEMENT UP
def up(rubik):
    utils.swap(rubik, [9,18,27,36])
    utils.swap(rubik, [10,19,28,37])
    utils.swap(rubik, [11,20,29,38])
    utils.swap(rubik, [0,2,8,6])
    utils.swap(rubik, [1,7,3,5])

def up_rev(rubik):
    utils.swap(rubik, [36,27,18,9])
    utils.swap(rubik, [37,28,19,10])
    utils.swap(rubik, [38,29,20,11])
    utils.swap(rubik, [6,8,2,0])
    utils.swap(rubik, [5,3,7,1])

def up_double(rubik):
    i = 0
    while i < 2:
        up(rubik)
        i += 1

def mup(rubik, x):
	if x == 0:
		up(rubik)
	elif x == 1:
		up_rev(rubik)
	elif x == 2:
		up_double(rubik)

#MOUVEMENT DOWN
def down(rubik):
    utils.swap(rubik, [15,24,33,42])
    utils.swap(rubik, [16,25,34,43])
    utils.swap(rubik, [17,26,35,44])
    utils.swap(rubik, [45,47,53,51])
    utils.swap(rubik, [46,48,52,50])

def down_rev(rubik):
    utils.swap(rubik, [42,33,24,15])
    utils.swap(rubik, [43,34,25,16])
    utils.swap(rubik, [44,35,26,17])
    utils.swap(rubik, [51,53,47,45])
    utils.swap(rubik, [50,52,48,46])

def down_double(rubik):
    i = 0
    while i < 2:
        down(rubik)
        i += 1

def mdown(rubik, x):
	if x == 0:
		down(rubik)
	elif x == 1:
		down_rev(rubik)
	elif x == 2:
		down_double(rubik)

# MOUVEMENT LEFT
def left(rubik):
    utils.swap(rubik, [0,38,45,18])
    utils.swap(rubik, [3,41,48,21])
    utils.swap(rubik, [6,44,51,24])
    utils.swap(rubik, [9,11,17,15])
    utils.swap(rubik, [10,12,16,14])

def left_rev(rubik):
    utils.swap(rubik, [18,45,38,0])
    utils.swap(rubik, [21,48,41,3])
    utils.swap(rubik, [24,51,44,6])
    utils.swap(rubik, [15,17,11,9])
    utils.swap(rubik, [14,16,12,10])

def left_double(rubik):
    i = 0
    while i < 2:
        left(rubik)
        i += 1

def mleft(rubik, x):
	if x == 0:
		left(rubik)
	elif x == 1:
		left_rev(rubik)
	elif x == 2:
		left_double(rubik)

# MOUVEMENT RIGHT
def right(rubik):
    utils.swap(rubik, [2,36,47,20])
    utils.swap(rubik, [5,39,50,23])
    utils.swap(rubik, [8,42,53,26])
    utils.swap(rubik, [27,29,35,33])
    utils.swap(rubik, [28,30,34,32])

def right_rev(rubik):
    utils.swap(rubik, [20,47,36,2])
    utils.swap(rubik, [23,50,39,5])
    utils.swap(rubik, [26,53,42,8])
    utils.swap(rubik, [33,35,29,27])
    utils.swap(rubik, [28,30,34,32])

def right_double(rubik):
    i = 0
    while i < 2:
        right(rubik)
        i += 1

def mright(rubik, x):
	if x == 0:
		right(rubik)
	elif x == 1:
		right_rev(rubik)
	elif x == 2:
		right_double(rubik)