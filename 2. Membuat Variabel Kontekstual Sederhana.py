import contextvars

var = contextvars.ContextVar('my_var', default='default_value')
print(var.get())  # Mendapatkan nilai default
# Fungsi: Membuat variabel kontekstual dengan nilai default.
# Kondisi: Ketika Anda ingin menyimpan nilai yang terpisah dalam konteks eksekusi.