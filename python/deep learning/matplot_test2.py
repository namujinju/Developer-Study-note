import matplotlib as mpl
import pandas
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# matplotlib 폰트설정
plt.rc('font', family='NanumGothic') # For Windows

DATASET_PATH = "../Datasets/"
test_dataframe = pandas.read_csv(DATASET_PATH + '목포 2014년.csv', sep=",", engine='python', header = None)
test_dataframe = test_dataframe.iloc[:20, :] # 1년 8760개의 데이터 중 1월만 가져옴

test_prediction_dataframe = pandas.read_csv(DATASET_PATH + 'my_testset_prediction_2014.csv', sep=",", engine='python', header = None)

# test
dataset = test_dataframe.values
x = dataset[:20,0]
y1 = dataset[:20,5]
dataset = test_prediction_dataframe.values
y2 = dataset[:20,0]

plt.plot(x, y1, label="observed")
plt.plot(x, y2, label="predicted")
# plt.plot(x, y3, label="MAE")

plt.title("2014년 영암 태양광 발전소 발전량 예측값과 관측값 testset")
plt.xlabel("시간")
plt.ylabel("발전량(kWh)")
plt.legend()
plt.show()
