# -*- coding: utf-8 -*-
"""Cópia de AOP2 - Introd a Programação de Computadores

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SvMY-vXyOoCBERDsprtxdjKR1JNikeZm

<html>
  <body>
        <center>
          <img src="https://uvv.br/wp-content/themes/uvvBr/templates/assets//img/logouvv.svg" alt="Logo UVV" style = width="100px"; height="100px">
          <p><b>Introdução à Programação de Computadores - Python</b></p>
          <p>Prof. MsC. Wagner de A. Perin</p>
          <p><b>Tutor: </b> Edgar Salardani Senhorello</p>
          <b>AOP2 - Atividade On-Line Pontuada</b>
        </center>
  </body>
</html>

Nome do Aluno: Vicória Alves Salute
"""

def calcular_media(alunos):
  alunos_aprovados = 0

  for aluno in range(alunos):
    print(f"ALUNO {aluno + 1}")
    AOP1 = float(input("Digite a nota da AOP1: "))
    while AOP1 < 0 or AOP1 > 1:
      AOP1 = float(input("Digite novamente a nota da AOP1 [0, 1]: "))

    AOP2 = float(input("Digite a nota da AOP2: "))
    while AOP2 < 0 or AOP2 > 2:
      AOP2 = float(input("Digite novamente a nota da AOP2 [0, 2]: "))

    AOP3 = float(input("Digite a nota da AOP3: "))
    while AOP3 < 0 or AOP3 > 2:
      AOP3 = float(input("Digite novamente a nota da AOP3 [0, 2]: "))

    ProvaRegular = float(input("Digite a nota da prova regular: "))
    while ProvaRegular < 0 or ProvaRegular > 6:
      ProvaRegular = float(input("Digite novamente a nota da prova regular [0, 6]: "))

    SomaTotal = (AOP1 + AOP2 + AOP3 + ProvaRegular)
    media = SomaTotal / 4

    if(SomaTotal <= 6):
      ProvaRecup = float(input("Digite a nota da prova de recuperacao: "))
      while ProvaRecup < 0 or ProvaRecup > 10:
        ProvaRecup = float(input("Digite novamente a nota da prova de recuperacao [0, 10]: "))
      media = (SomaTotal + ProvaRecup) / 2

    if(SomaTotal >= 7 or media >= 5):
      print("ALUNO APROVADO")
      alunos_aprovados += 1
    else:
      print("ALUNO REPROVADO")

  print(f"Total de alunos aprovados: {alunos_aprovados * 100 / alunos}%")

calcular_media(1)