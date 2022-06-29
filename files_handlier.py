from os import listdir
import csv
from pickle import dump
import pandas as pd


class FileHandlier:
    def __init__(self):
        self.res = {}

    # функция определения типа разделителя в csv файле
    def find_delimiter(self, path_file):
        try:
            first_reading = set(open(path_file, encoding='utf-8').readlines()[0])
            second_reading = set(open(path_file, encoding='866').readlines()[1])
            inter_reading = first_reading.intersection(second_reading)
            sniffer = csv.Sniffer()
            with open(path_file, encoding='utf-8') as fp:
                fp.seek(0)
                delimiter = sniffer.sniff(fp.read(5000)).delimiter
            if delimiter not in list(inter_reading):
                delimiter = 'None'
        except Exception:
            delimiter = 'None'
        return delimiter

    # функция для csv файлов
    def csv_handlier(self, in_path):
        csv_files = [i for i in listdir(in_path) if i[len(i) - 3:] == 'csv']
        for i in csv_files:
            self.res[i] = pd.read_csv(in_path+'/'+i, sep=self.find_delimiter(in_path + '/' + i), engine='python')

    # функция для эксель файлов
    def excel_handlier(self, in_path):
        excel_files = [i for i in listdir(in_path) if i[len(i) - 4:] == 'xlsx']
        for i in excel_files:
            self.res[i] = pd.read_excel(in_path + '/' + i)

    def to_pickle(self):
        with open('Result.pickle', 'wb') as file:
            dump(self.res, file)

    def main_handlier(self, in_path):
        self.excel_handlier(in_path)
        self.csv_handlier(in_path)
        self.to_pickle()


if __name__ == '__main__':
    path = 'C:/Users/.../PycharmProjects/.../task_data'
    handlier = FileHandlier()
    handlier.main_handlier(path)

