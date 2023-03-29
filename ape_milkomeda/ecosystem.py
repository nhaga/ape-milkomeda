from typing import Optional, cast

from ape.api.config import PluginConfig
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_ethereum.ecosystem import Ethereum, NetworkConfig


NETWORKS = {
    "c1": (2001, 2001),
    "c1-testnet": (200101, 200101),
    "a1": (2002, 2002),
    "a1-testnet": (200202, 200202),
}


class MilkomedaConfig(PluginConfig):
    c1: NetworkConfig = NetworkConfig(required_confirmations=1, block_time=3) 
    c1_testnet: NetworkConfig = NetworkConfig(required_confirmations=1, block_time=3) 
    a1: NetworkConfig = NetworkConfig(required_confirmations=1, block_time=3) 
    a1_testnet: NetworkConfig = NetworkConfig(required_confirmations=1, block_time=3) 
    #default_network: str = "c1"


class Milkomeda(Ethereum):
    @property
    def config(self) -> MilkomedaConfig:  
        return cast(MilkomedaConfig, self.config_manager.get_config("milkomeda"))
