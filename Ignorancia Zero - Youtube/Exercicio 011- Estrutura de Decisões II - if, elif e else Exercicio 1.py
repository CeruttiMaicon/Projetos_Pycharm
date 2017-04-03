
num1 = int(input("Digite um número menor que 1000: "))
aux = num1

if num1 < 1000:

    centenas = aux // 100
    aux = aux % 100

    dezenas = aux // 10
    aux = aux % 10

    unidades = aux // 1


    if num1 > 100:
        if centenas > 100:
            if dezenas > 10:
                if unidades > 1:
                    print (num1, "=", centenas, "centenas,", dezenas, "dezenas e", unidades, "unidades.")
                else:
                    print (num1, "=", centenas, "centenas,", dezenas, "dezenas e", unidades, "unidade.")
            else:
                if unidades > 1:
                    print (num1, "=", centenas, "centenas,", dezenas, "dezena e", unidades, "unidades.")
                else:
                    print (num1, "=", centenas, "centenas,", dezenas, "dezena e", unidades, "unidade.")
        
        else:
            if dezenas > 1:
                if unidades > 1:
                    
                    print (num1, "=", centenas, "centenas,", dezenas, "dezenas e", unidades, "unidades.")
                else:
                    print (num1, "=", centenas, "centenas,", dezenas, "dezenas e", unidades, "unidade.")
            else:
                if unidades > 1:
                    print (num1, "=", centenas, "centenas,", dezenas, "dezenas e", unidades, "unidades.")
                else:
                    print (num1, "=", centenas, "centenas,", dezenas, "dezenas e", unidades, "unidade.")

    elif 10 <= num1 < 100:
          if dezenas > 1:
             if unidades > 1:
                 print (num1, "=", dezenas, "dezenas e", unidades, "unidades.")
             else:
                  print (num1, "=", dezenas, "dezenas e", unidades, "unidade.")
          else:
               if unidades > 1:
                 print (num1, "=", dezenas, "dezena e", unidades, "unidades.")
               else:
                   print (num1, "=", dezenas, "dezena e", unidades, "unidade.")

    else:
        if unidades > 1:
           print (num1, "=", unidades, "unidades.")
        else:
           print (num1, "=", unidades, "unidade.")
else:
    print (" Esse número é maior que 1000 seu jumento")
                




                    
                
