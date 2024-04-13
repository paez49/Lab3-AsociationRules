from time import time


def measure_time(func):
    """Decorator to measure the time elapsed in a function.

    Args:
        function (function): Function to measure the time.
    """

    def wrapper(*args, **kwargs):
        time_start = time()
        func(*args, **kwargs)
        time_end = time()
        total_time = time_end - time_start
        print(
            f"### Time elapsed {func.__name__}: {total_time:.2f} seconds."
        )

    return wrapper
