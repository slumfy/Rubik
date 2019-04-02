def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

def swap(rubik,list):
    temp = rubik[list[0]]
    rubik[list[0]] = rubik[list[1]]
    rubik[list[1]] = rubik[list[2]]
    rubik[list[2]] = rubik[list[3]]
    rubik[list[3]] = temp