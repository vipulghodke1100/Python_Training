from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as chromeservice
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pypdf import PdfReader
import os
import json
import re
import time

def download_file(url):
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option('prefs',{'download.default_directory':'C:\\Traniee\\Python\\Numpy_Pandas_Assignment\\Python_Projects\\Assignment2\\down',
    'download.promt_for_download':False,
    'plugins.always_open_pdf_externally':True })
    driver=webdriver.Chrome(service=chromeservice(ChromeDriverManager().install()), options=options)
    driver.get(url)
    
def extract_text(file_path,pages):
    reader=PdfReader(file_path)
    text=''
    for i in range(pages):
        page=reader.pages[i]
        text+=page.extract_text()
        
    cin = r'[A-Z]\d{5}[A-Z]{2}\d{4}[A-Z]{3}\d{6}'
    email =r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
    phone= r'(\[-\s]?[6-9]\d{9}|[6-9]\d{9}|\d{2,5}[-\s]?\d{5,8})'
    pan= r'[A-Z]{5}[0-9]{4}[A-Z]{1}'
    date = r'(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/](\d{4})'
    website= r'\bhttps?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?\b|\bwww\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?\b'    
    
    cin_numbers=re.findall(cin ,text)
    emails=re.findall(email,text)
    phones=re.findall(phone ,text)
    pans=re.findall(pan ,text)
    dates=re.findall(date ,text)
    websites=re.findall(website ,text)
    
    print(f"count of CIN :{len(cin_numbers)}")
    print(cin_numbers)
    print(emails)
    print(phones)
    print(pans)
    print(dates)
    print(websites)
    return

def load_config():
    with open('./config.json','r') as file:
        config=json.load(file)
    urls=config.get('urls')
    pages_to_extract=config.get('pages_to_extract')
    return urls,pages_to_extract

def main():
    folder_path='./down'
    urls , pages_to_extract = load_config()
    for url in urls:
        print(url)
        download_file(url)
    time.sleep(0.5)
    for filename in os.listdir(folder_path):
        print(filename)
        if filename.endswith('.pdf'):
            file_path=f"{folder_path}/{filename}"
            print(f"------- Extacting from {filename} -------")
            extract_text(file_path ,pages_to_extract)
            
if __name__=='__main__':
    main()
