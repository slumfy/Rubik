import sys
rubik = "WWWWWWWWWBBBBBBBBBRRRRRRRRRGGGGGGGGGOOOOOOOOOYYYYYYYYY"

def error(info, string):
  if info == 0:
    sys.stderr.write("bad arguments number\n")
  if info == 1:
    sys.stderr.write("bad instruction format ==>\t")
    sys.stderr.write(string)
  sys.exit()

def parsing(inst):
  db = ["F","R","U","B","L","D"]
  db2 = ["2", "'"]
  tab = inst.split(" ")
  for idx in range(len(tab)):
    if len(tab[idx]) > 2:
      error(1, tab[idx])
    elif any(i in tab[idx][0] for i in db) == False:
      error(1, tab[idx])
    elif len(tab[idx]) == 2 and any(i in tab[idx][1] for i in db2) == False:
      error(1, tab[idx])
    print("tableau d'instuction", idx,"\t",tab[idx])

def print_rubik():
  pad = 0
  print("\n len de rubik",len(rubik))
  for idx in range (0, 6):
    print("face =" ,idx)
    for idx in range (0, 9):
      print (rubik[idx + pad], end = " ")
      if (idx + 1) % 3 == 0:
       print()
    pad += 9
    print()

def main():
  if len(sys.argv) != 2:
    error(0, "0")
  parsing(sys.argv[1])
  print_rubik()

main()
