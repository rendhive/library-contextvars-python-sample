import contextvars
from aiohttp import web

request_var = contextvars.ContextVar('request_var', default='')

async def middleware_handler(request):
    request_var.set('Handling request')
    print(request_var.get())  # Output var kontekstual
    return web.Response(text="Hello, World!")

app = web.Application(middlewares=[middleware_handler])
web.run_app(app)
# Fungsi: Menangani state dalam middleware untuk context request.
# Kondisi: Ketika Anda ingin mengatur konteks request dalam aplikasi web async.