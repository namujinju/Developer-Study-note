import pandas

DATASET_PATH = "../Datasets/"

output_reshape = pandas.read_csv(DATASET_PATH + '영암태양광 발전소 발전량 데이터-2차(2013년).csv', sep=",", engine='python', header = None)

filename = "new_output.csv"
with open(filename, 'w') as file:
    for i in range(output_reshape.shape[0]):
        for j in range(output_reshape.shape[1]): # prediction.shape[0]는 자료 행의 갯수
          
            file.write(str(output_reshape[j][i]))
            file.write('\n')
    print("...finished!")
    