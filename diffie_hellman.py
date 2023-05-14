import socket
import time
from threading import Thread
from multiprocessing import Queue
import random
import struct

def alice(queue_for_shared_key: Queue, port=54888):
    conn = socket.socket()
    conn.connect(("localhost", port))
    data = conn.recv(struct.calcsize("!III"))
    g, p, big_b = struct.unpack("!III", data)
    a = random.randint(1000, 9999)
    big_a = g**a%p
    packed_big_a = struct.pack("!I", big_a)
    conn.send(packed_big_a)
    shared_key = big_b**a%p
    queue_for_shared_key.put(shared_key)

def bob(queue_for_shared_key:Queue, port=54888):
    server = socket.socket()
    server.bind(("localhost", port))
    server.listen()
    conn, _ = server.accept()
    g = random.randint(1000, 9999)
    p = random.randint(1000, 9999)
    b = random.randint(1000, 9999)
    big_b = g**b%p
    packed_big_b = struct.pack("!III", g, p, big_b)
    conn.send(packed_big_b)
    data = conn.recv(struct.calcsize("!I"))
    (big_a,) = struct.unpack("!I", data)
    shared_key = big_a**b%p
    queue_for_shared_key.put(shared_key)


if __name__ == '__main__':
    queue_for_shared_keys = Queue()
    bob_thread = Thread(target=bob, args=(queue_for_shared_keys,))
    bob_thread.start()
    time.sleep(1)
    alice(queue_for_shared_keys)
    key_1, key_2 = queue_for_shared_keys.get(), queue_for_shared_keys.get()
    print(key_1, key_2)
    assert key_1==key_2
