from flask import Flask, render_template, request

def contador():

    contadorG = 0
    contadorA = 0
    contadorT = 0
    contadorL = 0

    resposta1 = request.form['opcao1']
    resposta2 = request.form['opcao2']
    resposta3 = request.form['opcao3']
    resposta4 = request.form['opcao4']

    if resposta1 == True:
        contadorG += 1

    if resposta2 == True:
        contadorA += 1

    if resposta3 == True:
        contadorT += 1

    if resposta4 == True:
        contadorL += 1

    print(contadorG)
    print(contadorA)
    print(contadorT)
    print(contadorL)