import json
import time
import solcx
from web3 import Web3

solcx.install_solc('0.8.18')

with open('Setup.sol', 'r') as f:
    setup_sol = f.read()
with open('ShootingArea.sol', 'r') as f:
    shooting_sol = f.read()

compiled_sol = solcx.compile_standard(
    {
        'language': 'Solidity',
        'sources': {
            'Setup.sol': {'content': setup_sol},
            'ShootingArea.sol': {'content': shooting_sol},
        },
        'settings': {
            'outputSelection': {
                '*': {
                    '*': ['abi', 'metadata', 'evm.bytecode', 'evm.sourceMap'],
                },
            }
        },
    },
    solc_version='0.8.18'
)
# print(compiled_sol)
with open('compiled.json', 'w+') as f:
    f.write(json.dumps(compiled_sol, indent=4))

setup_byte_code = compiled_sol['contracts']['Setup.sol']['Setup']['evm']['bytecode']['object']
setup_abi = compiled_sol['contracts']['Setup.sol']['Setup']['abi']

shooting_byte_code = compiled_sol['contracts']['ShootingArea.sol']['ShootingArea']['evm']['bytecode']['object']
shooting_abi = compiled_sol['contracts']['ShootingArea.sol']['ShootingArea']['abi']

# im assuming HTB is using a ganache container to simulate environments

w3 = Web3(Web3.HTTPProvider('http://139.59.173.68:31303')) # rpc

# latest_block = w3.eth.get_block('latest')
# print(latest_block, '\n', '\n')

# connection information; net cat into tcp address > option 1
#
# Private key     :  0xe0c39a276cc0bb7fc8b602cbb6460c78e64a55fe776785e89a72787bc33a612b
# Address         :  0x18C54c0303686Cb67D858dfF4d1bfB2285ef8739
# Target contract :  0x5DE543260461b30900bc6366691bD4BD9F6B71a0
# Setup contract  :  0x431dc73eEbc7E5A18866bc7d09F67221D57db85f
#
private_key = '0xe0c39a276cc0bb7fc8b602cbb6460c78e64a55fe776785e89a72787bc33a612b'
caller_address = '0x18C54c0303686Cb67D858dfF4d1bfB2285ef8739'
shooting_contract_address = '0x5DE543260461b30900bc6366691bD4BD9F6B71a0'
setup_contract_address = '0x431dc73eEbc7E5A18866bc7d09F67221D57db85f'

# check wallet balance
balance = w3.eth.get_balance(caller_address)
print('initial balance ->', balance)

# get contract instances
setup_contract = w3.eth.contract(address=setup_contract_address, abi=setup_abi, bytecode=setup_byte_code)
shooting_contract = w3.eth.contract(address=shooting_contract_address, abi=shooting_abi, bytecode=shooting_byte_code)

# get latest transaction
nonce = w3.eth.get_transaction_count(caller_address)
print('latest transaction ->', nonce)

### ensure contracts deployed

print('Setup constructor()')
tx = setup_contract.constructor().build_transaction({
    'chainId': w3.eth.chain_id,
    'from': caller_address,
    'nonce': w3.eth.get_transaction_count(caller_address)
})
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
sent_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
receipt = w3.eth.wait_for_transaction_receipt(sent_tx)
if receipt['status'] == 0:
    raise Exception('tx failed: status=0')

print('ShootingArea constructor()')
tx = shooting_contract.constructor().build_transaction({
    'chainId': w3.eth.chain_id,
    'from': caller_address,
    'nonce': w3.eth.get_transaction_count(caller_address)
})
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
sent_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
receipt = w3.eth.wait_for_transaction_receipt(sent_tx)
if receipt['status'] == 0:
    raise Exception('tx failed: status=0')

# interacting with contracts

# call:     simulate making call; no state change
# transact: make state change

# firstShot - fallback() external payable firstTarget

first_shot = shooting_contract.functions.firstShot().call()
print('firstShot -> ', first_shot, '\n')
if first_shot:
    raise Exception('firstShot already set !!!!!!!!')

sent_tx = w3.eth.send_transaction({
    'to': shooting_contract_address,
    'from': caller_address,
    'data': '0xDEADBEEF',
})

time.sleep(2)
receipt = w3.eth.wait_for_transaction_receipt(sent_tx)
if receipt['status'] == 0:
    print(receipt)
    raise Exception('tx failed: status=0')

first_shot = shooting_contract.functions.firstShot().call()
print('firstShot -> ', first_shot, '\n')
if not first_shot:
    raise Exception('failed to set firstShot')

# secondShot - receive() external payable secondTarget

tx = shooting_contract.receive().build_transaction({
    'chainId': w3.eth.chain_id,
    'nonce': w3.eth.get_transaction_count(caller_address),
    'from': caller_address,
    'gas': 10000000,
    'gasPrice': w3.eth.gas_price,
    'value':  w3.to_wei(0.0000000025, "ether"),
})
signed = w3.eth.account.sign_transaction(tx, private_key=private_key)
sent_tx = w3.eth.send_raw_transaction(signed.rawTransaction)

time.sleep(2)
receipt = w3.eth.wait_for_transaction_receipt(sent_tx)
if receipt['status'] == 0:
    raise Exception('tx failed: status=0')

# thirdShot - function third() public thirdTarget

tx = shooting_contract.functions.third().build_transaction({
    'chainId': w3.eth.chain_id,
    'from': caller_address,
    'nonce': w3.eth.get_transaction_count(caller_address),
})
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
sent_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
receipt = w3.eth.wait_for_transaction_receipt(sent_tx)

time.sleep(2)
receipt = w3.eth.wait_for_transaction_receipt(sent_tx)
if receipt['status'] == 0:
    raise Exception('tx failed: status=0')
