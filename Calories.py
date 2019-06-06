import pandas as pd
import glob
import datetime

# #readAllFiles
all_files = glob.glob("*.csv")
df = pd.concat((pd.read_csv(f) for f in all_files))
# # df = pd.read_excel("em290301_bike.xlsx",sep=";")
# print(df.head())
# print(df.shape)
#
# #concatenate all columns into one
df['concat'] = pd.Series(df.fillna('').values.tolist()).str.join('')
df = df[["concat"]]
# print(df.head())
# print(df.shape)
#
# #split columns into separate column
df_1 = df['concat'].str.split(';', 13, expand=True)
# print(df_1.head())
df_1 = df_1[[0,11,12]]
# # df_1= df_1[df_1[11] != 0]
# # df_1= df_1[df_1[12] != 0]
#
# #sort by values
df_1[0] = pd.to_datetime(df_1[0])#,format="%d-%m-%Y %H:%M:%S")
df_1 = df_1.sort_values(by=[0],ascending=True)
print(df_1.tail())
# # print(df_1.loc[(df_1[0] >= pd.datetime(2019,3,29)) & (df_1[0] <= pd.datetime(2019,3,29))])
# # a = df_1[df_1[0] <= datetime.date(2019,3,29)]
#
# # print(df_1[0].dtype)

# print(df_1.shape)
#
df_1 = df_1.astype({11:int,12:int})
df_1 = df_1[(df_1 != 0).all(1)]
df_1 = (df_1.reset_index(drop=True).tail())
print(df_1.shape)
print(df_1.shape)
print(df_1)
df_1 = df_1.set_index(0)

calories_list = []

    #subset dataframe from start time to end time
df_betTime = df_1["2019-03-28 13:11:00":"2019-03-28 13:12:10"]

    # for i,j in df_betTime.iterrows():
    #     print(j[11],j[12])

    #calculate calories
for i,j in df_betTime.iterrows():
    calories = ((j[11] * j[12] * 2 * 3.14) / 60) * 0.05 * 0.860421 * 4
    calories_list.append(calories)

print(calories_list)
# # print(df_1.iloc[0][11])
# power = (df_1.iloc[0][11] * df_1.iloc[0][11] * 2 * 3.14) / 60
# print(power)
#
# def getSortedFullDf(path):
#     all_files = glob.glob(path)
#     df = pd.concat((pd.read_excel(f) for f in all_files))
#
#     # concatenate all columns into one
#     df['concat'] = pd.Series(df.fillna('').values.tolist()).str.join('')
#     df = df[["concat"]]
#
#     # split columns into separate column
#     df_1 = df['concat'].str.split(';', 13, expand=True)
#
#     df_1 = df_1[[0, 11, 12]]
#
#     # sort by values
#     df_1[0] = pd.to_datetime(df_1[0])
#     df_1 = df_1.sort_values(by=[0], ascending=True)
#     # print(df_1.tail())
#     # print(df_1.loc[(df_1[0] >= pd.datetime(2019,3,29)) & (df_1[0] <= pd.datetime(2019,3,29))])
#     # a = df_1[df_1[0] <= datetime.date(2019,3,29)]
#
#     # print(df_1[0].dtype)
#
#     # print(df_1.shape)
#
#     df_1 = df_1.astype({11: int, 12: int})
#     df_1 = df_1[(df_1 != 0).all(1)]
#     df_1 = (df_1.reset_index(drop=True))
#     df_1 = df_1.set_index(0)
#     return df_1
#
# def powerInTimeRange(df_1,start,end):
#     calories_list = []
#     # df_betTime = df_1.between_time("2019-03-29 14:36:00","2019-03-29 14:39:00")
#     df_betTime = df_1[start:end]
#     # return df_betTime
#     # print(df_betTime.shape[0])
#     # for i,j in df_betTime.iterrows():
#     #     print(j[11],j[12])
#     for i,j in df_betTime.iterrows():
#         calories = ((j[11] * j[12] * 2 * 3.14) / 60) * 0.05 * 0.860421 * 4
#         calories_list.append(calories)
#     return sum(calories_list)/len(calories_list)
#
#
# if __name__ == '__main__':
#     path = "*.xlsx"
#     df = getSortedFullDf(path)
#     print(df.tail())
#     print(df.shape)
#     startTime = "2019-03-29 14:36:00"
#     endTime = "2019-03-29 14:36:10"
#     df_time = powerInTimeRange(df,startTime,endTime)
#     # print(df_time.shape)
#     # powerInTimeRange(df, startTime, endTime)
#     # print(df_time.tail())
#     # print(df_time.shape)
#     print(df_time)
#











#,usecols=["DateTimeStamp","PedalForce","Cadans"])
# # df = pd.read_csv("em280302_bike.csv",sep=";")
#
# # print(df.head())
# # print(list(df.columns.values))

# print(df.head())

# print(df.head())
# df["all"] = pd.DataFrame(df.astype(str).values.sum(axis=1))
# print(df.head())
# df_1 = pd.DataFrame(df.str.split(';',13),columns=["a","b","c","d","e","f","g","h","i","j","k","l","m","n"])

# print(len(df_1.columns))
#
# df = pd.DataFrame(df.row.str.split(' ',1).tolist(),
#                                    columns = ['flips','row'])
