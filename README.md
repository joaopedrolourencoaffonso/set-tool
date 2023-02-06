# set-tool
A small python based tool for manipulating sets in a simple intuitive way.

## How to use

To work, the script needs at least 2 files as input and a command of what to provide, being possible to pass multiple commands:

### Help
```python
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

### Intersection between files
By default, the script will create sets based on the lines of file, i. e., each line will be a different element in the set:
```python
>python set-tool.py --file1 teste_1.txt  --file2 teste_2.txt --inter
Common elements:  ['18', '19', '20', '17', '11', '13', '12', '10', '15', '14', '16']
```
