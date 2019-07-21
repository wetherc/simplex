import logging


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
        self.logger.warning('[WARN]: {}'.format(
            message)
        )

    def log_fail(self, message):
        self.logger.error('[FAIL]: {}'.format(
            message)
        )

    def log_okay(self, message):
        self.logger.info('[OKAY]: {}'.format(
            message)
        )
