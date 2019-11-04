import time


def time_this(NUM_RUNS=10):
    def decorator(func_to_run):
        def func(*args, **kwargs):
            avg = 0
            for _ in range(NUM_RUNS):
                t0 = time.time()
                func_to_run(*args, **kwargs)
                t1 = time.time()
                avg += (t1 - t0)
            avg /= NUM_RUNS
            fn = func_to_run.__name__
            print("Среднее время выполнения: %.5f сек." % avg)
        return func

    return decorator


@time_this()
def test_func():
    for _ in range(1000000):
        pass


if __name__ == "__main__":
    test_func()
