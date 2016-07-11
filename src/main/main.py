#_*_ coding:utf-8 _*_

from entity.entity import CSVStruct
from utils.csv_helper import CVSHelper

def main():
    computer_infos = CVSHelper("/Users/twcn/work/ISProject/computer-timeout-notification/resources/techops_china_asset_managemen.csv")
    for computer in computer_infos.read_all():
        print(computer.employee_id)
    print(computer_infos)
main()
