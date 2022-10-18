import pandas as pd
data={
    'PatientID': [556785, 998764, 477822, 678329, 675859],
    'Gender': ['M', 'F', 'M', 'M', 'F'],
    'Age': [19, 38, 54, 22, 41],
    'Outcome': ['Negative', 'Poisitive', 'Positive', 'Negative', 'Negative'],
}

dF = pd.DataFrame(data)
print(dF)
print(dF.head(n=3))
print(dF.tail(n=2))

gender_column= dF['Gender'] #抓個別column
print(gender_column)

age_column = dF.Age  #簡化，若標題為string，可以dF.直接接標題明
print(age_column)

cv_data_path = '/Users/LaiYuanTe/PycharmProjects/python-bioinformatics/data_2021-Oct-31.csv'
cv_data = pd.read_csv(cv_data_path, sep='delimiter', header=None, engine='python') #上網查的，第二第三才能成功顯示文件，第四要指名用python作為engine, 不加不行
print(cv_data.head(n=10))
print(cv_data.info())
print(cv_data.info) #上下兩者顯示資料不一樣，斟酌，cv_data.info也有顯示資料的shape
# print(cv_data.shape)

duplicated = cv_data.append(cv_data) #複製原始資料，原始資料形狀乘以兩倍了
print(duplicated.shape)
duplicated = duplicated.drop_duplicates() #drop掉重複的部分，因為有assign給新參數duplicated了，所以原始資料不會被改變
print(duplicated.shape)
# 若想改變原始資料：duplicated.drop_duplicates(inplace=True)



# 處理Null data
# 1. Remove all rows with missing data，目前先學1.
# 2. Imputing the missing values
import numpy as np
n_rows = cv_data.shape[0] #用shape值抓出row
null_containing_data = np.random.choice([None, 1], n_rows, p=[0.2,0.8]) #增加一個column，在其中以機率0.2:0.8來填上none或1
print(null_containing_data)
cv_data['RandomData'] = null_containing_data
print(cv_data.head(10))
print(cv_data.info())
print(cv_data.isnull().sum())
remove_rows = cv_data.dropna() #預設刪除帶有一個以上null值的row
print(remove_rows.head(10))
print(remove_rows.info()) #因為以機率0.2:0.8來填上none或1，所以會有2467-1972的null的row被刪除
cv_data.dropna(axis=1, inplace=True) #刪除剛剛增加的column，回覆原始資料狀態
print(cv_data.info())



# Understanding Data
cv_data = pd.read_csv(cv_data_path)
# print(cv_data.head(n=10))
print(cv_data.shape)
print(cv_data.describe()) #快速查找data的summary, info是給shape, 不一樣
print(cv_data.areaName.describe())
print(cv_data.areaName.unique()) #找無重複
print(cv_data.areaName.value_counts()) #Count每一組不重複的內容



#Slicing and Selecting
print(cv_data[['areaName', 'areaCode']].head(5)) #只讀取兩欄的前五筆資料，要用雙[[]]匡取！！
print(cv_data.loc[222]) #選擇一筆資料
print(cv_data.loc[222:226]) #選擇多筆資料



#Conditional Selection
wales_data = cv_data[cv_data['areaName']=='Wales'] #用條件句匡選小範圍的部分
print(wales_data.head(5))

print(cv_data[cv_data['newCasesByPublishDate']<100].head(5))

print(cv_data[(cv_data['newCasesByPublishDate']>10000) & (cv_data['areaName']=='England')].shape)



#Arithmetic
cv_data['estimated_tomorrow_total_number'] = cv_data.newCasesByPublishDate + cv_data.cumCasesByPublishDate
#製造新column
print(cv_data.head(5))
print(cv_data.shape)
print(cv_data.newCasesByPublishDate.mean()) #有無多那個括號都可以
print(cv_data.cumCasesByPublishDate.std()) #有無多那個括號都可以



#加上Functions
def categorize_cases(x):
    if x >= 30000:
        return 'High'
    elif x <= 10000:
        return 'Low'
    else:
        return 'Moderate'
cv_data['Category'] = cv_data['newCasesByPublishDate'].apply(categorize_cases)
print(cv_data.head(20)) #用apply連接function!!!
cv_data['new_Category'] = cv_data['newCasesByPublishDate'].apply(lambda x: 'Red' if x>40000 else 'Amber')
print(cv_data.head(20)) #用lambda簡化function設定



#Time-Series
print(type(cv_data.date))
cv_data['date'] = pd.to_datetime(cv_data['date']) #將string轉換成datetime type !!!
print(cv_data.info())
print(type(cv_data.date[2]))

# Lets select data between the 20th and the 30th October 2021 and restrict it to Wales
selection = cv_data[(cv_data['date'].between('2021-10-20','2021-10-30')) & (cv_data['areaName']=='Wales')]
print(selection.tail(10))
print(selection.shape)

scotland_data = pd.DataFrame(cv_data[cv_data.areaName == 'Scotland'])
scotland_data.set_index('date', inplace=True) #用date當index！ inplace設true：最新時間到最舊
print(scotland_data.head(5))

scotland_data.sort_index(inplace=False) #用sort_index順牌或逆排時間，inplace設true：最舊時間到最新
print(scotland_data.head(5))

print(scotland_data.loc['2021-10-23':'2021-10-29']) #用loc選時間區間 (注意時間中間用問號)

print(scotland_data.resample(rule='10d')['newCasesByPublishDate'].mean()) #用日數分小組，min()也可做min(), max(), sum()

scotland_data['rollingAvgTenDay'] = scotland_data.rolling(10)['newCasesByPublishDate'].mean() #rolling average
print(scotland_data.head(20))



#Ploting 繪圖
import matplotlib.pyplot as plt
# window = scotland_data['2021-09-30':'2021-10-30']
# window.newCasesByPublishDate.plot.box()  #box()盒方圖，可替換其他圖形如line()直線圖
# plt.show()

scotland_data.newCasesByPublishDate.plot(figsize=(12, 8))  # also specify the size!
scotland_data.rollingAvgTenDay.plot() #將每日case和10日平均曲線畫在同一張圖上
plt.legend();  # We can also add a legend using matplotlib!
plt.show()

figure = scotland_data.newCasesByPublishDate.plot(figsize=(12, 8)).get_figure()
figure.savefig('/Users/LaiYuanTe/PycharmProjects/python-bioinformatics/Scotland_2021-Dec-14.png')

#Question 如何將重疊的曲線圖存擋???
