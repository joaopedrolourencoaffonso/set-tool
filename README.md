# set-tool

<p align="center"><img src="https://raw.githubusercontent.com/joaopedrolourencoaffonso/set-tool/main/logo.png" width="312" height="200"></p>

Uma pequena ferramenta baseada em python para manipular conjuntos de forma simples e intuitiva.

## Como usar

O script precisa de pelo menos 2 arquivos como entrada e um comando do que fazer, sendo possível passar vários comandos:

### Help
```bash
>python set-tool.py --help
usage: set-tool.py [-h] [--arquivo1 ARQUIVO1] [--arquivo2 ARQUIVO2] [--inter] [--difer12] [--difer21] [--union]
                   [--elementos1] [--elementos2] [--s1 S1] [--s2 S2]

Um script para pegar elementos em comuns entre dois arquivos.

options:
  -h, --help           show this help message and exit
  --arquivo1 ARQUIVO1  Primeiro arquivo a ser comparado
  --arquivo2 ARQUIVO2  Segundo arquivo a ser comparado.
  --inter              Elementos em comum
  --difer12            Elementos que tem no arquivo 1 mas não no arquivo 2
  --difer21            Elementos que tem no arquivo 2 mas não no arquivo 1
  --union              Total de elementos
  --elementos1         Elementos no arquivo 1
  --elementos2         Elementos no arquivo 2
  --s1 S1              Separadores para serem usados no arquivo 1
  --s2 S2              Separadores para serem usados no arquivo 2
```

### Interseção de Conjuntos (**inter**)
Por padrão, o script criará conjuntos com base nas linhas do arquivo, ou seja, cada linha será um elemento diferente no conjunto. Como tal, a flag ```inter``` criará uma lista de linhas comuns (ou seja, elementos) de ambos os arquivos fornecidos:
```bash
>python set-tool.py --file1 teste_1.txt  --file2 teste_2.txt --inter
Elementos em comum:  ['18', '19', '20', '17', '11', '13', '12', '10', '15', '14', '16']
```

### União de arquivos (**union**)
Mostrará todas as *linhas* exclusivas individualmente de ambos os arquivos:
```bash
>python set-tool.py --arquivo1 "teste_1.txt" --arquivo2 "teste_2.txt" --union
All unique elements:  ['12', '16', '22', '4', '19', '7', '18', '10', '15', '28', '26', '9', '2', '11', '13', '29', '6', '21', '23', '25', '27', '24', '5', '20', '1', '3', '17', '14', '8']
```

### Diferença (**difer12**, **difer21**)
The options ```difer12``` and ```difer21``` are used to see the difference between the files provided: ```difer12``` will provide the elements of file 1 and not present on file 2, ```difer21``` will provide the elements of file 2 and not present on file 1.

```bash
>python set-tool.py --arquivo1 "teste_1.txt" --arquivo2 "teste_2.txt" --difer12 --difer21
Elementos de (1) ausentes de (2):  ['5', '8', '7', '6', '9', '2', '4', '3', '1']

Elementos de (2) ausentes de (1):  ['26', '27', '21', '25', '22', '28', '29', '24', '23']
```

### Elementos únicos em cada arquivo (**elements1**, **elements2**)
Fornece os elementos individualmente exclusivos nos arquivos fornecidos na forma de conjuntos:
```bash
>python set-tool.py --arquivo1 "teste_1.txt" --arquivo2 "teste_2.txt" --elementos1 --elementos2
Elementos no arquivo 1:  ['16', '13', '12', '3', '20', '19', '11', '8', '18', '7', '9', '6', '5', '17', '15', '2', '14', '4', '1', '10']

Elementos no arquivo 2:  ['16', '13', '21', '12', '25', '26', '28', '24', '20', '23', '19', '29', '11', '22', '18', '27', '17', '15', '14', '10']
```

### Separadores Arbitrários (**s1**, **s2**)
Por padrão, o set-tools usa "\n" como separador, no entanto, você pode usar o sinalizador s1 para fornecer uma lista de separadores personalizados, para isso você deve usar o sinalizador "s1" ou "s2" com uma string dos separadores desejados separados por "|" o **único** caractere que você não pode usar como separador personalizado:
```bash
>python set-tool.py --arquivo1 "teste_1.txt" --arquivo2 "teste_3.txt" --s2 "\n|;|-" --elementos1 --elementos2
Elementos no arquivo 1:  ['13', '9', '19', '4', '7', '5', '18', '16', '10', '11', '15', '8', '17', '6', '3', '14', '12', '1', '2', '20']

Elementos no arquivo 2:  ['13', '9', '19', '4', '7', '5', '18', '16', '10', '11', '15', '8', '17', '6', '3', '14', '12', '1', '2', '20']
```

