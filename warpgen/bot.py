import json
from http import HTTPStatus
from telegram import Update
from warpgen.bot import create_app

async def handler(request):
    try:
        # Инициализируем приложение
        app = create_app()
        await app.initialize()
        
        # Получаем данные от Telegram
        data = await request.json()
        update = Update.de_json(data, app.bot)
        
        # Обрабатываем обновление
        await app.process_update(update)
        
        return {
            "statusCode": HTTPStatus.OK,
            "body": json.dumps({"ok": True})
        }
    except Exception as e:
        return {
            "statusCode": HTTPStatus.INTERNAL_SERVER_ERROR,
            "body": json.dumps({"error": str(e)})
        }
    finally:
        await app.shutdown()
