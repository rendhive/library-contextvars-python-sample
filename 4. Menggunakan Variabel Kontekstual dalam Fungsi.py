import contextvars

var = contextvars.ContextVar('my_var', default='default_value')

def print_var():
    print(var.get())

var.set('new_value')
print_var()  # Memanggil fungsi yang mencetak nilai kontekstual
# Fungsi: Menggunakan variabel kontekstual di dalam fungsi untuk mencetak nilainya.
# Kondisi: Ketika Anda ingin menjaga ketidakbergantungan pada nilai global.