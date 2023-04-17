# Octopi info daemon

- systemd based daemon
- regularly uploads a static webpage containing current ocotpi's job info + picture

## Installation

- create `credentials.json` with correct values

```json
{
  "sftp": {
    "host": "host.com",
    "username": "user",
    "password": "P4sswo0Rd"
  },
  "octopi": {
    "url": "http://octopi.local/",
    "api_key": "ABCEDFEFEOZFJOIZF"
  }
}
```

- create venv, activate
- install `pip install git:http://github.com/mrfrangipane/octopi_info_daemon.git`
- create and install service file `octopi_info_daemon.service` (replace `{{ }}` with correct values)
- start and enable service

```ini
[Unit]
Description=Octopi-info-daemon
After=network-online.target

[Service]
ExecStart={{ venv }}/python -m octopi_info_daemon -c {{ credential_filepath }}
WorkingDirectory={{ venv }}
User={{ user }}

[Install]
WantedBy=multi-user.target
```
