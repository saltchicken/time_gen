import time

def time_gen():
    start_time = time.perf_counter()
    while True:
        current_time = time.perf_counter()
        yield current_time - start_time
        start_time = time.perf_counter()
        

if __name__ == "__main__":
    timer = time_gen()
    for elapsed_time in timer:
        print(f"Elapsed time: {elapsed_time} seconds")
