from simplex import SIMPLEX_ENV
from simplex import SimplexStorage


class SimplexSetupCheck:

    def __init__(self):
        self.issues = {}

    def run_checks(self):
        return

    def raise_issue(self, key):
        return


class SimplexPreflightSetupCheck(SimplexSetupCheck):
    """
    Setup checks to execute before any configuration files are loaded.
    """


class SimplexConfigSetupCheck(SimplexSetupCheck):
    """
    Validate application configuration
    """


class SimplexDatabaseSetupCheck(SimplexSetupCheck):
    """
    Validate database status and configuration
    """

    def __init__(self, SIMPLEX_ENV):
        # [TODO]: @chris
        # This should be abstracted to a `get_config()` method
        # in infrastructure.env.simplex_env.SimplexEnv so that
        # we can abstract some of the precedence-determining
        # operations described in simplex_env.py$47
        self.config = SIMPLEX_ENV.config.get('mysql')
        self.checks = [
            'host', 'user', 'password',
            'port', 'namespace']
        self.issues = []

        self.check_configuration_set()
        if not self.issues:
            self.db_connection = (
                SimplexStorage.SimplexStorageManagementAPI()
                .set_host(self.config['host'])
                .set_port(self.config['port'])
                .set_user(self.config['user'])
                .set_password(self.config['password'])
                .set_namespace(self.config['namespace'])
                .set_conn()
            )
            self.check_database_reachable()

    def check_configuration_set(self):
        if not self.config:
            # [TODO]: @chris start creating documentation
            self.issues.append({
                'issue:': 'No Database Configuration Found',
                'priority': 0,
                'description': (
                    'We were not able to find any valid configuration for '
                    'a database source.'),
                'resolution': (
                    'Please refer to Configuring Databases '
                    'for details on how to properly set up and configure a '
                    'Simplex database.')
            })
            return

        for conf_check in self.checks:
            # [TODO]: @chris
            # Properly format the config names and resolutions as code
            # with a monospace font
            if not self.config.get(conf_check):
                self.issues.append({
                    'issue': f'{conf_check} not set',
                    'priority': 1,
                    'description': (
                        'We couldn\'t find a configuration value set for '
                        f'mysql.{conf_check}.'),
                    'resolution': (
                        'Set a valid configuration value by running ',
                        f'./bin/config set mysql.{conf_check} VALUE')
                })
        return

    def check_database_reachable(self):
        try:
            conn = self.db_connection.connection.connect()
            conn.close()
        except Exception as e:
            self.issues.append({
                'issue:': 'Could not establish database connection',
                'priority': 1,
                'description': (
                    'We were not able to establish a connection to your '
                    'configured Simplex database.'),
                'resolution': (
                    'Please refer to Configuring Databases '
                    'for details on how to properly set up and configure a '
                    'Simplex database. Additional error details are provided '
                    f'below for reference:\n\n{e}')
            })

        return


class SimplexAuthSetupCheck(SimplexSetupCheck):
    """
    Validate authentication configuration
    """
