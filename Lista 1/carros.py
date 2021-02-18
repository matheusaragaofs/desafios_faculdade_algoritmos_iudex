def main():

    pista_principal = list() 
    pista_lateral = list()
    lista_tam_carros_principal = list()
    lista_tam_carros_lateral = list()

    while True:
        try:
            tam_nome_carro = len(input())
            qnt_pessoas = int(input())
        except EOFError:
            break

        if not pista_principal:
            pista_principal.append(qnt_pessoas)
            lista_tam_carros_principal.append(tam_nome_carro)
        else:
            if qnt_pessoas < pista_principal[-1] and pista_principal != (not pista_principal):
                pista_principal.append(qnt_pessoas)
                lista_tam_carros_principal.append(tam_nome_carro)

            elif qnt_pessoas > pista_principal[-1] and pista_principal != (not pista_principal):
                while qnt_pessoas > pista_principal[-1] and pista_principal != (not pista_principal):
                    pista_lateral.append(pista_principal[-1])
                    lista_tam_carros_lateral.append(lista_tam_carros_principal[-1])
                    pista_principal.pop()
                    lista_tam_carros_principal.pop()

                if qnt_pessoas == pista_principal[-1] and pista_principal != (not pista_principal):
                    if tam_nome_carro == lista_tam_carros_principal[-1]:
                        pista_principal.append(qnt_pessoas)
                        lista_tam_carros_principal.append(tam_nome_carro)
                    elif tam_nome_carro < lista_tam_carros_principal[-1]:
                        pista_principal.append(qnt_pessoas)
                        lista_tam_carros_principal.append(tam_nome_carro)
                    else:
                        pista_lateral.append(pista_principal[-1])
                        lista_tam_carros_lateral.append(lista_tam_carros_principal[-1])
                        pista_principal.pop()
                        lista_tam_carros_principal.pop()
                        pista_principal.append(qnt_pessoas)
                        lista_tam_carros_principal.append(tam_nome_carro)
                else:
                    pista_principal.append(qnt_pessoas)
                    lista_tam_carros_principal.append(tam_nome_carro)



                for i in pista_lateral[::-1]:
                    pista_principal.append(i)
                for j in lista_tam_carros_lateral[::-1]:
                    lista_tam_carros_principal.append(j)

            elif qnt_pessoas == pista_principal[-1] and pista_principal !=  (not pista_principal):
                if tam_nome_carro == lista_tam_carros_principal[-1]:
                    pista_principal.append(qnt_pessoas)
                    lista_tam_carros_principal.append()
                elif tam_nome_carro > lista_tam_carros_principal[-1]:
                    pista_lateral.append(pista_principal[-1])
                    lista_tam_carros_lateral.append(lista_tam_carros_principal[-1])
                    pista_principal.pop()
                    lista_tam_carros_principal.pop()
                    pista_principal.append(qnt_pessoas)
                    lista_tam_carros_principal.append(tam_nome_carro)
                
                for i in pista_lateral:
                    pista_principal.append(i)

    sub_lista = list()
    resultado = True
    for x in pista_principal:
        if not sub_lista:
            sub_lista.append(x)
        elif x < sub_lista[-1]:
            sub_lista.append(x)
        else:
            print(resultado)
            break

if __name__ == '__main__':
    main()  
