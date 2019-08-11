# Manages the execution environment configuration
#
# This class serves primarily to provide an API for
# reading Simplex configuration
from simplex.infrastructure.env import SimplexConfigSource


class SimplexEnv:

    def __init__(self):
        self.config = self.build_configuration_stack()
        self.cache = {}

    def initialize_web_environment(self):
        self.initialize_common_environment(false)

    def initialize_common_environment(self, optional_config: bool):
        self.build_configuration_stack(optional_config)

    def build_configuration_stack(self):
        # The source stack is prioritized by index position, with
        # a higher index value corresponding to a higher precedence.
        #
        # In this way, the default configuration will always take the
        # lowest order precedence and will always be superceded by any
        # other configuration source. Generally, this order will be
        # DefaultConfigSource < LocalConfigSource < DatabaseConfigSource
        _source_stack = [
            SimplexConfig.SimplexConfigDefaultSource(),
            SimplexConfig.SimplexConfigLocalSource(),
            SimplexConfig.SimplexConfigDatabaseSource()
        ]

        config = {}
        # [TODO]: @chris
        # I'm not a huge fan of this approach, but I guess it's functional
        # enough atm. Basically, I don't like that it hides information: if
        # you have the same configuration key set in multiple configuration
        # sources, this will only show whichever of those takes the highest
        # precedence. If you're editing a local config file and aren't seeing
        # your changes take effect because there's a higher precedence config
        # set in the database, that's going to be a weird and confusing user
        # experience. Ideally, we should be showing the user all of the config
        # sources for which a key is set, what that key is set to in each, and
        # which of them takes highest precedence.
        for source in range(len(_source_stack)):
            config = {**config, **_source_stack[source].config}

        return config

    def get_env_config(self, key):
        if not self.config:
            raise Exception(
                f'Trying to read configuration "{key}" before configuration '
                'has been initialized')

        if self.cache.get(key):
            return cache['key']

        result = config.get(key)
        if not result:
            raise Exception(f'No configuration specified for {key}')

        cache[key] = result
        return result
