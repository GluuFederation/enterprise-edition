import pytest


@pytest.fixture()
def settings():
    from pygluu.kubernetes.settings import ValuesHandler, unlink_values_yaml

    handler = ValuesHandler()
    yield handler
    unlink_values_yaml()

@pytest.fixture()
def kubeapi():
    from pygluu.kubernetes.kubeapi import Kubernetes, load_kubernetes_config

    handler = Kubernetes()
    yield handler
    load_kubernetes_config()

@pytest.fixture()
def gluu():
    from pygluu.kubernetes.gluu import Gluu

    handler = Gluu
    yield handler

