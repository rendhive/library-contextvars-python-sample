import contextvars
import asyncio

var = contextvars.ContextVar('my_var', default='default_value')

async def task_with_nested_context():
    token = var.set('nested_value')
    print("Inside nested context:", var.get())
    var.reset(token)  # Reset ke nilai sebelumnya

async def main_task():
    var.set('main_task_value')
    await task_with_nested_context()

asyncio.run(main_task())
# Fungsi: Demonstrasi penggunaan nested context melalui pengaturan dan reset.
# Kondisi: Ketika Anda ingin mengelola nilai di dalam konteks yang lebih dalam.