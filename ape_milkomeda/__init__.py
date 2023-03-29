from ape import plugins
from ape.api import NetworkAPI, create_network_type
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_test import LocalProvider
from ape_geth import GethProvider

from .ecosystem import NETWORKS, Milkomeda, MilkomedaConfig
from .provider import MilkomedaProvider

@plugins.register(plugins.Config)
def config_class():
    return MilkomedaConfig


@plugins.register(plugins.EcosystemPlugin)
def ecosystems():
    yield Milkomeda


@plugins.register(plugins.NetworkPlugin)
def networks():
    for network_name, network_params in NETWORKS.items():
        yield "milkomeda", network_name, create_network_type(*network_params)

    yield "milkomeda", LOCAL_NETWORK_NAME, NetworkAPI

@plugins.register(plugins.ProviderPlugin)
def providers():
    for network_name in NETWORKS:
        yield "milkomeda", network_name, MilkomedaProvider
        #yield "milkomeda", network_name, GethProvider          

    # yield "polygon", LOCAL_NETWORK_NAME, LocalProvider
    yield "milkomeda", LOCAL_NETWORK_NAME, MilkomedaProvider