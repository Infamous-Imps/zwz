from aiohttp import web
import aiohttp_jinja2
import jinja2
import time
from dba import add_message,delete_user,add_user,update_user_name


app = web.Application()
aiohttp_jinja2.setup(app,loader=jinja2.FileSystemLoader(["templates","server/templates"]))
routes = web.RouteTableDef()


@routes.post("/chat/{server}")
async def chat(request):
    """post new message to server """
    data = await request.post()
    server = request.match_info['server']
    timestamp = time.time()
    user = data["user"]
    message = data["message"]
    add_message(server,timestamp,user,message)
   

@routes.post("/api/cv1/player/delete/{name}")
async def del_user(request):
    """ delete user from the server """
    print(request)
    data = await request.post()
    name = request.match_info['name']
    delete_user(name, hashed)
    
    
@routes.post("/api/v1/player/create/{name}?password={hash}")
async def new_user(request):
    """ adds user to the server """
    print(request)
    data = await request.post()
    name = request.match_info['name']
    hashed = request.match_info['hash']
    add_user(name, hashed)
@routes.post("/api/cv1/player/update/{name}?name={new_name}?password={hashed}")
async def update_user(request):
    """update user credentials"""
    print(request)
    data = await request.post()
    name = request.match_info['name']
    hashed = request.match_info['hash']
    update_user_name(name, hashed, new_name)


app.add_routes(routes)
