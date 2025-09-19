from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import tabulate
import time

options = ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get("https://www.youtube.com/@DanKoeTalks/videos")
time.sleep(2)
page=driver.find_element(By.TAG_NAME, "html")
for i in range(10):
    page.send_keys(Keys.END)
    time.sleep(2)
search_box = driver.find_element(By.ID, "contents")
time.sleep(2)
videos = search_box.find_elements(By.ID, "video-title")
video_list = []
print("title:")
for video in videos:
    video_list.append(video.text)
views_list=[]
dates_list=[]
videos_info = search_box.find_elements(By.ID, "metadata-line")
print("info:")
for info in videos_info:
    one_info = info.text
    parts = one_info.split("\n")
    #print(parts[0], parts[1])
    views_list.append(parts[0])
    dates_list.append(parts[1])
# Instead of this:
# print(video_list)

# Do this:
print("--- Titles ---")
for title in video_list:
    print(title)

print("\n--- Views ---")
for view in views_list:
    print(view)

print("\n--- Dates ---")
for date in dates_list:
    print(date)


print ("\n--- Tabulated Data ---")
table = zip(video_list, views_list, dates_list)
print(tabulate.tabulate(table, headers=["Title", "Views", "Date"], tablefmt="grid"))