#Задача 0004
#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
#Входные и выходные данные хранятся в отдельных текстовых файлах.


data2 = open('file2.txt','w')

with open('file1.txt','r') as data1:
    for row in data1:
        previous = ''
        count = 0
        encoding = ''
        for symbol in row:
            if symbol != previous:
                if previous:
                    encoding = encoding + str(count) + previous
                count = 1
                previous = symbol
            else:
                count += 1
        
        encoding = encoding + str(count) + previous
        encoding = encoding.replace('1\n','')
        data2.write(encoding + '\n')
        
data2.close


data3 = open('file3.txt','r')

with open('file4.txt','w') as data4:
    for item in data3:
        count=''
        decoding = ''
        for symbol in item:
            if symbol.isdigit():
                count = count + symbol
            elif count != '':
                decoding = decoding + symbol * int(count)
                count = '' 
            else:
                decoding = decoding + symbol
        data4.write(decoding)

data3.close


