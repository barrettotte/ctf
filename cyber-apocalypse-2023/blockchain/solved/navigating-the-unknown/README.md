# navigating-the-unknown

**SOLVED**

> Your advanced sensory systems make it easy for you to navigate familiar environments, but you must rely on intuition to navigate in unknown territories. 
> Through practice and training, you must learn to read subtle cues and become comfortable in unpredictable situations. 
> Can you use your software to find your way through the blocks?

## Guidelines

The point of this README is to provide some guidance for people who attempt solving a blockchain challenge for the first time.

### Ports

As you have already seen, there are 2 ports provided.

- The one port is the `tcp` port, which is used to retrieve information about connecting to the private chain, such as private key, and the target contract's addresses. You can connect to this one using `netcat`.
- The other port is the `rpc` url. You will need this in order to connect to the private chain.

In order to figure out which one is which, try using `netcat` against both. The one which works is the `tcp` port, while the other one is the `rpc url`.

### Contract Sources

In these challenges, you will meet 2 type of smart contract source files, the `Setup.sol` file and the challenge files.

#### Setup.sol

The `Setup.sol` file contains a single contract, the `Setup`. As the name indicates, inside this contract all the initialization actions are happening. There will typically be 3 functions:

- `constructor()`: It is called automatically once when the contract is deployed and cannot be called again. It contains all the initialization actions of the challenge, like deploying the challenge contracts and any other actions needed.
- `TARGET()`: It returns the address of the challenge contract.
- `isSolved()`: This function contains the final objective of the challenge. It returns `true` if the challenge is solved, `false` otherwise. By reading its source, one is able to figure out what the objective is.

#### Other source files

All the other files provided are the challenge contracts. You will only have to interact with them to solve the challenge. Try analyzing their source carefully and figure out how to break them, following the objective specified in `isSolved` function of the `Setup` contract.

### Interacting with the blockchain

In order to interact wth the smart contracts in the private chain, you will need:

- A private key with some ether. We provide it via the tcp endpoint.
- The target contract's address. We provide both the Setup's and the Target's addresses.
- The rpc url, which can be found using what described earlier.

After having collected all the connection information, then you can either use `web3py` or `web3js` to perform function calls in the smart contracts or any other actions needed. You can find some useful tutorials about both with a little googlin'.
An even handier way is using a tool like `foundry-rs`, which is an easy-to-use cli utility to interact with the blockchain, but there are less examples online than the other alternatives.


## Solving

68.183.45.143:31928 <- rpc
68.183.45.143:30854 <- tcp

`nc 68.183.45.143 30854`

```txt
Private key     :  0x53949d9cea852f2e765a3e20a710621cc2be213337d3c1d8033f2d3f190cd79f
Address         :  0x055E58BF6267a78783B871A7D989868242c65172
Target contract :  0x1A56759Bb1c2e2751ccB07ca2C2F4828Fca689E4
Setup contract  :  0x0aECB410F070C3075C9DB6e38003E690360446fe
```

- https://web3py.readthedocs.io/en/stable/quickstart.html
- https://ethereum.stackexchange.com/questions/134720/execute-a-contract-function-from-web3-py
- https://leftasexercise.com/2021/08/22/using-web3-py-to-interact-with-a-smart-contract/
- https://medium.com/coinmonks/function-state-mutability-in-solidity-acb850eedccc
- https://docs.soliditylang.org/en/v0.8.17/abi-spec.html#mapping-solidity-to-abi-types
- https://stackoverflow.com/questions/72613116/ethereum-raw-contract-interaction-using-web3-python


`python3 flag.py`

```txt
AttributeDict({'transactionHash': HexBytes('0x0d86e34450439c7a2d70697cd31aa70e8e8eb7a0c924e76f6386abe868bdc61b'), 'transactionIndex': 0, 'blockHash': HexBytes('0xb71a1cd03b1a039984c72078e7b6a441ae39242e13589cf7eadd5ce5146fdcd6'), 'blockNumber': 2, 'from': '0x055E58BF6267a78783B871A7D989868242c65172', 'to': '0x1A56759Bb1c2e2751ccB07ca2C2F4828Fca689E4', 'cumulativeGasUsed': 43574, 'gasUsed': 43574, 'contractAddress': None, 'logs': [], 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'), 'type': 2, 'effectiveGasPrice': 1000000000})
```

netcat back tcp, got flag

`HTB{9P5_50FtW4R3_UPd4t3D}`