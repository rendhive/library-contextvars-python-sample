import contextvars
import threading

var = contextvars.ContextVar('my_var', default='default_value')

def thread_task(value):
    var.set(value)
    print(f"Thread {threading.current_thread().name}: {var.get()}")

t1 = threading.Thread(target=thread_task, args=('Thread 1 Value',), name='T1')
t2 = threading.Thread(target=thread_task, args=('Thread 2 Value',), name='T2')

t1.start()
t2.start()
t1.join()
t2.join()
# Fungsi: Menggunakan variabel kontekstual untuk menjaga keunikan antar thread.
# Kondisi: Ketika Anda ingin memisahkan context dalam eksekusi paralel.