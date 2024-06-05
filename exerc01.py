nota1 = float(input("Digite a nota 1"))
nota2 = float(input("Digite a nota 2"))
nota3 = float(input("Digite a nota 3"))

media = (nota1 + nota2 + nota3) / 3

# verificar a media  
if media >= 7:
   print("o aluno esta aprovado!")
elif media <= 5:
   print("o aluno esta em recuperaçao!")
else:   
   print(" o aluno reprovado!")
