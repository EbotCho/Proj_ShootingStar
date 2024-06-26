#2020 그래프
import pandas as pd

# CSV 파일에서 데이터를 불러옵니다. 파일 경로를 적절히 수정하세요.
df = pd.read_excel("/content/spring_2020_data.xlsx")

spring=pd.DataFrame(df)
spring

#한 공동주택의 봄 기간(2월4일~5월 4일)
spring=spring.iloc[0:2163]
spring
len(spring)

#봄,가을 데이터 개수 맞추기 위한 과정
number=[]
for i in range(23,2164,24):
  number.append(i)
print(number)

number_3=[]
for i in range(1,2164,24):
  number_3.append(i)
print(number_3)

number_4=[]
for i in range(2,2164,24):
  number_4.append(i)
print(number_4)


spring.drop([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,144,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,168,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190],axis=0,inplace=True)

spring.drop([23, 47, 71, 95, 119, 143, 167, 191, 215, 239, 263, 287, 311, 335, 359, 383, 407, 431, 455, 479, 503, 527, 551, 575, 599, 623, 647, 671, 695, 719, 743, 767, 791, 815, 839, 863, 887, 911, 935, 959, 983, 1007, 1031, 1055, 1079, 1103, 1127, 1151, 1175, 1199, 1223, 1247, 1271, 1295, 1319, 1343, 1367, 1391, 1415, 1439, 1463, 1487, 1511, 1535, 1559, 1583, 1607, 1631, 1655, 1679, 1703, 1727, 1751, 1775, 1799, 1823, 1847, 1871, 1895, 1919, 1943, 1967, 1991, 2015, 2039, 2063, 2087, 2111, 2135, 2159],axis=0,inplace=True)

spring.drop([1, 25, 49, 73, 97, 121, 145, 169, 193, 217, 241, 265, 289, 313, 337, 361, 385, 409, 433, 457, 481, 505, 529, 553, 577, 601, 625, 649, 673, 697, 721, 745, 769, 793, 817, 841, 865, 889, 913, 937, 961, 985, 1009, 1033, 1057, 1081, 1105, 1129, 1153, 1177, 1201, 1225, 1249, 1273, 1297, 1321, 1345, 1369, 1393, 1417, 1441, 1465, 1489, 1513, 1537, 1561, 1585, 1609, 1633, 1657, 1681, 1705, 1729, 1753, 1777, 1801, 1825, 1849, 1873, 1897, 1921, 1945, 1969, 1993, 2017, 2041, 2065, 2089, 2113, 2137, 2161],axis=0,inplace=True)

spring.drop([2, 26, 50, 74, 98, 122, 146, 170, 194, 218, 242, 266, 290, 314, 338, 362, 386, 410, 434, 458, 482, 506, 530, 554, 578, 602, 626, 650, 674, 698, 722, 746, 770, 794, 818, 842, 866, 890, 914, 938, 962, 986, 1010, 1034, 1058, 1082, 1106, 1130, 1154, 1178, 1202, 1226, 1250, 1274, 1298, 1322, 1346, 1370, 1394, 1418, 1442, 1466, 1490, 1514, 1538, 1562, 1586, 1610, 1634, 1658, 1682, 1706, 1730, 1754, 1778, 1802, 1826, 1850, 1874, 1898, 1922, 1946, 1970, 1994, 2018, 2042, 2066, 2090, 2114, 2138, 2162],axis=0,inplace=True)

spring.drop([2084,1992,1848,1824,1728],axis=0,inplace=True)

spring.drop([528,576,648,696,744,792,888,984,1032,1080],axis=0,inplace=True)
#봄,가을 인덱스 맞추기 위함
spring.reset_index(inplace=True)
len(spring)


import pandas as pd

# CSV 파일에서 데이터를 불러옵니다. 파일 경로를 적절히 수정하세요.
df = pd.read_excel("/content/fall_2020_data.xlsx")

fall=pd.DataFrame(df)
fall

#한 공동주택의 가을 기간(8월7일~11월 6일)
fall=fall.iloc[0:1708]
#봄,가을 인덱스 맞추기 위함
fall.reset_index(inplace=True)
len(fall)
import pandas as pd
import matplotlib.pyplot as plt


# 그래프 그리기
plt.figure(figsize=(60, 20))

# spring 데이터 그래프
plt.plot(spring.index, spring['e_sum_load'], label='Spring 2020', marker='o', linestyle='-', color='b')

# fall 데이터 그래프
plt.plot(fall.index, fall['e_sum_load'], label='Fall 2020', marker='x', linestyle='-', color='r')

# 그래프 설정
plt.xlabel('e_tm')
plt.ylabel('e_sum_load')
plt.title('Comparison of e_sum_load: Spring 2020 vs Fall 2020')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# 그래프 보여주기
plt.show()

#2021 그래프
import pandas as pd

# CSV 파일에서 데이터를 불러옵니다. 파일 경로를 적절히 수정하세요.
df = pd.read_excel("/content/spring_2021_data.xlsx")

spring=pd.DataFrame(df)
spring

#한 공동주택의 봄 기간(2월4일~5월 4일)
spring=spring.iloc[2:2139]
#봄,가을 인덱스 맞추기 위함
spring.reset_index(inplace=True)
spring
len(spring)


import pandas as pd

# CSV 파일에서 데이터를 불러옵니다. 파일 경로를 적절히 수정하세요.
df = pd.read_excel("/content/fall_2021_data (1).xlsx")

fall=pd.DataFrame(df)
fall
#한 공동주택의 가을 기간(8월7일~11월 6일)
fall=fall.iloc[0:2187]
len(fall)

fall.drop([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,51,52,53,54,55,56,57],axis=0,inplace=True)
fall.reset_index(inplace=True)
len(fall)


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
# MinMaxScaler를 사용하여 데이터를 스케일링
scaler = MinMaxScaler()

spring['e_sum_load_scaled'] = scaler.fit_transform(spring[['e_sum_load']])
fall['e_sum_load_scaled'] = scaler.fit_transform(fall[['e_sum_load']])

# 그래프 그리기
plt.figure(figsize=(60, 20))

# spring 데이터 그래프
plt.plot(spring.index, spring['e_sum_load'], label='Spring 2021', marker='o', linestyle='-', color='b')

# fall 데이터 그래프
plt.plot(fall.index, fall['e_sum_load'], label='Fall 2021', marker='x', linestyle='-', color='r')

# 그래프 설정
plt.xlabel('e_tm')
plt.ylabel('e_sum_load')
plt.title('Comparison of e_sum_load: Spring 2021 vs Fall 2021')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# 그래프 보여주기
plt.show()

#2022년 그래프
import pandas as pd

# CSV 파일에서 데이터를 불러옵니다. 파일 경로를 적절히 수정하세요.
df = pd.read_excel("/content/spring_2022_data (1).xlsx")

spring=pd.DataFrame(df)
spring
#한 공동주택의 봄 기간(2월4일~5월 4일)
spring=spring.iloc[0:2139]
#봄,가을 데이터 맞추기 위함
spring.reset_index(inplace=True)
len(spring)


import pandas as pd

# CSV 파일에서 데이터를 불러옵니다. 파일 경로를 적절히 수정하세요.
df = pd.read_excel("/content/fall_2022_data (1).xlsx")

fall=pd.DataFrame(df)
fall
fall=fall.iloc[0:2211]
fall
len(fall)

fall.drop([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69],axis=0,inplace=True)
fall.drop([70,72,75,76,77,78,79,80,81,82],axis=0,inplace=True)
#봄,가을 데이터 맞추기 위함
fall.reset_index(inplace=True)
len(fall)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
# MinMaxScaler를 사용하여 데이터를 스케일링
scaler = MinMaxScaler()

spring['e_sum_load_scaled'] = scaler.fit_transform(spring[['e_sum_load']])
fall['e_sum_load_scaled'] = scaler.fit_transform(fall[['e_sum_load']])

# 그래프 그리기
plt.figure(figsize=(60, 20))

# 그래프 그리기
plt.figure(figsize=(60, 20))

# spring 데이터 그래프
plt.plot(spring.index, spring['e_sum_load'], label='Spring 2022', marker='o', linestyle='-', color='b')

# full 데이터 그래프
plt.plot(fall.index, fall['e_sum_load'], label='Fall 2022', marker='x', linestyle='-', color='r')

# 그래프 설정
plt.xlabel('e_tm')
plt.ylabel('e_sum_load')
plt.title('Comparison of e_sum_load: Spring 2022 vs Fall 2022')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# 그래프 보여주기
plt.show()
