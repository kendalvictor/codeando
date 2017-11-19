import time
from threading import Thread


class ClassThread(Thread):
    def __init__(self, ii):
        self.ii = int(ii)
        super(ClassThread, self).__init__()

    def run(self):
        for j in range(100000000):
            self.ii += 1


print("/////// CON HILOS:: Join afuera ")
comienzo = time.time()
threads = []
for i in range(5):
    print(" {0}".format(i))
    t = ClassThread(comienzo)
    threads.append(t)
    t.start()
    t.join()

print(time.time() - comienzo)

for k in range(10):
    print(k, end=" ")


