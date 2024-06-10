from aiogram import Router
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config_reader import config

router= Router()
markup = (
      InlineKeyboardBuilder()
      .button(text="Open", web_app=WebAppInfo(url=config.WEBAPP_URL))
) .as_markup()


@router.message(CommandStart())
async def start(message: Message) -> None:
        await message.answer("Let's Bong!", reply_markup=markup)