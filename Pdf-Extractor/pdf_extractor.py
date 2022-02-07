# Importing packages
import pandas as pd
import requests
from pdf2image import convert_from_path
import os
import pytesseract
import PIL
import json
from bs4 import BeautifulSoup

books = pd.read_csv('Books.csv')

BOOK_PATH = './Books/'
IMAGE_PATH = './Images/'

def convert_to_images(book_name):
    book_location = BOOK_PATH+book_name
    book_images_location = IMAGE_PATH+book_name
    images = convert_from_path(book_location+'.pdf')
    os.mkdir(book_images_location)
    for i,img in enumerate(images):
        img.save(book_images_location+'/Page-'+str(i)+'.png','PNG')
    return len(images)

def read_page(page_location):
    page = page_location+'.png'
    page_string = pytesseract.image_to_string(PIL.Image.open(page,'r'), lang='hin')
    return page_string

def read_book(book_url,book_name):
    book = requests.get(book_url)
    with open(BOOK_PATH+book_name+'.pdf', 'wb') as pdf:
        pdf.write(book.content)
        pdf.close()
    num_pages = convert_to_images(book_name)
    # num_pages = 5+11
    book_string = ""
    for i in range(1,num_pages):
        page_location = IMAGE_PATH + book_name+'/Page-'+str(i)
        page_string = read_page(page_location)
        book_string+=page_string
    return book_string

books_json = []

def extract_content():
    os.mkdir('./Books/')
    os.mkdir('./Images')
    for i,url in enumerate(books['book_url'][:2]):
        print(url)
        if url[-4:]=='.pdf':
            book_details = dict()
            book_details['page-url']=url
            book_details['pdf-url']=url
            book_details['pdf-content'] = read_book(url,'Book-'+str(i))
            books_json.append(book_details)
        else:
            response = requests.get('https://archive.org/details/majhagadhoocormar/mode/2up')
            soup = BeautifulSoup(response.content)
            page = str(soup)
            while True:
                start_link = page.find("href")
                if start_link != -1:
                    start_quote = page.find('"', start_link)
                    end_quote = page.find('"', start_quote + 1)
                    url = page[start_quote + 1: end_quote]
                    if url[-4:]=='.pdf':
                        book_details = dict()
                        book_details['page-url']=url
                        book_details['pdf-url']=url
                        book_details['pdf-content'] = read_book(url,'Book-'+i)
                        books_json.append(book_details)
                        break
                    page = page[end_quote:]
                else:
                    break
    output = os.path.join(os.getcwd(),'pdf_extract.json')    
    with open(output,'w') as out:
        json.dump(books_json,out)

# Due to the long running time of the script, the output in the pdf_extract.json only shows contents from the first 5 pages of the books. 
# However, the script is such that it can extract contents from all the pages if left running. 
# It also takes care of the double columns and extracts text in readable forn
extract_content()