# Дана строка, содержащая полное имя файла. Выделитьт из этой строки расширение файла (без предшествующей точки).

string = 'C:\\Users\\Кирилл\\Documents\\Grechanov_IS_25\\PZ_7\\PZ_7_7(2).py'

print('Расширение файла:', string.split('.')[-1])
