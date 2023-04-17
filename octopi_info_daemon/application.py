import os
import tempfile
import time
import logging

from .credentials import Credentials
from .downloader import download
from .html_template import make_html_template
from .octopi_info import get_octopi_info
from .uploader import upload

_logger = logging.getLogger(__name__)

_MAIN_LOOP_INTERVAL = 60
_WEBCAM_ROUTE = "webcam/?action=snapshot"


class Application:
    def __init__(self, credentials: Credentials):
        self._credentials = credentials

    def main_loop(self):
        _logger.info("Starting main loop...")
        while True:
            try:
                self._main_loop_step()

            except KeyboardInterrupt as e:
                return

            except Exception as e:
                _logger.warning(f"Exception occurred {e}")

            finally:
                time.sleep(_MAIN_LOOP_INTERVAL)  # FIXME: use a loop and datetime

    def _main_loop_step(self):
        image_filepath = tempfile.mktemp() + '.jpg'
        download(f"{self._credentials.octopi['url']}/{_WEBCAM_ROUTE}", image_filepath)

        octopi_info = get_octopi_info(self._credentials.octopi)

        htmlpage_filepath = tempfile.mktemp() + '.html'
        make_html_template(htmlpage_filepath, octopi_info)

        upload(
            credentials=self._credentials,
            files={
                image_filepath: 'image.jpg',
                htmlpage_filepath: 'index.html'
            }
        )

        os.remove(image_filepath)
        os.remove(htmlpage_filepath)
