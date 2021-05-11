
def main():
  operations_dict = {
    "+": lambda f_num, s_num: f_num + s_num,
    "-": lambda f_num, s_num: f_num - s_num,
    "*": lambda f_num, s_num: f_num * s_num,
    "/": lambda f_num, s_num: f_num / s_num
  }

  user_input = input("Enter expression>>")
  symb = user_input.split()
  if (len(symb) != 3):
      print("Oops")
      return
  f_num = float(symb[0])
  oper = symb[1]
  s_num = float(symb[2])

  if oper in operations_dict:
      print(operations_dict[oper](f_num, s_num))
  else:
      print("Error")
main()





