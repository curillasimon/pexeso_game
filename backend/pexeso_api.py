from fastapi import FastAPI, Body #parameter (size) má byť načítaný z tela požiadavky (body)
from pexeso_game import PexesoGame
from pydantic import BaseModel
import uvicorn


app = FastAPI()


class GuessInput(BaseModel):
    x1: int
    y1: int
    x2: int
    y2: int


@app.get("/")
def root():
    return {"message": "Vitaj v Pexeso API!"}

@app.post("/new-game")
def new_game(size: int = Body()):
    global game
    game = PexesoGame(size)
    return{"message": f"Nová hra vytvorená s veľkosťou {size}"}

@app.get('/board')
def get_board():
    return{"board": game.get_board_view().split("\n")}

@app.get('/revelaed')
def get_revealed():
    return{"revealed": game.revealed}

@app.post("/guess")
def guess(data:GuessInput):
    match, message = game.guess_pair(data.x1, data.y1, data.x2, data.y2)
    board_view = game.get_board_view(reveal_temp =[(data.x1,data.y1), (data.x2,data.y2)])

    return{
        "success": match,
        "message": message,
        "board": board_view.split("\n"),
        "revealed": game.revealed,
        "complete": game.is_complete()
    }

