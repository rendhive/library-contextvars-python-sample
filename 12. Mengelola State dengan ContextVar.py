import contextvars

user_state = contextvars.ContextVar('user_state', default='guest')

def set_user(new_state):
    user_state.set(new_state)

def get_user():
    return user_state.get()

set_user('admin')
print("Current user state:", get_user())
# Fungsi: Mengelola state pengguna menggunakan variabel kontekstual.
# Kondisi: Ketika Anda ingin mengatur dan mengakses informasi pengguna dalam konteks tertentu.