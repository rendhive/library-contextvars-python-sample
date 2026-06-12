import contextvars
import asyncio

request_var = contextvars.ContextVar('request_var')

async def request_handler(request_id):
    request_var.set(request_id)
    print(f"Handling request: {request_var.get()}")
    await asyncio.sleep(2)

async def main():
    tasks = [request_handler(i) for i in range(3)]
    await asyncio.gather(*tasks)

asyncio.run(main())
# Fungsi: Mengelola request bersamaan dengan context vars.
# Kondisi: Ketika Anda ingin memisahkan request untuk setiap task koncurrent.