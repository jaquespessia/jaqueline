operacao = int (input("coloque sua idade: "))
match operacao:
    case x if x < 12:
      print("crianca")
    case x if x>12 and x<18:
      print("adolescente")
    case x if x>18 and x<60:
      print("adulto")
    case x if x>60 and x<100:
      print("idoso")
    case x if x>100 and x<200:
      print("mumia")
