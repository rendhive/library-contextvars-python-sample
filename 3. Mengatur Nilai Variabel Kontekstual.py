import contextvars

var = contextvars.ContextVar('my_var', default='default_value')
var.set('new_value')
print(var.get())  # Mendapatkan nilai yang baru di-set
# Fungsi: Mengubah nilai dari variabel kontekstual.
# Kondisi: Ketika Anda ingin memperbarui nilai dalam konteks tertentu.