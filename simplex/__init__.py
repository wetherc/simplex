from simplex.infrastructure.config import APP_ROOT
from simplex.infrastructure import management as SimplexManagement
from simplex.infrastructure import storage as SimplexStorage
from simplex.infrastructure import env as Env

from simplex.view import page as SimplexPage
from simplex.view import layout as SimplexLayout
from simplex.view import simui as SIMUI

from simplex.application import data as SimplexData
from simplex.application import config as SimplexConfig


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
