import sys
import logging

from octopi_info_daemon.credentials import Credentials
from octopi_info_daemon.application import Application


_logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # FIXME: use argparse
    if '-c' in sys.argv:
        credentials_filepath = sys.argv[sys.argv.index('-c') + 1]
    else:
        raise ValueError("Please specify a credential filepath with '-c' argument")

    credentials = Credentials(credentials_filepath)
    credentials.load()

    application = Application(credentials)
    application.main_loop()

    _logger.info("Exit")
