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
        self.workflow = SimplexManagement.SimplexManagementWorkflow()
        self.config_path = APP_ROOT / 'conf/default.json'
        self.config = self.load_config()

    def load_config(self):
        if not self.config_path.is_file():
            return {}

        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
        except json.decoder.JSONDecodeError:
            self.workflow.log_fail(
                f'Configuration file {self.config_path} exists, but is either '
                'not readable, or is not valid JSON. Please check the file '
                'permissions and that it is valid JSON.')
            config = {}
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

    def set_keys(self, update_keys: dict, config=None, path=[]):
        if config is None:
            config = self.config

        for _key in update_keys:
            if _key in config:
                if (
                    isinstance(config[_key], dict) and
                    isinstance(update_keys[_key], dict)
                ):
                    self.set_keys(
                        path=path + [str(_key)],
                        config=config[_key],
                        update_keys=update_keys[_key])
                elif config[_key] == update_keys[_key]:
                    pass  # same leaf value
                else:
                    config[_key] = update_keys[_key]
            else:
                config[_key] = update_keys[_key]
        self.config = config
        return

    def get_key(self, key: str):
        _keys = key.split('.')
        _val = self.config
        for _key in _keys:
            _val = _val.get(_key)
        return(_val)

    def delete_keys(self, keys: list):
        # [TODO]: @chris
        # Unbreak this. It won't currently work with nesting
        for key in keys:
            try:
                self.config.pop(key)
            except:
                pass
        return

    def can_write(self):
        return True


class SimplexConfigLocalSource(SimplexConfigDefaultSource):

    def __init__(self):
        self.workflow = SimplexManagement.SimplexManagementWorkflow()
        self.config_path = APP_ROOT / 'conf/local.json'
        self.config = self.load_config()


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
        self.config = self.load_config()

    def load_config(self):
        return {}
