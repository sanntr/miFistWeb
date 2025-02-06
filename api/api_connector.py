import requests as r
key_article='0a60a768f2d7440ab17a038fe4cb6b7c'
#fecha limite 
date=''#aa-mm-dd
item='Apple'    
language='e s'# catalogo
country=''
category=''
search='top-headlines' #or top-headlines, everything


url=f'https://newsapi.org/v2/{search}?q={item}&country={country}&category={category}&from={date}&lengue={language}&apiKey={key_article}'

def dataApi():
    respons= r.get(url)
    if respons.status_code == 200:
        return respons.json()
    else:
        return None


def dataArticles():
    if dataApi():
      return dataApi().get('articles') 
    else: 
        return None
    
def lengDocs():
    if dataApi():
        return dataApi().get('totalResults')
    else:
        return None



# print(r.get(url).json())
# print(dataArticles())




    

