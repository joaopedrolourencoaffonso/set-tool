# set-tool

<p align="center"><img src="https://raw.githubusercontent.com/joaopedrolourencoaffonso/set-tool/main/logo.png" width="312" height="200"></p>

A small python-based tool to manipulate sets in a simple and intuitive way.

## How to use

The script needs at least 2 files as input and a command of what to do, being possible to pass several commands:

### Help
```bash
>python set-tool.py --help
Usage: set-tool.py [-h] [--file1 FILE1] [--file2 FILE2] [--inter] [--difer12] [--difer21] [--union]
                     [--elements1] [--elements2] [--s1 S1] [--s2 S2]

A script to pick up common elements between two files.

options:
    -h, --help show this help message and exit
    --file1 FILE1  First file to compare
    --file2 FILE2  Second file to compare.
    --inter        Common elements
    --difer12      Elements that are in file 1 but not in file 2
    --difer21      Elements that are in file 2 but not in file 1
    --union        Total set of elements
    --elements1    Elements in file 1
    --elements2    Elements in file 2
    --s1 S1        Separators to be used in file 1
    --s2 S2        Separators to be used in file 2
```

### Intersection of Sets (**inter**)
By default, the script will create sets based on lines in the file, i.e. each line will be a different element in the set. As such, the ```inter``` flag will create a list of common lines (i.e. elements) from both given files:
```bash
>python set-tool.py --file1 test_1.txt --file2 test_2.txt --inter
Common elements: ['18', '19', '20', '17', '11', '13', '12', '10', '15', '14', '16']
```

### Union of files (**union**)
It will show all individualized unique *lines* from both files:
```bash
>python set-tool.py --file1 "test_1.txt" --file2 "test_2.txt" --union
All unique elements: ['12', '16', '22', '4', '19', '7', '18', '10', '15', '28', '26', '9', '2', '11', '13', '29', '6', '21', '23', '25', '27', '24', '5', '20 ', '1', '3', '17', '14', '8']
```

### Difference (**difer12**, **difer21**)
The ```difer12``` and ```difer21``` options are used to see the difference between the given files: ```difer12``` will provide elements from file 1 and not present in file 2, ` ` `difer21``` will provide elements from file 2 and not present in file 1.

```bash
>python set-tool.py --file1 "test_1.txt" --file2 "test_2.txt" --difer12 --difer21
Elements of (1) not present in (2): ['5', '8', '7', '6', '9', '2', '4', '3', '1']

Elements of (2) not present in (1): ['26', '27', '21', '25', '22', '28', '29', '24', '23']
```

### Unique elements in each file (**elements1**, **elements2**)
Provides a set of unique elements in the files:
```bash
>python set-tool.py --file1 "test_1.txt" --file2 "test_2.txt" --elements1 --elements2
File 1 elements: ['16', '13', '12', '3', '20', '19', '11', '8', '18', '7', '9', '6', '5', '17', '15', '2', '14', '4', '1', '10']

File 2 elements: ['16', '13', '21', '12', '25', '26', '28', '24', '20', '23', '19', '29', '11', '22', '18', '27', '17', '15', '14', '10']
```

### Arbitrary Separators (**s1**, **s2**)
By default set-tools uses "\n" as a separator, however you can use the s1 flag to provide a list of custom separators, for this you must use the "s1" or "s2" flag with a string of desired separators separated by "|" the **only** character that you cannot use as a custom separator:
```bash
>python set-tool.py --file1 "test_1.txt" --file2 "test_3.txt" --s2 "\n|;|-" --elements1 --elements2
File 1 elements: ['13', '9', '19', '4', '7', '5', '18', '16', '10', '11', '15', '8', '17', '6', '3', '14', '12', '1', '2', '20']

File 2 elements: ['13', '9', '19', '4', '7', '5', '18', '16', '10', '11', '15', '8', '17', '6', '3', '14', '12', '1', '2', '20']
```
