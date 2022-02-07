import wikipedia
import wikipediaapi
import json
import sys
import os

class WikiExtractor:
    def __init__(self):
        print('Initializing Wiki-Extractor')
        self.wiki = wikipediaapi.Wikipedia('en',extract_format=wikipediaapi.ExtractFormat.WIKI)        

    def get_links(self,q:str, num_links=10, output=None):
        if output is None:
            output = q+'.json'
        pages = wikipedia.search(q, results=num_links) 
        links = []
        for page in pages:
            wiki_page = self.wiki.page(page)
            page_dict = dict()
            page_dict['url'] = wiki_page.fullurl
            page_dict['paragraph'] = wiki_page.summary
            links.append(page_dict)
        output = os.path.join(os.getcwd(),output)    
        with open(output,'w') as out:
            json.dump(links,out)


keyword = "Random"
num_urls = 10
output_path = ""
keys = ['--keyword=','--num_urls=','--output=']

try:
    for i in range(1,len(sys.argv)):
        for key in keys:
            if sys.argv[i].find(key)==0:
                if key==keys[0]:
                    keyword = sys.argv[i].split('=')[1]
                elif key==keys[1]:
                    num_urls = sys.argv[i].split('=')[1]
                elif key==keys[2]:
                    output_path=sys.argv[i].split('=')[1]
                break
    print(f'Searching {num_urls} wikipedia links for {keyword}')
    WikiExtractor().get_links(q=keyword,num_links=num_urls,output=output_path)
    print('\n\nCompleted')
except:
    print('Some error occured, please try again')