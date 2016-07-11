#!_*_ coding:utf-8 _*_

from entity.entity import CSVStruct

class CVSHelper:

    def __init__(self, csv_path):
        print(csv_path)
        self.csv_path = csv_path

    def read_all(self):
        csv_content = []
        with open(self.csv_path) as fp:
            while True:
                line = fp.readline().strip()
                if not line:
                    break
                print(line)
                items = line.split(",")
                item = CSVStruct(items(0), items(1), items(2), items(3), items(4), items(5))
                csv_content.append(iterm)
        return csv_content
