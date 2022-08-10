
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app = FastAPI()


@app.get("/")
def index():
    return {"data": {"name":"Mahabub"}}

@app.get('/blog')
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    #only published 10 blogs
    if published:

        return {"data": f'{limit} blogs Data published'}
    else:
        return {"data": f'{limit} blogs Data unpublished'}

@app.get('/blog/unpublished')
def unpublished():
    return {"data": 'unpublished Data'}


@app.get("/blog/{id}")
def blog(id:int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id,limit=10 ):
    # return limit
    return {"data": {'1','2'}}

class Blog(BaseModel):
   
    title: str
    description: str 
    published_at: Optional[bool]
 
@app.post("/blog/create")
def create_blog(request:Blog):

    # return limit
    return {"data": f'Blog is created with title: {request.title}'}

# new port open for debug
# if __name__=="__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000)