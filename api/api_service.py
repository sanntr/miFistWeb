# from .api_connector import dataArticles 
from .api_connector import api_request, data_api, data_articles

def process_articles(search, item ,category):
   try:
        data=api_request(search, item,category )
        print(data)
        data=data_api(data)
        data=data_articles(data)

        result=[]
        for i in data:
            source=i.get('source',[]).get('name',[])
            author=i.get('author',[])
            title=i.get('title',[])
            description=i.get('description',[])
            url_doc=i.get('url',[])
            urlToImage=i.get('urlToImage',[])
            content=i.get('content',[])

            
            data_article={
                'name':verify_data(source),
                'author':verify_data(author),
                'title': verify_data(title),
                'description':verify_data(description),
                'url_doc': verify_data(url_doc),
                'urlToImage': urlToImage,
                'content':  content.split('[')[0]
            }
            result.append(data_article)
        return result
   except:
        print(len(result))
        if len(result) == 0:
            return None
        return result
   
def verify_data(data):
            if data == None:
                return ''
            else: return data   

