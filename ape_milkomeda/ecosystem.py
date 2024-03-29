from ape.api.config import PluginConfig
from ape_ethereum.ecosystem import Ethereum, NetworkConfig
from ape_ethereum.transactions import TransactionType

NETWORKS = {
    "c1": (2001, 2001),
    "c1-testnet": (200101, 200101),
    "a1": (2002, 2002),
    "a1-testnet": (200202, 200202),
}

milkomeda_config = NetworkConfig(
    default_provider="milkomeda",
    default_transaction_type=TransactionType.STATIC,
    gas_limit=1_000_000,
)


class MilkomedaConfig(PluginConfig):
    c1: NetworkConfig = milkomeda_config
    c1_testnet: NetworkConfig = milkomeda_config
    a1: NetworkConfig = milkomeda_config
    a1_testnet: NetworkConfig = milkomeda_config
    local: NetworkConfig = NetworkConfig(
        default_transaction_type=TransactionType.STATIC, default_provider="test"
    )


class Milkomeda(Ethereum):
    @property
    def config(self) -> MilkomedaConfig:
        return self.config_manager.get_config("milkomeda")
