import threading
# Threading is having two or more processes run at once

class MyMessenger(threading.Thread):
    def run(self):
        for _ in range(100):
            print(threading.currentThread().getName())

x = MyMessenger(name="Send out messages")
y = MyMessenger(name="Receive messages")
x.start()
y.start()
