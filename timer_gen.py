import time

def time_gen():
    last_time = time.perf_counter()
    while True:
        current_time = time.perf_counter()
        time_diff = current_time - last_time
        last_time = current_time
        yield time_diff

if __name__ == "__main__":
    timer = timer_gen()
    for elapsed_time in timer:
        print(f"Elapsed time: {elapsed_time} seconds")
        time.sleep(0.5)
