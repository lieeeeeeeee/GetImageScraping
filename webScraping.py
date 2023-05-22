from icrawler.builtin import GoogleImageCrawler
import os

print("Please input data that you want to search")
serch_Keyword = input()
print("Please input number of images that you want to download")
image_num = input()
while not image_num.isdecimal():
    print("Please input number")
    image_num = input()
folderName = serch_Keyword.replace(" ", "-").replace("　", "-")
dir_path = "Downloads/" + folderName
if not os.path.isdir(dir_path):
    os.makedirs(dir_path)
google_crawler = GoogleImageCrawler(storage={'root_dir': dir_path})
google_crawler.crawl(keyword=serch_Keyword, max_num=int(image_num))
print("Download complete")
print("dir_path: "+dir_path)

