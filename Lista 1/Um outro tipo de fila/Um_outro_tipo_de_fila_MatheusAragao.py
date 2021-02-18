tamanho = int(input())
class Pilha:
    def __init__(self,tamanho):
        self.tamanho = tamanho
        self.lista = []
        self.is_reversed = False
        
    def execute(self):
        for x in range(tamanho):
            comandos = input().split()
            operacao = comandos[0]
            if len(comandos) >1:
                valor = comandos[1]
            if self.is_reversed == False:
                if operacao == '4' and len(self.lista) ==0  or operacao == '5' and len(self.lista) ==0:  
                    print('-1')
                else:
                    if operacao =='4':
                        valor_removido = self.lista.pop(0)
                        print(valor_removido)
                    if operacao =='5':
                        valor_removido =  self.lista.pop()
                        print(valor_removido)
                if operacao == '1':
                    self.lista.insert(0,valor)
                if operacao == '2':
                    self.lista.append(valor)
                if operacao == '3':
                    self.is_reversed = True
                    continue            

            if self.is_reversed == True:
                    if operacao == '4' and len(self.lista) ==0  or operacao == '5' and len(self.lista) ==0:  
                        print('-1')
                    else:
                        if operacao =='4':
                            valor_removido = self.lista.pop()
                            print(valor_removido)

                        if operacao =='5':
                            valor_removido =  self.lista.pop(0)
                            print(valor_removido)

                        if operacao == '1':
                            self.lista.append(valor)  

                        if operacao == '2':
                            self.lista.insert(0,valor)
        
                        if operacao == '3':
                            self.is_reversed = False
                
                

def main():
    p1 = Pilha(tamanho)
    p1.execute()
        



if __name__ == '__main__':
    main()
