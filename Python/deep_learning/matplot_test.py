import matplotlib as mpl
import pandas
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# matplotlib 폰트설정
plt.rc('font', family='NanumGothic') # For Windows

DATASET_PATH = "../Datasets/"
train_dataframe = pandas.read_csv(DATASET_PATH + '목포_2013년_train.csv', sep=",", engine='python', header = None)
dev_dataframe = pandas.read_csv(DATASET_PATH + '목포_2013년_dev.csv', sep=",", engine='python', header = None)
test_dataframe = pandas.read_csv(DATASET_PATH + '목포_2013년_test.csv', sep=",", engine='python', header = None)
train_prediction_dataframe = pandas.read_csv(DATASET_PATH + 'my_trainset_prediction.csv', sep=",", engine='python', header = None)
dev_prediction_dataframe = pandas.read_csv(DATASET_PATH + 'my_devset_prediction.csv', sep=",", engine='python', header = None)
test_prediction_dataframe = pandas.read_csv(DATASET_PATH + 'my_testset_prediction.csv', sep=",", engine='python', header = None)

# train
dataset = train_dataframe.values
x = dataset[:,0]
y1 = dataset[:,5]
dataset = train_prediction_dataframe.values
y2 = dataset[:,0]

plt.plot(x, y1, label="observed")
plt.plot(x, y2, label="predicted")
plt.title("2013년 영암 태양광 발전소 발전량 예측값과 관측값 trainset")
plt.xlabel("시간")
plt.ylabel("발전량(kWh)")
plt.legend()
plt.show()

# dev
dataset = dev_dataframe.values
x = dataset[:,0]
y1 = dataset[:,5]
dataset = dev_prediction_dataframe.values
y2 = dataset[:,0]

plt.plot(x, y1, label="observed")
plt.plot(x, y2, label="predicted")
plt.title("2013년 영암 태양광 발전소 발전량 예측값과 관측값 devset")
plt.xlabel("시간")
plt.ylabel("발전량(kWh)")
plt.legend()
plt.show()

# test
dataset = test_dataframe.values
x = dataset[100:300,0]
y1 = dataset[100:300,5]
dataset = test_prediction_dataframe.values
y2 = dataset[100:300,0]
# y3 = y1-y2

plt.plot(x, y1, label="observed")
plt.plot(x, y2, label="predicted")
# plt.plot(x, y3, label="MAE")

plt.title("2013년 영암 태양광 발전소 발전량 예측값과 관측값 testset")
plt.xlabel("시간")
plt.ylabel("발전량(kWh)")
plt.legend()
plt.show()
