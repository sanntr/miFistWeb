import requests as r
key_article=''
#fecha limite 
# date=''#aa-mm-dd
# item=''    
# language=''# catalogo
# category=''#business entertainment general health science sports technology
# search='g' #or top-headlines, everything

def api_request(search, item, category, date='',language=""):
    url=f'https://newsapi.org/v2/{search}?q={item}&category={category}&from={date}&apiKey={key_article}'
    return url

def data_api(url):
    respons= r.get(url)
    print(respons)
    if respons.status_code == 200:
        return respons.json()
    else:
        return None

def data_articles(data):
    try:
        if data:
            return data.get('articles') 
        else: 
            return None
    except:
        return None
    
def leng_docs():
    data=data_api()
    if data:
        return data.get('totalResults')
    else:
        return None



# print(r.get(url).json())
# print(dataArticles())




    

