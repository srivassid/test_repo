import pandas as pd
import glob
import datetime

# #readAllFiles
all_files = glob.glob("*.csv")
df = pd.concat((pd.read_csv(f) for f in all_files))kghgiugiug
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
#asdsDFSDFadsasfdsadf\
adsfsdfsdfsdf
# #sort by values
SDGSRAFGsfgsdfgasfg
df_1[0] = pd.to_datetime(df_1[0])#,format="%d-%m-%Y %H:%M:%S")
df_1 = df_1.sort_values(by=[0],ascending=True)

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
asdasdasdasdasfdsdfsdf
