import time


def start_timer() -> float:
    return time.perf_counter()


def get_time(start_time: float) -> float:
    return round((time.perf_counter() - start_time) * 1000, 3)
