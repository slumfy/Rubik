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

def check_rubik(rubik):
	valid =  ["Y","Y","Y","Y","Y","Y","Y","Y","Y",
        	  "O","O","O","O","O","O","O","O","O",
          	  "B","B","B","B","B","B","B","B","B",
          	  "R","R","R","R","R","R","R","R","R",
          	  "G","G","G","G","G","G","G","G","G",
         	  "W","W","W","W","W","W","W","W","W"]
			   
	for idx in range(len(valid)):
		if valid[idx] != rubik[idx]:
			return (False)
	return (True)