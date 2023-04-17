import json
import logging

_logger = logging.getLogger(__name__)


class Credentials:
    def __init__(self, filepath):
        self.octopi = None
        self.sftp = None
        self._filepath = filepath

    def load(self):
        with open(self._filepath, 'r') as credential_file:
            data = json.load(credential_file)
            self.sftp = data["sftp"]
            self.octopi = data["octopi"]

        # ensure no trailing /
        self.octopi['url'] = self.octopi['url'].strip('/')

        _logger.info(f"Credentials loaded from {self._filepath}")
