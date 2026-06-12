import contextvars
import asyncio

status_var = contextvars.ContextVar('status', default='idle')

async def async_task():
    status_var.set('running')
    print(f'Task status: {status_var.get()}')
    await asyncio.sleep(1)
    status_var.set('completed')

async def main():
    await async_task()
    print(f'Status at end: {status_var.get()}')

asyncio.run(main())
# Fungsi: Menggunakan context vars untuk melacak status dalam eksekusi asinkron.
# Kondisi: Ketika Anda ingin memisahkan status antara berbagai eksekusi tugas.