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
    for i in range(len(name)):
        cur = name[i]
        # 截斷 第x季...
        if cur == '（' or cur == '第':
            return temp[:i]
        elif (i+1) < len(name) and cur == ' ' and name[i+1].isalpha():
            return temp[:i]
        # 漢字
        elif '\u4e00' <= cur <= '\u9fa5' or cur == '，' or cur == '、' or cur == '！' or cur == '－':
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
            if i != 0:
                temp = temp[:i] + ' ' + temp[i+1:]
            else:
                temp = temp[1:]
    #print(temp)
    return temp

def cmp(a,b):
    ct = 0
    for i in range(min(len(a),len(b))):
        if (a[i] == b[i]):
            ct+=1
    return ct / min(len(a),len(b)) if min(len(a),len(b)) != 0 else 0

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
            name = ''.join(ani.text).strip()
            name = only_contain_chinese(name)
            for el in all_dict:
                if cmp(name,el) >= 0.7:
                    duplicate = True
                    break
            if not duplicate:
                all_dict.add(name)
        driver.close()

def baha_crawler():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
    }
    for page in range(1,22):
        print(f'parsing bahamut {page} page ...')
        url = f'https://ani.gamer.com.tw/animeList.php?page={page}&c=All&sort=2'
        r = requests.get(url,headers=headers)
        soup = BeautifulSoup(r.text,'html.parser')
        all_ani = soup.find_all('p', class_="theme-name")
        for ani in all_ani:
            name = ''.join(ani.text).strip()
            name = only_contain_chinese(name)
            duplicate = False
            for el in all_dict:
                if cmp(name,el) >= 0.7:
                    duplicate = True
                    break
            if not duplicate:
                all_dict.add(name)

def muse_crawler():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
    }
    for page in range(1,32):
        url = f'https://www.e-muse.com.tw/zh/animation_cat/anime-head/?page={page}'
        print(f'parsing muse {page} page ...')
        r = requests.get(url,headers=headers)
        soup = BeautifulSoup(r.text,'html.parser')
        all_ani = soup.find_all('p', class_="p-18 txt-bold")
        for ani in all_ani:
            name = ''.join(ani.text).strip()
            name = only_contain_chinese(name)
            duplicate = False
            for el in all_dict:
                if cmp(name,el) >= 0.7:
                    duplicate = True
                    break
            if not duplicate:
                all_dict.add(name)

# 太多垃圾
def wiki_crawler():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
    }
    for year in range(2012,2024):
        url = f'https://zh.wikipedia.org/zh-tw/{year}%E5%B9%B4%E6%97%A5%E6%9C%AC%E5%8B%95%E7%95%AB%E5%88%97%E8%A1%A8'
        print(f'parsing wiki {year} year anime ...')
        r = requests.get(url,headers=headers)
        soup = BeautifulSoup(r.text,'html.parser')
        table = soup.find_all('table', class_="wikitable")
        for i in range(4):
            anime_row = table[i].find_all('tr')
            for anime in anime_row[1:]:
                anime_name = anime.find_all('td')
                if (len(anime_name) >= 2):
                    if (anime_name[1].find('a') != None):
                        name = ''.join(anime_name[1].find('a').text).strip()
                    else:
                        name = ''.join(anime_name[1].text).strip()
                    name = only_contain_chinese(name)
                    duplicate = False
                    for el in all_dict:
                        if cmp(name,el) >= 0.7:
                            duplicate = True
                            break
                    if not duplicate:
                        all_dict.add(name)
def myself_crawler():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
    }
    url = f'https://myself-bbs.com/portal.php?mod=topic&topicid=8'
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')
    anime_div = soup.find_all('div', class_="module cl xl xl1")
    for div in anime_div:
        row = div.find_all('li')
        for r in row:
            name = ''.join(r.find('a').text).split('／')[0]
            name = only_contain_chinese(name)
            duplicate = False
            for el in all_dict:
                if cmp(name,el) >= 0.7:
                    duplicate = True
                    break
            if not duplicate:
                all_dict.add(name)

#wiki_crawler()  
myself_crawler()
baha_crawler()
#muse_crawler()
#line_crawler()
with open('output.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile,delimiter=' ')
    for el in sorted(all_dict):
        writer.writerow([el])
