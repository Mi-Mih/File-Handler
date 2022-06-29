class FileHandlier:
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

