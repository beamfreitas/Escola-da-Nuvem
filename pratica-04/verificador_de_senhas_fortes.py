"""
3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair". 
"""

while True:
    senha = input('Digite uma senha (ou "sair" para encerrar): ')

    if senha.lower() == "sair":
        print("Programa encerrado.")
        break

    if len(senha) < 8:
        print("Senha fraca. A senha deve ter no mínimo 8 caracteres.")
        print("-" * 20)
        continue  

    tem_numero = False
    for char in senha:
        if char.isdigit():
            tem_numero = True
            break 

    if not tem_numero:
        print("Senha fraca. A senha deve conter pelo menos um número.")
        print("-" * 20)
        continue  

    print("Senha forte! Programa encerrado.")
    break