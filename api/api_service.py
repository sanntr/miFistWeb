# from .api_connector import dataArticles 
from .api_connector import dataArticles
def inData():
    data=dataArticles()
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
            'name':verifData(source),
            'author':verifData(author),
            'title': verifData(title),
            'description':verifData(description),
            'url_doc': verifData(url_doc),
            'urlToImage': urlToImage,
            'content': clearString(content)
        }
        result.append(data_article)

    return result


def verifData(data):
    if data == None:
        return ''
    else: return data   

def clearString(string):
    stringR=""
    for a in string:
        if a=='[':
            break
        else: stringR=stringR+a
    return stringR
