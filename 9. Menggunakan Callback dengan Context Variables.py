import contextvars
import asyncio

var = contextvars.ContextVar('my_var', default='default_value')

def callback():
    print("Callback value:", var.get())

async def main():
    var.set('callback_value')
    callback()  # Memanggil callback di mana konteks sudah di-set

asyncio.run(main())
# Fungsi: Menggunakan variabel kontekstual dalam callback.
# Kondisi: Ketika Anda ingin memastikan konteks tetap terjaga saat fungsi dipanggil.