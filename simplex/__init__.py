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
