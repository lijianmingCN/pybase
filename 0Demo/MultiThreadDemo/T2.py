import threading

class BoothThread(threading.Thread):
    def __init__(self, data, lock):
        threading.Thread.__init__(self)
        self.data = data
        self.lock = lock

    def run(self):
        for i in range(1000):
            with lock:
                self.doChore(self.data)

    def doChore(self,data):
        data['num'] = data['num'] +1

lock = threading.Lock()
data = {'num':0}
for k in range(10):
    new_thread = BoothThread(data, lock)
    new_thread.start()
    new_thread.join()

print data