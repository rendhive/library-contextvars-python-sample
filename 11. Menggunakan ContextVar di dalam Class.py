import contextvars

class MyClass:
    var = contextvars.ContextVar('class_var', default='default_value')

    def set_var(self, value):
        self.var.set(value)

    def print_var(self):
        print("Class var value:", self.var.get())

my_obj = MyClass()
my_obj.set_var('Hello World')
my_obj.print_var()
# Fungsi: Menggunakan context vars dalam konteks kelas.
# Kondisi: Ketika Anda ingin menyimpan dan mengelola data dalam konteks objek.