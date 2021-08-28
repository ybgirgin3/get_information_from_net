from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
from get_sub import main


#url = "https://en.wikipedia.org//wiki/Abengoa"

url_list = main()

for url in url_list:
    if 'Category' not in url:

        fn = url.split('/')[-1]
        html = urlopen(url).read()
        soup = BS(html, features="html.parser")
        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        for p in soup.find_all('p', text=True, recursive=True):
            print("""
                {}

            """.format(fn))
            print(p)

             
        #for parag in soup.find_all('p'):
        # kill all script and style elements
        #with open(f"{fn}.txt", "a") as f:
        #  f.write(f"{text}")
