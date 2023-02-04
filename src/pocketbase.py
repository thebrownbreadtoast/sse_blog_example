import requests


PB_BASE_URL = "http://pocketbase:8080"


def get_token() -> str:
    url = f"{PB_BASE_URL}/api/admins/auth-with-password"

    body = {
        "identity": "root@root.com",
        "password": "root@root.com",
    }

    response_obj = requests.post(url, data=body)

    parsed_response_obj = response_obj.json()

    return parsed_response_obj["token"]


def create_job() -> str:
    url = f"{PB_BASE_URL}/api/collections/jobs/records"

    headers = {
        "Authorization": f"{get_token()}",
        "Content-Type": "application/json",
    }

    data = {
        "status": "processing",
    }

    response_obj = requests.post(url, json=data, headers=headers)

    return response_obj.json()


def get_job(job_id: str) -> str:
    url = f"{PB_BASE_URL}/api/collections/jobs/records/{job_id}"

    headers = {
        "Authorization": f"{get_token()}",
        "Content-Type": "application/json",
    }

    response_obj = requests.get(url, headers=headers)

    return response_obj.json()


def update_job(job_id: str, status: str) -> None:
    url = f"{PB_BASE_URL}/api/collections/jobs/records/{job_id}"

    headers = {
        "Authorization": f"{get_token()}",
        "Content-Type": "application/json",
    }

    data = {
        "status": status,
    }

    response_obj = requests.patch(url, json=data, headers=headers)

    return
