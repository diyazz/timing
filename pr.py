import time

class timm:
    def __init__(self, func, *args):
        self.num_runs = 10
        self.func = func

        avg_time = 0
        for i in range(self.num_runs):
            t0 = time.time()

            self.func(*args)

            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= self.num_runs
        fn = self.func.__name__
        print("Среднее время выполнения за %s запусков: %.5f секунд" % (self.num_runs, avg_time))

@timm
def f(n=1000000):
    for i in range(n):
        pass

