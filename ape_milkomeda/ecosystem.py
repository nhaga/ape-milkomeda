from typing import Optional

from ape.api.config import PluginConfig
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_ethereum.ecosystem import Ethereum, NetworkConfig

NETWORKS = {
    # chain_id, network_id
    "c1": (2001, 2001),
    "c1-testet": (200101, 200101),
    "a1": (2002, 2002),
    "a1-testnet": (200202, 200202)
}


def _create_network_config(
    required_confirmations: int = 1, block_time: int = 2, **kwargs
) -> NetworkConfig:
    # Helper method to isolate `type: ignore` comments.
    return NetworkConfig(
        required_confirmations=required_confirmations, block_time=block_time, **kwargs
    )  # type: ignore


def _create_local_config(default_provider: Optional[str] = None) -> NetworkConfig:
    return _create_network_config(
        required_confirmations=0, block_time=0, default_provider=default_provider
    )


class MilkomedaConfig(PluginConfig):
    a1: NetworkConfig = _create_network_config()
    a1_fork: NetworkConfig = _create_local_config()
    a1_testnet: NetworkConfig = _create_network_config()
    a1_testnet_fork: NetworkConfig = _create_local_config()
    local: NetworkConfig = NetworkConfig(default_provider="test")
    default_network: str = LOCAL_NETWORK_NAME


class Milkomeda(Ethereum):
    @property
    def config(self) -> MilkomedaConfig:  # type: ignore
        return self.config_manager.get_config("milkomeda")  # type: ignore
