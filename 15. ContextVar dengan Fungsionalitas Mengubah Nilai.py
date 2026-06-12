import contextvars

var = contextvars.ContextVar('counter', default=0)

def increment_counter():
    current_value = var.get()
    var.set(current_value + 1)

increment_counter()
print("Counter value after increment:", var.get())
# Fungsi: Mengelola counter yang terpisah menggunakan variabel kontekstual.
# Kondisi: Ketika Anda ingin menghitung secara independen di dalam konteks.