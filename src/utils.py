import random
import time

from .pocketbase import update_job


HOST_ADDR = "192.168.1.14"


def fetch_slow_api(job_id: str) -> None:
    random_latency = random.randint(4, 12)

    time.sleep(random_latency)  # noqa

    update_job(job_id, "completed")  # noqa

    return
