from datetime import datetime, timedelta
import requests

_STRFMT = "%d/%m/%Y %H:%M"
_JOB_ROUTE = "api/job"


def get_octopi_info(credentials):  # FIXME: make info a dataclass
    response = requests.get(
        url=f"{credentials['url']}/{_JOB_ROUTE}",
        headers={'X-Api-Key': credentials['api_key']}
    )
    if response.status_code != 200:
        raise RuntimeError(f'Octopi response code {response.status_code} ({response.text})')
    data = response.json()

    if "error" in data.keys():
        return [
            datetime.now().strftime(_STRFMT), "",
            data['error']
        ]

    if data['state'] != "Printing":
        return [
            datetime.now().strftime(_STRFMT), "",
            f"State: {data['state']}"
        ]

    name = data['job']['file']['display']
    progress = data['progress']['completion']
    elapsed = data['progress']['printTime']
    finishes_at = (datetime.now() + timedelta(seconds=data['progress']['printTimeLeft'])).strftime(_STRFMT)
    state = data['state']

    return [
        datetime.now().strftime(_STRFMT), "",
        f"{state}: {name.replace('.gcode', '')}", "",
        f"Elapsed: {elapsed / 60 / 60:.1f}h ({progress:.1f}%)",
        f"Finishes at: {finishes_at} (estimated)"
    ]
