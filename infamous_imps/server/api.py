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
    """Post new message to server """
    data = request.post()
    server = request.match_info['server']
    timestamp = time.time()
    user = data["user"]
    message = data["message"]
    add_message(server,timestamp,user,message)
   

@routes.post("/api/cv1/player/delete/{name}&hash={hashed}")
async def del_user(request):
    """ Delete user from the server """
    data = request.post()
    print(request)
    name = request.match_info['name']
    hashed = request.match_info['hashed']
    delete_user(name, hashed)
    
    
@routes.post("/api/v1/player/create/{name}?password={hash}")
async def new_user(request):
    """ Adds user to the server """
    print(request)
    name = request.match_info['name']
    hashed = request.match_info['hash']
    add_user(name, hashed)
@routes.post("/api/cv1/player/update/{name}?name={new_name}?password={hashed}")
async def update_user(request):
    """Update user credentials"""
    print(request)
    name = request.match_info['name']
    hashed = request.match_info['hashed']
    new_name = request.match_info['new_name']
    update_user_name(name, hashed, new_name)


app.add_routes(routes)
