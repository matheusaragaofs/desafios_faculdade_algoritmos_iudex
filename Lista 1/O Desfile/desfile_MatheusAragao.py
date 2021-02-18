
def main():
    sambodromo = []
    rua_lateral = []
    topo_sambodromo = {}
    topo_rua_lateral = 0
    incoerencias = 0
    primeiro_input = 0
    while True:     
        try:
            tema = input()
            pessoas= int(input())
            carro_atual = {
                tema: pessoas
            }
            primeiro_input +=1
        except EOFError:
            break
        if primeiro_input == 1:  
            rua_lateral.append(carro_atual)
            topo_rua_lateral = carro_atual
        else:
            if pessoas < sum(topo_sambodromo.values()) and len(sambodromo) != 0:
                incoerencias +=1
            else:
                if pessoas < sum(topo_rua_lateral.values()):
                    rua_lateral.append(carro_atual)
                    topo_rua_lateral = carro_atual

                elif pessoas == sum(topo_rua_lateral.values()):
                    if tema > list(topo_rua_lateral.keys())[0]:
                        rua_lateral.append(pessoas)
                    else:
                        rua_lateral.append(pessoas)

                elif pessoas > sum(topo_rua_lateral.values()):
                    while pessoas > sum(topo_rua_lateral.values()):
                        topo_removido =  rua_lateral.pop()
                        sambodromo.append(topo_removido)
                        topo_sambodromo = topo_removido


                        if len(rua_lateral) == 0:
                            rua_lateral.append(carro_atual)
                            topo_rua_lateral = carro_atual 

                        elif len(rua_lateral) != 0:
                            topo_rua_lateral = rua_lateral[-1]


                        

    while len(rua_lateral) != 0:
        topo_da_rua_lateral = rua_lateral.pop()
        sambodromo.append(topo_da_rua_lateral)  


    if incoerencias == 0:
        print('True')
    else:
        print('False')                           
                                




if __name__ == '__main__':
    main()
