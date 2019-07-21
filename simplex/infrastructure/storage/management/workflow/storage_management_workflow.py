from simplex.infrastructure.management.management_workflow import (
    SimplexManagementWorkflow
)


class SimplexStorageManagementWorkflow(SimplexManagementWorkflow):

    def __init__(self):
        self.apis = []

        # [TODO @chris]:
        # Attributes not currently used
        self.dryRun = False
        self.force = False
        self.patches = []

    def set_apis(self, apis):
        self.apis = apis
        return self

    def set_dry_run(self, dryRun):
        self.dryRun = dryRun
        return self

    def set_force(self, force):
        self.force = force
        return self

    def set_patches(self, patches):
        self.patches = patches
        return self
