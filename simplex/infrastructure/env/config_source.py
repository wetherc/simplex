import json
import pathlib
from simplex import APP_ROOT, SimplexManagement


class SimplexConfigSource:

    def __init__(self):
        self.name = None
        self.config = {}

    def set_name(self, name):
        self.name = name
        return self

    def can_write(self):
        return False

    def set_keys(self, keys):
        raise Exception('This configuration does not support write operations')

    def delete_keys(self, keys):
        raise Exception('This configuration does not support write operations')


class SimplexConfigDefaultSource(SimplexConfigSource):

    def __init__(self):
        self.config_path = APP_ROOT / 'conf/default.json'
        self.config = self.load_config()
        self.workflow = SimplexManagement.SimplexManagementWorkflow()

    def load_config(self):
        if not self.config_path.is_file():
            return {}

        try:
            with open(self.config_path, 'r') as f:
                config = json.loads(f)
        except json.decoder.JSONDecodeError:
            self.workflow.log_fail(
                f'Configuration file {self.config_path} exists, but is either '
                'not readable, or is not valid JSON. Please check the file '
                'permissions and that it is valid JSON.')
        return config

    def save_config(self):
        try:
            with open(self.config_path, 'w') as f:
                json.dump(self.config, f)
        except:
            self.workflow.log_fail(
                f'Could not write configuration to {self.config_path}. '
                'Please ensure that the file is writable.'
            )
        return

    def set_keys(self, keys: dict):
        self.config = {**self.config, **keys}
        return

    def delete_keys(self, keys: list):
        [self.config.pop(key) for key in keys]
        return

    def can_write(self):
        return True


class SimplexConfigLocalSource(SimplexConfigDefaultSource):

    def __init__(self):
        self.config_path = APP_ROOT / 'conf/local.json'
        self.print(config_path)
        self.config = self.load_config()
        self.workflow = SimplexManagement.SimplexManagementWorkflow()


class SimplexConfigDatabaseSource(SimplexConfigSource):

    def __init__(self, **kwargs):
        if kwargs is not None:
            self.host = kwargs.get('host')
            self.port = kwargs.get('port')
            self.namespace = kwargs.get('namespace')
            self.user = kwargs.get('user')
            self.password = kwargs.get('password')
        else:
            self.host = None
            self.port = None
            self.namespace = None
            self.user = None
            self.password = None
