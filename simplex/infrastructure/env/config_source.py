import json
from simplex import APP_ROOT, management


class SimplexConfigSource:

    def __init__(self):
        name = None
        config = {}

    def set_name(self, name):
        self.name = name
        return self

    def can_write(self):
        return False

    def set_keys(self, keys):
        raise Exception('This configuration does not support write operations')

    def delete_keys(self, keys):
        raise Exception('This configuration does not support write operations')


class SimplexConfigLocalSource(SimplexConfigSource):

    def __init__(self):
        _config_path = APP_ROOT / 'conf/local.json'
        config = self.load_config()
        workflow = management.SimplexManagementWorkflow()

    def load_config(self):
        if not os.path.exists(self._config_path):
            return {}

        try:
            with open(self._config_path, 'r') as f:
                config = json.loads(f)
        except json.decoder.JSONDecodeError:
            self.workflow.log_fail(
                f'Configuration file {_config_path} exists, but is either '
                'not readable, or is not valid JSON. Please check the file '
                'permissions and that it is valid JSON.')
        return config

    def save_config(self):
        try:
            with open(self._config_path, 'w') as f:
                json.dump(self.config, f)
        except:
            self.workflow.log_fail(
                f'Could not write configuration to {self._config_path}. '
                'Please ensure that the file is writable.'
            )
        return

    def set_keys(self, keys: dict):
        self.config = {**self.config, **keys}
        return

    def delete_keys(self, keys: list):
        [self.config.pop(key) for key in keys]
        return
