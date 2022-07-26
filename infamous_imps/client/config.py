
WIN_WIDTH = 640
WIN_HEIGHT = 480

TILE_W = 960
TILE_H = 720

TILE_SIZE = 32
PLAYER_LAYER = 3
PLAYER_SPEED = 3
GROUND_LAYER = 1
BLOCK_LAYER = 2
PICKUP_LAYER  =  PLAYER_LAYER

FPS = 60

RED = (255,0,0)
BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
GREY = (105,105,105)



def tile_map():
    win_w = int(TILE_W/32)
    win_h =  int(TILE_H/32)
    print(win_w, win_h)
    tilemap = [[0 for x in range(win_w)] for x in range(win_h)]
    for i in range(win_h):
        for j in range(win_w):
            if i == 0 or j == 0:
                tilemap[i][j] = 1
            if i == win_h-1 or j == win_w-1:
                tilemap[i][j] = 1
    px = int(WIN_HEIGHT/64)
    py = int(WIN_WIDTH/64)
    tilemap[px][py] = 2
    return tilemap

tilemap =  tile_map()

            

