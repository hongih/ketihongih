import os
import pandas as pd

path = "D:\keti_bigdata_platform\keti_bigdata\서울31바4508"
# path data 매개변수로 입력 하게 변경

file_list = os.listdir(path)
file_list_csv = [file for file in file_list if file.endswith(".csv")]
print("원본 file 갯수:", len(file_list_csv))

new_file_list_csv = []

for file in file_list_csv:
    file_size = os.path.getsize(file)
    # print(file_size)
    if file_size != 0:
        new_file_list_csv.append(file)

print("new file 갯수:", len(file_list_csv))
# new file : file size가 0이 아닌 파일


# new_file_name = new_file_list_csv[0].split('_')[1].split('-')[0]
# print(new_file_name)

df_list = []

for file_list in new_file_list_csv:
    df_name = file_list.split('_')[1].split('-')[0]
    # print(df_name)
    df_list.append(df_name)

print("df_name 갯수 : ", len(df_list))
# for df_name in df_list:
#    print(df_name)


for file_csv in new_file_list_csv:
    df_temp = pd.read_csv(file_csv, sep='\t')
    # df_temp.info()
    df_ov = df_temp.shape
    if df_ov[1] != 1:
        print("real data")
    # else:
    #    print("null data")
    df_temp.describe()


# data 프레임 갯수 및 이름 리스트로 관리.
# print(df_name)
