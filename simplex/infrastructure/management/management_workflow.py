import logging
import sys


logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO)


class SimplexManagementWorkflow:

    def __init__(self):
        self.logger = logging.getLogger()

    def is_executable(self):
        return True

    def log_info(self, message):
        self.logger.info('[INFO]: {}'.format(
            message)
        )

    def log_warn(self, message):
        self.logger.info('[WARN]: {}'.format(
            message)
        )

    def log_fail(self, message):
        self.logger.info('[FAIL]: {}'.format(
            message)
        )

    def log_okay(self, message):
        self.logger.info('[OKAY]: {}'.format(
            message)
        )
