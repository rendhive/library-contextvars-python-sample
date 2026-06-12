import contextvars
import asyncio

var = contextvars.ContextVar('my_var', default='default_value')

async def modify_var():
    var.set('async_value')
    print(var.get())

asyncio.run(modify_var())
# Fungsi: Menjalankan fungsi asinkron yang memodifikasi dan mencetak variabel kontekstual.
# Kondisi: Ketika Anda membutuhkan penggunaan variabel kontekstual dalam alur asinkron.