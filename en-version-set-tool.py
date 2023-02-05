# IMPORTING LIBRARIES
# COMMAND LINE
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
            print("ERROR: Lacking arguments")
            exit();
            
        '''CREATING SETS
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


        '''ACTION SELECTED BY USER
        '''
        if args.elementos1:
            print("File 1 elements: ",list(lista_1),"\n");
            
        if args.elementos2:
            print("File 3 elements: ",list(lista_2),"\n");
        
        if args.inter:
            print("Common elements: ", list(lista_1.intersection(lista_2)),"\n");
        
        if args.difer12:
            print("Elements of (1) not present in (2): ", list(lista_1 - lista_2),"\n");
        
        if args.difer21:
            print("Elements of (2) not present in (1): ", list(lista_2 - lista_1),"\n");
            
        if args.union:
            print("All unique elements: ", list(lista_1.union(lista_2)),"\n");
    
    except forbiden_symbol:
        print("Error: Symbol '|' cannot be used as a separator.\nPlease check your entry for typos.");

    except Exception as e:
        print("=================================");
        print(str(e));
        print("=================================");

parser = argparse.ArgumentParser(description='A script to pick up common elements between two files.');
parser.add_argument('--file1',default=False,type=Path, help='First file to be comparedo');
parser.add_argument('--file2',default=False, type=Path,help='Second file to be compared');
parser.add_argument('--inter',action="store_true",default=False, help='Common elements');
parser.add_argument('--difer12',action="store_true",default=False, help='Elements present in file 1 but not in file 2');
parser.add_argument('--difer21',action="store_true",default=False, help='Elements present in file 2 but not in file 1');
parser.add_argument('--union',action="store_true",default=False, help='All unique elements');
parser.add_argument('--elements1',action="store_true",default=False,help='File 1 elements');
parser.add_argument('--elements2',action="store_true",default=False, help='File 2 elements');
parser.add_argument('--s1',default=False, help='Separators to be used in file 1');
parser.add_argument('--s2',default=False, help='Separators to be used in file 2');
    
args = parser.parse_args();

if __name__ == '__main__':
    main();
