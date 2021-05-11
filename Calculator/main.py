
def main():
  operations_dict = {
    "+": lambda f_num, s_num: f_num + s_num,
    "-": lambda f_num, s_num: f_num - s_num,
    "*": lambda f_num, s_num: f_num * s_num,
    "/": lambda f_num, s_num: f_num / s_num
  }

  f_num = float(input("Enter the first number>>"))
  oper = input("Enter operation>>")
  s_num = float(input("Enter the second number>>"))
  if oper in operations_dict:
      print(operations_dict[oper](f_num, s_num))
  else:
      print("Error")
main()





