import contextvars
import asyncio

api_context = contextvars.ContextVar('api_context')

async def api_request(id):
    api_context.set(f'Context for API {id}')
    print(api_context.get())

async def main():
    await asyncio.gather(api_request(1), api_request(2))

asyncio.run(main())
# Fungsi: Menghubungkan context vars dalam konteks API.
# Kondisi: Ketika Anda ingin menjaga informasi untuk eksekusi API yang berbeda.