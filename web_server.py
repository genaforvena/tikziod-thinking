import asyncio
from aiohttp import web
from ollama import AsyncClient

async def get_ollama_continuation(word, context):
    client = AsyncClient()
    prompt = f"Continue the following sentence that contains the word '{word}': {context}"
    response = await client.chat(model='llama2', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

async def get_continuation(request):
    data = await request.json()
    word = data['word']
    context = data['context']
    continuation = await get_ollama_continuation(word, context)
    return web.json_response({'continuation': continuation})

async def start_server():
    app = web.Application()
    app.router.add_get('/', lambda request: web.FileResponse('intersecting_texts.html'))
    app.router.add_post('/get_continuation', get_continuation)
    app.router.add_static('/static', 'docs/static')

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    print("Server started at http://localhost:8080")
    print("Press Ctrl+C to stop the server")

    # Keep the server running
    while True:
        await asyncio.sleep(3600)
