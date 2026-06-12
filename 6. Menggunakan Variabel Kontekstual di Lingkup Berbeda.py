import contextvars
import asyncio

var = contextvars.ContextVar('my_var', default='default_value')

async def first_task():
    var.set('first_task_value')
    print(var.get())  # Menampilkan nilai untuk task pertama

async def second_task():
    print(var.get())  # Menampilkan nilai yang sama karena dalam konteks yang sama

asyncio.run(first_task())
asyncio.run(second_task())  # Contoh ini menunjukkan nilai default
# Fungsi: Melihat pengaruh konteks yang berbeda terhadap variabel kontekstual.
# Kondisi: Ketika Anda ingin memisahkan nilai berdasarkan eksekusi.