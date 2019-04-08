import sys
import parsing
import print_rubik
import move
import shuffle
import utils

rubik =  ["Y","Y","Y","Y","Y","Y","Y","Y","Y",
          "O","O","O","O","O","O","O","O","O",
          "B","B","B","B","B","B","B","B","B",
          "R","R","R","R","R","R","R","R","R",
          "G","G","G","G","G","G","G","G","G",
          "W","W","W","W","W","W","W","W","W"]

def main():
  if len(sys.argv) != 2:
    parsing.error(0, "0")
  inst = parsing.parsing(sys.argv[1])
  print_rubik.print_rubik(rubik)
  shuffle.shuffle(rubik, inst)
  if utils.check_rubik(rubik) == False:
    print("the cube is not solved")
  else:
    print("the cube is solved")

main()