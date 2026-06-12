import contextvars

context_var = contextvars.ContextVar('ctx_var', default='default_value')

class ExampleClass:
    def set_context_var(self, value):
        context_var.set(value)

    def print_var(self):
        print("Current value:", context_var.get())

example = ExampleClass()
example.set_context_var('example_value')
example.print_var()
# Fungsi: Menggunakan context vars untuk memisahkan data dalam kelas dan fungsi.
# Kondisi: Ketika Anda ingin memperhatikan kontekstual data di struktur yang berbeda.