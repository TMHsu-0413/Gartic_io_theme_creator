# Gartic io題目輸入器

## 簡介
- 爬取livetv,巴哈動畫瘋,木棉花官網的動漫名稱。

## 操作

1. 爬資料
```python=
python crawler.py
```
執行後會產生一個output.csv

2. 生成字串
```python=
python trans_to_data.py
```
執行後會產生一個items.txt

3. 開啟gartic.io，並到生成主題的頁面
4. 開啟console.js，並把裡面全部的code貼到瀏覽器的console
5. 開啟items.txt，並把全部複製貼到瀏覽器的console
6. 在瀏覽器的console輸入 add(data)
7. 完成

## Bug
- 會抓到一些特殊符號，例如：全形標點符號,星星符號...，要把這些處理成空格
- 資料筆數有點太少
