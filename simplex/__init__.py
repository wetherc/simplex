from .infrastructure.config import APP_ROOT
from .infrastructure import management as SimplexManagement
from .infrastructure import storage as SimplexStorage
from .infrastructure import env as Env

from .view import SimplexPage
from .view import SimplexLayout
from .view import SIMUI

from .application import data as SimplexData
from .application import config as SimplexConfig


SIMPLEX_ENV = Env.SimplexEnv()
_issues = (
    SimplexConfig
    .SetupCheck
    .SimplexDatabaseSetupCheck(SIMPLEX_ENV)
    .issues)
if _issues:
    raise Exception(
        f'Could not load application. Please correct the following: {_issues}'
    )

SIMPLEX_ENV.config['DB_CONN'] = (
    SimplexStorage.SimplexStorageManagementAPI()
    .set_host(SIMPLEX_ENV.config['mysql']['host'])
    .set_port(SIMPLEX_ENV.config['mysql']['port'])
    .set_user(SIMPLEX_ENV.config['mysql']['user'])
    .set_password(SIMPLEX_ENV.config['mysql']['password'])
    .set_namespace(SIMPLEX_ENV.config['mysql']['namespace'])
    .set_conn()
)

SIMPLEX_ENV.config['fresh_install'] = (
    SimplexConfig
    .SetupCheck
    .SimplexAuthSetupCheck(SIMPLEX_ENV))
