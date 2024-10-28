import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

browser = webdriver.Chrome()
parsed_data = []
url = "https://www.divan.ru/kazan/category/divany-i-kresla"

#Функция для добавления данных в parsed_data
def append_parsed_data(url):
    print("Start parsing")
    browser.get(url)
    time.sleep(3)

    divans = browser.find_elements(By.CSS_SELECTOR,"div.WdR1o")
    # print(divans)
    for divan in divans:
        try:
            price = divan.find_element(By.CSS_SELECTOR,"div.pY3d2").find_element(By.TAG_NAME,"span").text
            price = float(price.replace(' ','').strip("руб."))
            # print(price)
        except:
            print("Произошла ошибка при парсинге")
            continue
        parsed_data.append([price])
    print("Finish parsing of one page")

#Функция для записи в файл
def write_data_to_csv(parsed_data,filename):
    with open(filename,'w',encoding='utf-16') as file:
        writer = csv.writer(file)
        writer.writerow(['Цена'])
        writer.writerows(parsed_data)
    print("File was written")

#Парсим данные с 3 страниц сайта (все 40 страниц будут очень долго грузиться)
for i in range(1,4):
    append_parsed_data(url+'/page-'+str(i))
browser.quit()

#Записываем данные в файл
write_data_to_csv(parsed_data,'divans.csv')

