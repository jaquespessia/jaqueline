operacao = int (input("qual a sua nota: "))
match operacao:
    case 10:
      print("parabéns, nota máxima")
    case 7|8|9:
      print("parabéns, nota boa")
    case 5|6:
      print("se esforce mais")
    case 2|3|4:
      print("estude mais")
    case 0|1:
      print("voce é burro e nunca vai ser ninguem na vida")
