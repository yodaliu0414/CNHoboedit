import pandas as pd
import os
import numpy as np
from sympy import EX

openpath = 'xxxxx' #把XXXXX替换成包含HOBO数据的文件夹地址
savepath = 'xxxxx' #把XXXXX替换成存放提取出的HOBO数据的文件夹地址
#开始时间
startyear = '2022' #格式yyyy，填写开始的年份
startmonth = '08' #格式mm，填写开始的月份
startday = '03' #格式dd，填写开始的日期
starthour = '09' #24小时制，填写开始的时间小时
startminute = '55' #24小时制，填写开始的时间分钟
#结束时间
endyear = '2022' #格式yyyy，填写结束的年份
endmonth = '08' #格式mm，填写结束的月份
endday = '04' #格式dd，填写结束的日期
endhour = '11' #24小时制，填写开始的时间小时
endminute = '05' #24小时制，填写开始的时间分钟

#建议稍微放宽1-2分钟范围，不要填写正好时间，防止因为秒数偏差导致数据获取失败
#只替换''内文字，不要删除''

encoding = 'utf-8-sig' #如果生成的文件出现乱码，可以删除全部文件，再把这替换成utf-8试一下。


def get_file_list(filepath):
    filelist = os.listdir(filepath)
    return filelist

def format_hobo_file(file):
    df = pd.read_csv(file,skiprows=1)
    df.columns=['No','Time','Temp','RH']
    df['Time'] = df['Time'].map(lambda x: x.)!!!

    return df


def split_data(dataframe,start,end):
    con1 = dataframe['Time'] >= start
    con2 = dataframe['Time'] <= end
    data = dataframe[con1&con2]
    return data

if __name__ == '__main__':
    start = f'{startyear}-{startmonth}-{startday} {starthour}:{startminute}'
    end = f'{endyear}-{endmonth}-{endday} {endhour}:{endminute}'
    filelist = get_file_list(openpath)

    for filename in filelist:
        fail_list = []
        success = 0
        csv_number = 0
        if 'csv' in filename:
            csv_number +=1
            try:
                file = os.path.join(openpath,filename)
                formatted_hobo_data = format_hobo_file(file)
                splitted = split_data(formatted_hobo_data,start,end)
                splitted.to_csv(savepath,encoding=encoding)
                success += 1
            except Exception as e:
                print(str(e))
                fail_list.append(filename)

    print(f'{success}/{csv_number} succeed.Check them at{savepath}')
    if len(fail_list)>0:
        print(f'File {fail_list} failed.')
            





    

