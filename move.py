import utils

def swap(rubik, list):
    for idx in utils.my_range(0, len(list) - 1, 2):
        temp = rubik[list[idx + 1]]
        rubik[list[idx + 1]] = rubik[list[idx]]
        rubik[list[idx]] = temp

def front(rubik):
    swap(rubik, [6,27,7,30,8,33])
    swap(rubik, [6,45,7,46,8,47])
    swap(rubik, [6,11,7,14,8,17])
    swap(rubik, [18,20,18,26,18,24,19,23,19,25,19,21])