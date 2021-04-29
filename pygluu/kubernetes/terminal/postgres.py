"""
pygluu.kubernetes.terminal.postgres
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains helpers to interact with user's inputs for postgres terminal prompts.

License terms and conditions for Gluu Cloud Native Edition:
https://www.apache.org/licenses/LICENSE-2.0
"""

import click


class PromptPostgres:
    """Prompt is used for prompting users for input used in deploying Gluu.
    """

    def __init__(self, settings):
        self.settings = settings

    def prompt_postgres(self):
        """Prompts for PostGres. Injected in a file postgres.yaml used with kubedb
        """
        if self.settings.get("installer-settings.postgres.install") in (None, ''):
            install = click.confirm("Install postgres using the KubeDB operator?)")
            self.settings.set("installer-settings.postgres.install", install)

        if self.settings.get("installer-settings.postgres.install"):
            if self.settings.get("installer-settings.postgres.namespace") in (None, ''):
                namespace = click.prompt("Please enter a namespace for postgres.", default="postgres")
                self.settings.set("installer-settings.postgres.namespace", namespace)

            if self.settings.get("installer-settings.postgres.replicas") in (None, ''):
                replicas = click.prompt("Please enter number of replicas for postgres.", default=3)
                self.settings.set("installer-settings.postgres.replicas", replicas)

        if self.settings.get("config.configmap.cnJackrabbitPostgresHost") in (None, ''):
            url = click.prompt(
                "Please enter  postgres (remote or local) "
                "URL base name.The recommended approach is to use a "
                "production grade managed service such as Aurora",
                default=f"postgres.{self.settings.get('installer-settings.postgres.namespace')}.svc.cluster.local",
            )
            self.settings.set("config.configmap.cnJackrabbitPostgresHost", url)
