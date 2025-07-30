import asyncio
from aiogram import Bot, Dispatcher
from handlers import start

API_TOKEN = "7253351659:AAHIlLIZx8FdKuOcFRJzXvn1CfHjhQne4ts"

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.include_router(start.router)
    print("✅ SmartПрораб запущено!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
