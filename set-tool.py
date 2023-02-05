# Versão em português

# IMPORTANDO BIBLIOTECAS
# Linha de comando
import argparse
from pathlib import Path

class forbiden_symbol(Exception):
    "Raised when the forbiden symbol '|' is used"
    pass

def gera_set(lista, separadores):

    temp = separadores.split('|')[0];    
    separadores = separadores.split("|");

    if separadores.count("") > 0:
        raise forbiden_symbol;
    
    for separador in separadores:
        if separador == "\\n":
            separador = "\n";
            
        lista = lista.replace(separador, temp);

    lista = lista.split(temp)
    
    return set(lista);

def main():
    try:
        if not (args.arquivo1 and args.arquivo2):
            print("ERROR: Faltando argumentos")
            exit();
            
        '''CRIANDO OS SETS
        '''
        lista_1 = open(args.arquivo1,'r').read();
        lista_2 = open(args.arquivo2,'r').read();
        
        if args.s1:
            lista_1 = gera_set(lista_1, args.s1);
            
        else:
            lista_1 = set(lista_1.split("\n"));

        if args.s2:
            lista_2 = gera_set(lista_2, args.s2);

        else:
            lista_2 = set(lista_2.split("\n"));


        '''AÇÃO SELECIONADA PELO USUÁRIO
        '''
        if args.elementos1:
            print("Elementos no arquivo 1: ",list(lista_1),"\n");
            
        if args.elementos2:
            print("Elementos no arquivo 2: ",list(lista_2),"\n");
        
        if args.inter:
            print("Elementos em comum: ", list(lista_1.intersection(lista_2)),"\n");
        
        if args.difer12:
            print("Elementos de (1) ausentes de (2): ", list(lista_1 - lista_2),"\n");
        
        if args.difer21:
            print("Elementos de (2) ausentes de (1): ", list(lista_2 - lista_1),"\n");
            
        if args.union:
            print("Elementos únicos em ambos: ", list(lista_1.union(lista_2)),"\n");
    
    except forbiden_symbol:
        print("Erro: Simbolo '|' proibido foi utilizado como separador.\nVerifique seu input por erros de digitacao.");

    except Exception as e:
        print("=================================");
        print(str(e));
        print("=================================");

parser = argparse.ArgumentParser(description='Um script para pegar elementos em comuns entre dois arquivos.');
parser.add_argument('--arquivo1',default=False,type=Path, help='Primeiro arquivo a ser comparado');
parser.add_argument('--arquivo2',default=False, type=Path,help='Segundo arquivo a ser comparado.');
parser.add_argument('--inter',action="store_true",default=False, help='Elementos em comum');
parser.add_argument('--difer12',action="store_true",default=False, help='Elementos que tem no arquivo 1 mas não no arquivo 2');
parser.add_argument('--difer21',action="store_true",default=False, help='Elementos que tem no arquivo 2 mas não no arquivo 1');
parser.add_argument('--union',action="store_true",default=False, help='Total de elementos');
parser.add_argument('--elementos1',action="store_true",default=False,help='Elementos no arquivo 1');
parser.add_argument('--elementos2',action="store_true",default=False, help='Elementos no arquivo 2');
parser.add_argument('--s1',default=False, help='Separadores para serem usados no arquivo 1');
parser.add_argument('--s2',default=False, help='Separadores para serem usados no arquivo 2');
    
args = parser.parse_args();

if __name__ == '__main__':
    main();
