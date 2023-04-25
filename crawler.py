import csv
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


all_dict = set()
def only_contain_chinese(name):
    temp = name
    print(name)
    for i in range(len(name)):
        cur = name[i]
        # 漢字
        if '\u4e00' <= cur <= '\u9fa5':
            continue
        # 英文字
        elif cur.isalpha():
            continue
        # 數字
        elif cur.isdigit():
            continue
        # 空格
        elif cur.isspace():
            continue
        else:
            temp.replace(cur,' ')
    print(temp)
    return temp

def cmp(a,b):
    ct = 0
    for i in range(min(len(a),len(b))):
        if (a[i] == b[i]):
            ct+=1
    return ct / min(len(a),len(b))

def line_crawler():
    locator = (By.CLASS_NAME,"huBOKl")
    for page in range(1,33):
        print(f'parsing linetv {page} page...')
        url = f'https://www.linetv.tw/channel/2/genre?page={page}&sort=VIEW_COUNT_LAST_7_DAYS&source=CHANNEL_PREDEFINED_FILTER&source_channel_id=2&source_feed_id=14'
        driver = webdriver.Safari()
        driver.get(url)
        WebDriverWait(driver,10).until(EC.presence_of_element_located(locator))
        all_anima = driver.find_elements(By.CLASS_NAME,"huBOKl")
        for ani in all_anima:
            duplicate = False
            name = ''.join(ani.text).strip().split(' ')[0]
            name = only_contain_chinese(name)
            for el in all_dict:
                if cmp(name,el) >= 0.5:
                    duplicate = True
                    break
            if not duplicate:
                all_dict.add(name)
        driver.close()

def baha_crawler():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
    }
    for page in range(1,54):
        print(f'parsing bahamut {page} page ...')
        url = f'https://ani.gamer.com.tw/animeList.php?page={page}&c=All&sort=2'
        r = requests.get(url,headers=headers)
        soup = BeautifulSoup(r.text,'html.parser')
        all_ani = soup.find_all('p', class_="theme-name")
        for ani in all_ani:
            name = ''.join(ani.text).strip().split(' ')[0]
            name = only_contain_chinese(name)
            duplicate = False
            for el in all_dict:
                if cmp(name,el) >= 0.5:
                    duplicate = True
                    break
            if not duplicate:
                all_dict.add(name)

def muse_crawler():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
    }
    for page in range(1,32):
        print(f'parsing muse {page} page ...')
        url = f'https://www.e-muse.com.tw/zh/animation_cat/anime-head/?page={page}'
        r = requests.get(url,headers=headers)
        soup = BeautifulSoup(r.text,'html.parser')
        all_ani = soup.find_all('p', class_="p-18 txt-bold")
        for ani in all_ani:
            name = ''.join(ani.text).strip().split(' ')[0]
            name = only_contain_chinese(name)
            duplicate = False
            for el in all_dict:
                if cmp(name,el) >= 0.5:
                    duplicate = True
                    break
            if not duplicate:
                all_dict.add(name)

baha_crawler()
muse_crawler()
line_crawler()
with open('output.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile,delimiter=' ')
    for el in sorted(all_dict):
        writer.writerow([el])
