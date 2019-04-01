import utils

def print_rubik(rubik):
  pad = 0
  print("\n")
  for idx in range (0, 6):
    if idx == 0:
      print("\tUP\n\t", end = "")
      for idx in range (0, 9):
        print(rubik[idx + pad], end = "")
        if (idx + 1) % 3 == 0:
          print("\n\t", end = "")
    if idx == 1:
      print("\n LEFT  FRONT  RIGHT  BACK")
      for idx in utils.my_range(0,8,3):
        for idx in range (0,3):
          print(rubik[idx + pad], end = "")
        print("\t", end = "")
        for idx in range (0,3):
          print(rubik[idx + pad *2], end = "")
        print("\t", end = "")
        for idx in range (0,3):
          print(rubik[idx + pad *3], end = "")
        print("\t", end = "")
        for idx in range (0,3):
          print(rubik[idx + pad *4], end = "")
        print()
    if idx == 5:
      print("\n\tDOWN\n\t", end = "")
      for idx in range (0, 9):
        print(rubik[idx + pad], end = "")
        if (idx + 1) % 3 == 0:
           print("\n\t", end = "")
    pad += 9
  print()