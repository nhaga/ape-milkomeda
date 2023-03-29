from ape.api import ProviderAPI, Web3Provider
from web3 import HTTPProvider, Web3
from web3.middleware import geth_poa_middleware
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from web3.gas_strategies.time_based import medium_gas_price_strategy

class MilkomedaProvider(Web3Provider, ProviderAPI):

    @property
    def uri(self) -> str:
        rpcs = {
            2001: "https://rpc-mainnet-cardano-evm.c1.milkomeda.com",
            200101: "https://rpc-devnet-cardano-evm.c1.milkomeda.com",
            2002: "https://rpc-mainnet-algorand-rollup.a1.milkomeda.com",
            200202: "https://rpc-devnet-algorand-rollup.a1.milkomeda.com",
        }
        return rpcs.get(self.chain_id)

    def connect(self):
        self._web3 = Web3(HTTPProvider(self.uri))


    def disconnect(self):
        self._web3 = None
