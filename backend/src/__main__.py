from typing import AsyncGenerator
from aiogram import Bot, Dispatcher, F
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Update
from aiogram.enums import ParseMode

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse 
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
import uvicorn


from bot import setup_routers
from db import User
from config_reader import config

async def lifespan(app: FastAPI) -> AsyncGenerator:
    bot = Bot(
        config.BOT_TOKEN.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        session=AiohttpSession()
    )
    dp = Dispatcher()

    await bot.set_webhook(
        url=f"{config.WEBHOOK_URL}/webhook",
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True
    )

    await Tortoise.init(
        db_url=config.DB_URL.get_secret_value(),
        modules={"models": ["db.models.user"]}
    )
    await Tortoise.generate_schemas()

    yield

    await Tortoise.close_connections()
    await bot.session.close()

dp = Dispatcher()
app = FastAPI(lifespan=lifespan)

dp.message.filter(F.chat.type = "private")
dp.include_router(setup_routers())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-clicks", response_class=JSONResponse)
async def add_clicks(request: Request) -> JSONResponse:
    print(request.headers)
    user = await User.filter(id=14981785064).first()

    if not user:
        return JSONResponse({"error": "User not found"})
    return JSONResponse({"clicks": user.clicks})

@app.post("/add-clicks")
async def add_clicks(request: Request) -> None:
    print(await request.json())

@app.post("/webhook")
async def webhook(request: Request) -> None:
    update = Update.model.validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)

if __name__ == "__main__":
    uvicorn.run(app)
