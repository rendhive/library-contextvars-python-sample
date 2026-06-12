import contextvars
import asyncio

current_task = contextvars.ContextVar('current_task', default=None)

async def run_task(name):
    current_task.set(name)
    print(f"Running task: {current_task.get()}")
    await asyncio.sleep(1)

async def main():
    tasks = [run_task(f'Task {i}') for i in range(3)]
    await asyncio.gather(*tasks)

asyncio.run(main())
# Fungsi: Menggunakan variabel kontekstual untuk melacak tugas yang berjalan.
# Kondisi: Ketika Anda ingin memisahkan identitas tugas di dalam eksekusi asinkron.