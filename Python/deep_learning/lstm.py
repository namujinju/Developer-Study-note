## 1. 모듈 불러오기
import numpy as np
import math
import matplotlib as mpl
from matplotlib.image import imread
from random import randint

# import theano
import keras
import pandas

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.wrappers.scikit_learn import KerasClassifier
from keras import optimizers
import keras.utils
import keras.layers
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import AdaBoostClassifier
import copy
import csv


# mpl.use('Agg') # plot을 non_GUI backend로 불러옴

import matplotlib.pyplot as plt

DATASET_PATH = "../Datasets/" # 불러올 Dataset의 경로 정의
#%%
## 2. 함수들 정의
## 1) normalize_data
## 2) import_data: 데이터 import와 전처리
## 3) build_model: Keras RNN model을 만들어 return
## 4) write_to_csv: csv에 예측값을 저장
## 5) evaluate: 하나의 모델에 기초해 train, develop, test 모델의 MSE(Mean Squared Error) error values값 return -> 안 쓰임
## 6) mse: 예측값과 관측값의 평균 제곱 오차 계산

# 데이터의 y값을 0~1로 정규화하는 함수 정의
def normalize_data(dataset, data_min, data_max):
    data_std = (dataset - data_min) / (data_max - data_min)
    test_scaled = data_std * (np.amax(data_std) - np.amin(data_std)) + np.amin(data_std)

    # amax 함수: flatten된 data 전체 중 max인 값
    return test_scaled

# 데이터 import와 미래 적용을 위한 전처리
def import_data(train_dataframe, dev_dataframe, test_dataframe):
    dataset = train_dataframe.values # pandas로 가져온 train_dataframe의 모든 값을 가져오기.
    dataset = dataset.astype('float32')
    
    
    #Include all 12 initial factors (Year ; Month ; Hour ; Day ; Cloud Coverage ; Visibility ; Temperature ; Dew Point ;
    #Relative Humidity ; Wind Speed ; Station Pressure ; Altimeter
    
    # 발전량 값 중 max, min을 가져와서 scale_factor 계산
    max_test = np.max(dataset[:,5]) # 발전량 값 중 max값
    min_test = np.min(dataset[:,5])
    scale_factor = max_test - min_test
    max = np.empty(6) # max값 초기화(쓰레기값)
    min = np.empty(6)
    

    # Create training dataset
    # 각각의 열에 대해 최소, 최대값 구하고 정규화하기
    for i in range(0,6):
        min[i] = np.amin(dataset[:,i],axis = 0) 
        max[i] = np.amax(dataset[:,i],axis = 0)
        dataset[:,i] = normalize_data(dataset[:, i], min[i], max[i])

    train_data = dataset[:,0:5]
    train_labels = dataset[:,5]

    # Create dev dataset
    dataset = dev_dataframe.values
    dataset = dataset.astype('float32')

    for i in range(0, 6):
        dataset[:, i] = normalize_data(dataset[:, i], min[i], max[i])

    dev_data = dataset[:,0:5]
    dev_labels = dataset[:,5]
    

    # Create test dataset
    dataset = test_dataframe.values
    dataset = dataset.astype('float32')

    for i in range(0, 6):
        dataset[:, i] = normalize_data(dataset[:, i], min[i], max[i])

    test_data = dataset[:, 0:5]
    test_labels = dataset[:, 5]

    return train_data, train_labels, dev_data, dev_labels, test_data, test_labels, scale_factor
    #train, dev, test 각각의 기상 데이터, 발전량을 return, scale_factor도 return

# Keras RNN model을 만들어 return
def build_model(init_type = 'glorot_uniform', optimizer = 'adam', num_features = 5):
    model = Sequential()
    layers = [num_features, 64, 64, 1, 1]
    model.add(keras.layers.LSTM(
        layers[0],
        input_shape = (None, num_features),
        return_sequences=True))
    model.add(keras.layers.Dropout(0.2))

    model.add(keras.layers.LSTM(
        layers[1],
        kernel_initializer = init_type,
        return_sequences=True
        #bias_initializer = 'zeros'
    ))
    # Dropout layer randomly sets input units to 0 with a frequency of rate at each step during training time
    # 과적합 방지를 위해 중간층 노드를 강제로 없애는 드롭아웃
    model.add(keras.layers.Dropout(0.2)) 
    
    model.add(Dense(
        layers[2], activation='tanh',
        kernel_initializer=init_type,
        input_shape = (None, 1)
        ))
    model.add(Dense(
        layers[3]))

    model.add(Activation("relu"))

    #Alternative parameters:
    #momentum = 0.8
    #learning_rate = 0.1
    #epochs = 100
    #decay_rate = learning_rate / 100
    #sgd = keras.optimizers.SGD(lr=learning_rate, momentum=momentum, decay=decay_rate, nesterov=False)
    #model.compile(loss="binary_crossentropy", optimizer=sgd)
    rms = keras.optimizers.RMSprop(lr=0.002, rho=0.9, epsilon=1e-08, decay=0.01)
    model.compile(loss="mean_squared_error", optimizer=optimizer)

    return model

# Save output predictions for graphing and inspection
# csv에 예측값을 저장
def write_to_csv(prediction, filename):
    print("Writing to CSV...")
    with open(filename, 'w') as file:
        for i in range(prediction.shape[0]): # prediction.shape[0]는 자료 행의 갯수
            file.write("%.7f" % prediction[i][0][0])
            file.write('\n')
    print("...finished!")

# 안 쓰이는 함수
# 하나의 모델에 기초해 train, develop, test 모델의 MSE(Mean Squared Error) error values값 return
# def evaluate(model, X_train, Y_train, X_dev, Y_dev, X_test, Y_test, scale_factor):
#     scores = model.evaluate(X_train, Y_train, verbose = 0) * scale_factor * scale_factor
#     print("train: ", model.metrics_names, ": ", scores)
#     scores = model.evaluate(X_dev, Y_dev, verbose = 0) * scale_factor * scale_factor
#     print("dev: ", model.metrics_names, ": ", scores)
#     scores = model.evaluate(X_test, Y_test, verbose = 0) * scale_factor * scale_factor
#     print("test: ", model.metrics_names, ": ", scores)


# 예측값과 관측값의 평균 제곱 오차 계산
def mse(predicted, observed):
    
    return np.sum(np.multiply((predicted - observed),(predicted - observed)))/predicted.shape[0]
    # predicted.shape[0]는 자료 행의 갯수

#%%
## 3. 메인 함수의 시작

def main():
    # plt.switch_backend('tkAgg')

    # Import test data(6027행, 13열)
    # pandas로 csv 파일을 읽고 dataframe으로 변환해 가져오기
    train_dataframe = pandas.read_csv(DATASET_PATH + '목포_2013년_train.csv', sep=",", engine='python', header = None)
    dev_dataframe = pandas.read_csv(DATASET_PATH + '목포_2013년_dev.csv', sep=",", engine='python', header = None)
    test_dataframe = pandas.read_csv(DATASET_PATH + '목포_2013년_test.csv', sep=",", engine='python', header = None)
    train_data, train_labels, dev_data, dev_labels, test_data, test_labels, scale_factor = import_data(train_dataframe, dev_dataframe, test_dataframe)
    

    time_steps = 1
    assert(train_data.shape[0] % time_steps == 0) # 1시간 마다, 시간 단위가 정수인지 확인

    X_train = np.reshape(train_data, (train_data.shape[0] // time_steps, time_steps, train_data.shape[1])) #(7008,1,5)
    X_dev = np.reshape(dev_data, (dev_data.shape[0] // time_steps, time_steps, dev_data.shape[1]))
    X_test = np.reshape(test_data, (test_data.shape[0] // time_steps, time_steps, test_data.shape[1]))
    Y_train = np.reshape(train_labels, (train_labels.shape[0] // time_steps, time_steps, 1)) #(7008,1,1)
    Y_dev = np.reshape(dev_labels, (dev_labels.shape[0] // time_steps, time_steps, 1))
    Y_test = np.reshape(test_labels, (test_labels.shape[0] // time_steps, time_steps, 1))

    model = build_model('glorot_uniform', 'adam')

#%%
    #표준 vanilla LSTM 모델

    model_fit_epochs = 100 # epoch: 전체 Dataset을 학습시키는 정도
    print("X_train shape: ",X_train.shape, " Y_train shape: ",Y_train.shape)
    
    model.fit(
        X_train, Y_train,
        batch_size = 16, epochs = model_fit_epochs)
    
    trainset_predicted = model.predict(X_train)
    devset_predicted = model.predict(X_dev)
    testset_predicted = model.predict(X_test)

    print("Train MSE: ", mse(trainset_predicted, Y_train) * scale_factor * scale_factor)
    print("Dev MSE: ", mse(devset_predicted, Y_dev) * scale_factor * scale_factor)
    print("Test MSE: ", mse(testset_predicted, Y_test) * scale_factor * scale_factor)
    

    # #Adaboost model (ensemble learning)

    # #cv_model = KerasClassifier(build_fn=build_model, epochs=100, batch_size=16, verbose=0)
    # adaboost = AdaBoostClassifier(base_estimator=build_model, learning_rate=0.01, algorithm='SAMME')
    # adaboost.fit(train_data, train_labels)

    # trainset_predicted = adaboost.predict(X_train)
    # devset_predicted = adaboost.predict(X_dev)
    # testset_predicted = adaboost.predict(X_test)

    # print("Train MSE: ", mse(trainset_predicted, Y_train) * scale_factor * scale_factor)
    # print("Dev MSE: ", mse(devset_predicted, Y_dev) * scale_factor * scale_factor)
    # print("Test MSE: ", mse(testset_predicted, Y_test) * scale_factor * scale_factor)

    # # K-fold cross validation (K = 10):
    # kf = KFold(n_splits=10, shuffle=True)
    # # Loop through the indices the split() method returns
    # for index, (train_indices, val_indices) in enumerate(kf.split(X_train, Y_train)):
    #     print("Training on fold " + str(index + 1) + "/10...")
    #     # Generate batches from indices
    #     xtrain, xval = X_train[train_indices], X_train[val_indices]
    #     ytrain, yval = Y_train[train_indices], Y_train[val_indices]
    #     # Clear model, and create it
    #     model = None
    #     model = build_model()

    #     model.fit(
    #         xtrain, ytrain,
    #         batch_size=16, epochs=model_fit_epochs)
    #     testset_predicted = model.predict(xval)
    #     print("Test MSE: ", mse(testset_predicted, yval))

    # Grid search to optimize model params
    
    # 모델 최적화
    # init = ['glorot_uniform'] # ['uniform', 'normal', 'glorot_uniform']
    # epochs = [100]
    # batches = [16]
    # optimizers = ['rmsprop'] # ['rmsprop', 'adam']
    # optimal_params = np.empty(4)
    # minimum_error = 2e63

    # for init_type in init:
    #     for epoch in epochs:
    #         for batch in batches:
    #             for optimizer in optimizers:
    #                 model = None
    #                 model = build_model(init_type, optimizer)

    #                 model.fit(
    #                     X_train, Y_train,
    #                     batch_size=batch, epochs=epoch)
    #                 predicted = model.predict(X_test)
    #                 error = mse(predicted, Y_test)
    #                 print([init_type, epoch, batch, optimizer], error)
    #                 if error < minimum_error:
    #                     minimum_error = error
    #                     optimal_params = [init_type, epoch, batch, optimizer]

    # print("optimal params: ", optimal_params)
    # print("minimized error: ", minimum_error)
#%%


    # with open('my_trainset_mse.csv', 'w') as file:
    #     for i in range(prediction[0]): # prediction.shape[0]는 자료 행의 갯수
    #         file.write("%.7f" % prediction[i][0][0])
    #         file.write('\n')

    trainset_predicted = model.predict(X_train) * scale_factor
    devset_predicted = model.predict(X_dev) * scale_factor
    testset_predicted = model.predict(X_test) * scale_factor

    write_to_csv(trainset_predicted,'my_trainset_prediction.csv')
    write_to_csv(devset_predicted,'my_devset_prediction.csv')
    write_to_csv(testset_predicted, 'my_testset_prediction.csv')


#%%
# 현재 모델을 2014년에 적용    
    # test_dataframe = pandas.read_csv(DATASET_PATH + '목포 2014년.csv', sep=",", engine='python', header = None)
    # train_data, train_labels, dev_data, dev_labels, test_data, test_labels, scale_factor = import_data(test_dataframe, test_dataframe, test_dataframe)

    # time_steps = 1
    # assert(train_data.shape[0] % time_steps == 0) # 1시간 마다, 시간 단위가 정수인지 확인

    # X_train = np.reshape(train_data, (train_data.shape[0] // time_steps, time_steps, train_data.shape[1])) #(7008,1,5)
    # X_dev = np.reshape(dev_data, (dev_data.shape[0] // time_steps, time_steps, dev_data.shape[1]))
    # X_test = np.reshape(test_data, (test_data.shape[0] // time_steps, time_steps, test_data.shape[1]))
    # Y_train = np.reshape(train_labels, (train_labels.shape[0] // time_steps, time_steps, 1)) #(7008,1,1)
    # Y_dev = np.reshape(dev_labels, (dev_labels.shape[0] // time_steps, time_steps, 1))
    # Y_test = np.reshape(test_labels, (test_labels.shape[0] // time_steps, time_steps, 1))

    # model = build_model('glorot_uniform', 'adam')

    # model_fit_epochs = 100 # epoch: 전체 Dataset을 학습시키는 정도
    # print("X_train shape: ",X_train.shape, " Y_train shape: ",Y_train.shape)
    
    # model.fit(
    #     X_train, Y_train,
    #     batch_size = 16, epochs = model_fit_epochs)

    # testset_predicted = model.predict(X_test) * scale_factor

    # write_to_csv(testset_predicted, 'my_testset_prediction_2014.csv')

    return

if __name__ == '__main__':
    print("main 함수의 시작")
    main()
