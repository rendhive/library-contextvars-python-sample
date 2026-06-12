import contextvars
import logging

request_id = contextvars.ContextVar('request_id')

logging.basicConfig(level=logging.INFO)

def log_with_request_id(message):
    req_id = request_id.get()
    logging.info(f"[{req_id}] {message}")

def process_request(id):
    request_id.set(id)
    log_with_request_id("Processing request.")

process_request('12345')
# Fungsi: Menggunakan variabel kontekstual untuk menjaga konteks pada log.
# Kondisi: Ketika Anda ingin menjaga informasi kontekstual dalam log.