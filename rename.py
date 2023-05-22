import os

print("Please input file path")
dir_path = input()
if not os.path.isdir(dir_path):
    print("not exist")
    exit()
print("Please input file name")
file_name = input()
print("Please input type(int) of file")
file_type = input()
while not file_type.isdecimal():
    print("Please input number")
    file_type = input()
files = os.listdir(dir_path)
file_count = len(files)
for i in range(file_count):
    os.rename(dir_path + "/" + files[i], dir_path + "/" + "/image_{:0=4}.jpg".format(i))
    print("dataset/101_ObjectCategories/RowImgs/"+ file_name +"/image_{:0=4}.jpg ".format(i) + str(file_type))

