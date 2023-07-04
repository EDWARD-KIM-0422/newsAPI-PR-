
from typing import Union
from pydantic import BaseModel
import requests
from fastapi import FastAPI



app = FastAPI()



#commit
#(python -m uvicorn newsapi:app --reload   ->서버여는 키)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/api/v2/newsapi")  
# ( http://127.0.0.1:8000+"내가 지정한 경로") 
def news_api():  
    q = 'cat' 
    api = '8ec2109c834d4af1b4e7aaea3f56a85d                '
    response = requests.get('https://newsapi.org/v2/everything'\
                        , params={'q':{q},'from':'2023-06-30','sortBy':'popularity','apiKey':{api}}) 
    print(response.text) 
    data = response.json()    
    return {"articles": data["articles"]}                                                                                          


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = "None"):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}