"""
This program will generate the first step of the excel file creation
for pd_create formula of excel 
formulae=[]
formulae.append(xlwt.Formula('SUM(F1:F5)'))
"""

import pandas as pd
import xlwt


COLOMS = ["models", "eod_or_sod", "pd_create", "merge", "check", "save"]

def create_excel(date, eod, sod):
    """
    Pdcreate file 
    :param date:
    :type date:
    :param eod:
    :type eod:
    :param sod:
    :type sod:
    :return: Dataframe required 
    :rtype: pd.DataFrame
    """
    input_file_df = pd.read_excel(r'citi.xls')
    return input_file_df


if __name__ == "__main__":
    get_date = raw_input("enter the date : ")
    eod = raw_input("enter the number of days for eod :")
    sod = raw_input("enter the number of days for sod :")
    output_df = create_excel(get_date, eod, sod)
    writer = pd.ExcelWriter('output.xlsx')
    output_df.to_excel(writer,'Sheet1')
    writer.save()
    raw_input("output file is created press enter to exit ")
