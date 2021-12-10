import re

'''
С ПАСКАЛЯ НА СИ ЦИКЛ DO WHILE
'''

keyWordsDict = {'var': '1.1',  # ключевые слова
                'integer': '1.2',
                'begin': '1.3',
                'repeat': '1.4',
                'until': '1.5',
                'Inc': '1.6',
                'end': '1.7'}
opersDict = {'+': '2.1',  # операции
             '-': '2.2',
             '*': '2.3',
             '/': '2.4',
             '=': '2.5',
             '(': '2.6',
             ')': '2.7',
             '<': '2.8',
             '>': '2.9',
             '<=': '2.10',
             '>=': '2.11',
             ':=': '2.12',
             '+=': '2.13',
             '-=': '2.14',
             '*=': '2.15',
             '/=': '2.16',
             ';': '2.17',
             '.': '2.18',
             ',': '2.19',
             ':': '2.20',
             '!=': '2.21'}

peremsDict = {}
num = 0

def addingPerem(i,j):
    p = ''
    pc = j
    global num
    while(i[pc] not in opersDict.keys() and i[pc] != ' '):
        p += i[pc]
        pc += 1
    if(p in peremsDict.keys()):
        return p
    num += 1
    peremsDict[p] = '3.' + str(num)

    return p

def delete(arr):
    """
    функция создающая массив для работы др функций
    """
    consistance = list()
    for i in arr:
        i = re.sub("[\n]", " ", i)
        i += ' '
        consistance.append(list(i))
    
    return consistance


def parceToNums():
    """
    функция заменяющая синтаксис кода на его представление
    """
    with open("code.txt", "r") as f:
        v1 = f.readlines()

    code = delete(v1)
    final = ""
    rrr = ''

    with open('lab1sapr.txt', 'w') as f:
        for i in code:
            j = 0
            while j < len(i):
                sub = ''
                if i[j] == ' ':
                    pass
                elif  i[j].isalpha():#проверка на ключевое слово
                    k = 0
                    while i[j+k].isalpha():
                        sub += i[j+k]
                        k += 1
                        if sub in keyWordsDict.keys():
                            final += keyWordsDict.get(sub) + '\n'
                            sub = ''
                            j += k-1
                            break

                if i[j] in opersDict.keys():#проверка на операцию
                    if(i[j+1] == ' '):
                        cc = j+1
                        dlin = len(i) - 1 
                        while (i[cc] == ' ') and (cc < dlin):
                            if i[cc+1] in opersDict.keys():
                                print('неверно введенный символ', i)
                                exit(0)
                            cc += 1
                    dd = i[j] + i[j+1]
                    if (dd) in opersDict.keys():
                        final += opersDict.get(i[j] + i[j+1]) + '\n'
                        j += 1
                        sub = ''
                    else:
                        final += opersDict.get(i[j]) + '\n'

                if i[j].isdigit():#проверка на число
                    m = j
                    while i[m].isdigit():
                        sub += i[m]
                        m += 1
                    final += sub + '\n'
                    j = m - 1

                if sub != '' and not sub.isdigit():
                    rrr = addingPerem(i,j)
                    j += len(rrr) - 1
                    sub = ''
                    final += peremsDict.get(rrr) + '\n'
                j += 1
        f.write(final)

def cl(arr):
    """
    функция для удаления всего лишнего кроме значений таблиц
    """
    for i in arr:
        i.pop(-1)
        i.pop(-1)
    return arr

def sntAnalysis():
    """
    основная функция для создания древовидного представления
    """
    with open('lab1sapr.txt', 'r') as f:
        v2 = f.readlines() #все из файла лаб1

    analysis = delete(v2)
    analysis = cl(analysis)
    print(analysis)
    
if __name__ == "__main__":
    parceToNums()
    sntAnalysis()

