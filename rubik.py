import sys
import parsing
import print_rubik
import move

rubik =  ["W","W","W","W","W","W","W","W","W",
          "B","B","B","B","B","B","B","B","B",
          "O","O","O","O","O","O","O","O","O",
          "G","G","G","G","G","G","G","G","G",
          "R","R","R","R","R","R","R","R","R",
          "Y","Y","Y","Y","Y","Y","Y","Y","Y"]

def main():
  if len(sys.argv) != 2:
    parsing.error(0, "0")
  inst = parsing.parsing(sys.argv[1])
  print_rubik.print_rubik(rubik)
  for idx in range(len(inst)):
    print("tableau d'instuction", idx,"\t",inst[idx])

main()