from PyPDF2 import PdfFileReader #импорт библиотеки для работы с prf-файлами
import os # импорт библиотеки для работы с операционной системой
import pandas as pd #импорт библиотеки для работы с таблицами


def read_pdf(fname): #объявили функцию, получает на вход параметр - имя файла(включая путь), а возвращает структуру данных с набором полей из файла
    try:
        inputPdf = PdfFileReader(open(fname, "rb")) #открываем указанный файл, с помощью PdfFileReader переводим в объект
        docInfo = inputPdf.getDocumentInfo() #запрашиваем информацию из pdf-файла
        return {
            'author': docInfo.author,
            'creator': docInfo.creator,
            'producer': docInfo.producer,
            'title': docInfo.title,
            'subject': docInfo.subject
        }
    except:
        print('ERROR: cant read file '+fname) #в случае ошибки выводим "ERROR : cant read file ... "
        return {} # и возвращаем пустую структуру данных

rows = [] #задаем пустой массив
for root, dirs, files in os.walk('data/Raw Spec Files'): #пробежаться по всем поддиректориям и файлам в "data/Raw Spec Files"
    for f in files:
        fname = os.path.join(root, f) # к имени файла дописываем директорию, в которой он лежит
        rows.append(read_pdf(fname)) #наполняем массив данными из pdf-файла

df = pd.DataFrame(rows) #превращаем массив в таблицу
print(df)