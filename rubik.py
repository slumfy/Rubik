import sys

def error(info):
  if info == 0:
    sys.stderr.write("bad arguments number\n")
  if info == 1:
    sys.stderr.write("bad instruction format\n")
  sys.exit()

def parsing(inst):
  db = ["F","R","U","B","L","D"]
  tab = inst.split(" ")
  for idx in range(len(tab)):
    if any(i in tab[idx][0] for i in db) == False:
      error(1)
    print("tableau d'instuction", idx,"\t",tab[idx])


def main():
  if len(sys.argv) != 2:
    error(0)
  parsing(sys.argv[1])

main()