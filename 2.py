import re
import pydot

def obhod():
    pass

def main():

    with open('lab1sapr.txt', 'r') as f:
        v2 = f.readlines()

    ident = list()

    for i in v2: #получаем список строк итогового кода
       i = re.sub("[\n]", "", i)
       ident.append(i)

    #сексуальная реализация дерева)))))))))))
    obhod()
    print(obhod())



    

if __name__ == "__main__":
    main()