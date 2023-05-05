import asyncio
import aioschedule 
from datetime import datetime, time

async def notify_on_friday():
    print("Пятница, 18:00! Настало время уведомления.")

# Запускаем уведомление каждую пятницу в 18:00
aioschedule.every().friday.at("18:00").do(asyncio.create_task, notify_on_friday())


async def main():
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

asyncio.run(main())




