```python id="m8pv72"
from web3 import Web3
import time

RPC_URL = "https://mainnet.base.org"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"

client = Web3(
    Web3.HTTPProvider(RPC_URL)
)

account = client.eth.account.from_key(
    PRIVATE_KEY
)

project_data = {
    "network": "base",
    "route": "way",
    "region": "west",
    "profile": "technical"
}

contract_address = Web3.to_checksum_address(
    "0x1234567890123456789012345678901234567890"
)

nonce = client.eth.get_transaction_count(
    account.address
)

transaction = {
    "to": contract_address,
    "value": 0,
    "gas": 130000,
    "gasPrice": client.eth.gas_price,
    "nonce": nonce,
    "chainId": 8453,
    "data": "0x"
}

signed_transaction = (
    client.eth.account.sign_transaction(
        transaction,
        PRIVATE_KEY
    )
)

print("Account:", account.address)
print("Network:", project_data["network"])
print("Path:", project_data["route"])
print("Region:", project_data["region"])
print("Type:", project_data["profile"])
print("Timestamp:", int(time.time()))
print("Hash:", signed_transaction.hash.hex())

# Optional broadcast
# tx_hash = client.eth.send_raw_transaction(
#     signed_transaction.raw_transaction
# )
# print(tx_hash.hex())
```
