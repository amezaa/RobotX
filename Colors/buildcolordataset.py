import xlsxwriter
import random

def build_dataset_color():
    #red data
    red = random.sample(range(200,255),10)
    blue = random.sample(range(0,100),10)
    green = random.sample(range(0,100),10)

    red_data = []

    for i in red:
        for j in green:
            for k in blue:
                red_data.append([i,j,k,'red'])

    #green data
    green = random.sample(range(200,255),10)
    blue = random.sample(range(0,100),10)
    red = random.sample(range(0,100),10)

    green_data = []

    for i in red:
        for j in green:
            for k in blue:
                red_data.append([i,j,k,'green'])

    #blue data
    blue = random.sample(range(200,255),10)
    red = random.sample(range(0,100),10)
    green = random.sample(range(0,100),10)

    blue_data = []

    for i in red:
        for j in green:
            for k in blue:
                red_data.append([i,j,k,'blue'])
    blue_data

    dataset = [["R", "G", "B", "Color"]] + red_data + green_data + blue_data

    return dataset

dataset = build_dataset_color()
#print(dataset)
workbook = xlsxwriter.Workbook('../Datasets/RGBcolordatas.csv')
worksheet = workbook.add_worksheet()
row = 0
col = 0

for R,G,B,color in dataset:
    worksheet.write(row, col, R)
    worksheet.write(row, col + 1, G)
    worksheet.write(row, col + 2, B)
    worksheet.write(row, col + 3, color)
    row += 1

workbook.close()