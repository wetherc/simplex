# Manages the execution environment configuration
#
# This class serves primarily to provide an API for
# reading Simplex configuration


class SimplexEnv:

    def __init__(self):
        source_stack = None
        cache = {}

    def initialize_web_environment(self):
        self.initialize_common_environment(false)

    def initialize_common_environment(self, optional_config: bool):
        self.build_configuration_stack(optional_config)

    def build_configuration_stack(self):
        pass

    def get_env_config(self, key):
        if not self.source_stack:
            raise Exception(
                f'Trying to read configuration "{key}" before configuration '
                'has been initialized')

        if self.cache.get(key):
            return cache['key']

        result = source_stack.get(key)
        if not result:
            raise Exception(f'No configuration specified for {key}')

        cache[key] = result
        return result
