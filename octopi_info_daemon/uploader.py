import logging

import pysftp

_logger = logging.getLogger(__name__)


def upload(credentials, files):
    host = credentials.sftp['host']
    username = credentials.sftp['username']
    password = credentials.sftp['password']

    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    with pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts) as sftp:
        for local, remote in files.items():
            _logger.info(f"Uploading {local} -> {remote}")
            sftp.put(local, remote)
