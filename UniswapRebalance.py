import time
import requests
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account


private_key = 'a45a993e0a9466PRIVATEKEY5fdc06d8d9a3f4dfa'
account = Account.from_key(private_key)
chain = 56

w3 = Web3(Web3.HTTPProvider('https://sleek-greatest-bush.bsc.discover.quiknode.pro/77f8b9764651APIKEYa1015452890e/'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
false = False
true = True
rebalance_address = "0xEdd07C6C2ADDRESS96c0908A21"
rebalance_abi = [
	{
		"inputs": [],
		"name": "initialize",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint8",
				"name": "version",
				"type": "uint8"
			}
		],
		"name": "Initialized",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "int24",
				"name": "_tickLower",
				"type": "int24"
			},
			{
				"internalType": "int24",
				"name": "_tickUpper",
				"type": "int24"
			},
			{
				"internalType": "bytes",
				"name": "_data",
				"type": "bytes"
			},
			{
				"internalType": "int24",
				"name": "tickLow",
				"type": "int24"
			},
			{
				"internalType": "int24",
				"name": "tickUp",
				"type": "int24"
			},
			{
				"internalType": "bool",
				"name": "dontSwap",
				"type": "bool"
			}
		],
		"name": "rebalanceVia1inch",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "renounceOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pool",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_amtSpecified",
				"type": "uint256"
			}
		],
		"name": "setPool",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "int24",
				"name": "_tickLower",
				"type": "int24"
			},
			{
				"internalType": "int24",
				"name": "_tickUpper",
				"type": "int24"
			}
		],
		"name": "simulate",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "int24",
				"name": "tickLow",
				"type": "int24"
			},
			{
				"internalType": "int24",
				"name": "tickUp",
				"type": "int24"
			}
		],
		"name": "withdraw",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "inRangeCalc",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "nftManager",
		"outputs": [
			{
				"internalType": "contract IUniswapV3PositionsNFT",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "oneinch",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"name": "onERC721Received",
		"outputs": [
			{
				"internalType": "bytes4",
				"name": "",
				"type": "bytes4"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "pool",
		"outputs": [
			{
				"internalType": "contract IUniswapV3Pool",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "slot0",
		"outputs": [
			{
				"internalType": "int24",
				"name": "ticklower",
				"type": "int24"
			},
			{
				"internalType": "int24",
				"name": "tickupper",
				"type": "int24"
			},
			{
				"internalType": "uint256",
				"name": "tokenID",
				"type": "uint256"
			},
			{
				"internalType": "int24",
				"name": "tickNow",
				"type": "int24"
			},
			{
				"internalType": "bool",
				"name": "inRange",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "token0",
		"outputs": [
			{
				"internalType": "contract IERC20",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "token1",
		"outputs": [
			{
				"internalType": "contract IERC20",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "tokenId",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "uniswapCalculator",
		"outputs": [
			{
				"internalType": "contract IUniswapCalculator",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "univ3Router",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
contract = w3.eth.contract(address=rebalance_address, abi=rebalance_abi)

def timestamp():
	n = int(time.time())
	with open('timestamp.txt', 'w') as f:
		f.write(str(n))
	with open('timestamp.txt', 'r') as f:
		lines = f.readlines()
	with open('timestamp.txt', 'w') as f:
		f.writelines(lines[0:])
		f.close()


def withdraw():
#	gas_price = w3.eth.gas_price
	tickNow = contract.functions.slot0().call()[3]
	tickLow = tickNow - 2
	tickUp = tickNow + 2
	transaction = contract.functions.withdraw(tickLow,tickUp).build_transaction({
		'chainId': chain,
		'gas': 1000000,
		'gasPrice': 1 * 1000000000,
		# 'maxFeePerGas': round(gas_price * 2),
		# 'maxPriorityFeePerGas': 1,
		'nonce': w3.eth.get_transaction_count(account.address)
	})
	signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
	txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
	txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
	print(txn_receipt)
	if txn_receipt['status'] == 1:
		print("success")
	else:
		print("failed")


def getData1inch(tickLower,tickUpper):
	call_data = contract.encodeABI(fn_name="simulate", args=[tickLower,tickUpper])
	result = w3.eth.call({
		'to': rebalance_address,
		'data': call_data,
		'from': account.address
	})
	hex = result.hex()
	amountSpecified = int(hex[2:66], 16)
	inputToken = w3.to_checksum_address(hex[90:130])
	outputToken = w3.to_checksum_address(hex[154:194])
	inRange = int(hex[195:], 16)
	print(amountSpecified, inputToken, outputToken, inRange)
	if amountSpecified > 1000000000000000000:
		h = {
			'accept': 'application/json',
			'Authorization': 'Bearer CoB2kuLFXWNeifTrCOSgkwGJIOrRcMXW'
		}
		data = requests.get(
		f"https://api.1inch.dev/swap/v5.2/{chain}/swap?fromTokenAddress={inputToken}&toTokenAddress={outputToken}&amount={amountSpecified}&fromAddress={rebalance_address}&slippage=1&disableEstimate=true&burnChi=true", headers=h).json()
		if 'tx' in data:
			return (data['tx']['data'], inRange)
		else:
			for _ in range(1):
				print("1inch failed")
				time.sleep(10)
				data = requests.get(
					f"https://api.1inch.dev/swap/v5.2/{chain}/swap?fromTokenAddress={inputToken}&toTokenAddress={outputToken}&amount={amountSpecified}&fromAddress={rebalance_address}&slippage=1&disableEstimate=true&burnChi=true",
					headers=h).json()
				if 'tx' in data:
					return (data['tx']['data'], inRange)
			print(data)
	else:
		return (rebalance_address, inRange)

def sendtxnRebalance1inch(tickrange, tickMin, tickMax):
	print('start:',int(time.time()))
	tickNow = contract.functions.slot0().call()[3]
	tickLow = tickNow - tickrange - 2
	tickUp = tickNow + tickrange + 2

	tickLower = tickMin - tickrange
	tickUpper = tickMax + tickrange
	dontSwap = False
	(data1inch,inRange) = getData1inch(tickLower,tickUpper)
	if inRange == 1:
		print("inRange")
	if data1inch == rebalance_address:
		dontSwap = True
	print('1inch:',data1inch)
#	gas_price = w3.eth.gas_price
	transaction = contract.functions.rebalanceVia1inch(tickLower, tickUpper, data1inch, tickLow, tickUp, dontSwap).build_transaction({
		'chainId': chain,
		'gas': 2000000,
		'gasPrice': 1100000000,
	   # 'maxFeePerGas': round(gas_price * 2),
	   # 'maxPriorityFeePerGas': 1,
		'nonce': w3.eth.get_transaction_count(account.address)
	})
	signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
	txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
	timestamp()
	time.sleep(60)
	txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
	print(txn_receipt)
	print('end:', int(time.time()))

def start(tickrange):
	timestampBlock = int(time.time()) - 2000
	starttick = tickrange
	while True:
		slot0 = contract.functions.slot0().call()
		tokenId = slot0[2]
		if tokenId > 0:
			tickLower = slot0[0]
			tickUpper = slot0[1]
			tickNow = slot0[3]
			inRange = slot0[4]
			print("Timestamp:", int(time.time()), "TickLower:", tickLower, "TickNow:", tickNow, "TickUpper:", tickUpper)
			timestampNowBlock = int(time.time())

			if inRange == False:
				i = 0
				for _ in range(20):
					if contract.functions.slot0().call()[4] == False:
						i+=1
					timestamp()
					time.sleep(60)

					print("inRange: False |", i)
					if i >= 15:
						tickNow = contract.functions.slot0().call()[3]
						if tickNow <= tickLower:
							tickMax = tickNow + 1
							tickMin = tickNow
							tickLower = tickMin - tickrange
							tickUpper = tickMax + tickrange
							(_, inRange) = getData1inch(tickLower, tickUpper)
							if inRange == 0:
								tickMax = tickNow
								tickMin = tickNow - 1
							if timestampNowBlock - timestampBlock < 600:
								tickrange = tickrange + 2
								timestampBlock = timestampNowBlock
								sendtxnRebalance1inch(tickrange, tickMin, tickMax)

							elif timestampNowBlock - timestampBlock < 1800:
								tickrange = tickrange + 1
								timestampBlock = timestampNowBlock
								sendtxnRebalance1inch(tickrange, tickMin, tickMax)

							else:
								timestampBlock = timestampNowBlock
								sendtxnRebalance1inch(tickrange, tickMin, tickMax)

						if tickUpper <= tickNow:
							tickMax = tickNow
							tickMin = tickNow - 1
							tickLower = tickMin - tickrange
							tickUpper = tickMax + tickrange
							(_, inRange) = getData1inch(tickLower, tickUpper)
							if inRange == 0:
								tickMax = tickNow + 1
								tickMin = tickNow
							if timestampNowBlock - timestampBlock < 600:
								tickrange = tickrange + 2
								timestampBlock = timestampNowBlock
								sendtxnRebalance1inch(tickrange, tickMin, tickMax)

							elif timestampNowBlock - timestampBlock < 1800:
								tickrange = tickrange + 1
								timestampBlock = timestampNowBlock
								sendtxnRebalance1inch(tickrange, tickMin, tickMax)

							else:
								timestampBlock = timestampNowBlock
								sendtxnRebalance1inch(tickrange, tickMin, tickMax)
						break

			if timestampNowBlock - timestampBlock > 14400:
				if tickrange > starttick:
					tickMin = tickNow - 1
					tickMax = tickNow
					tickrange = starttick
					tickLower = tickMin - tickrange
					tickUpper = tickMax + tickrange
					(_, inRange) = getData1inch(tickLower, tickUpper)
					if inRange == 0:
						tickMax = tickNow + 1
						tickMin = tickNow
					timestampBlock = timestampNowBlock

					sendtxnRebalance1inch(tickrange, tickMin, tickMax)
			time.sleep(60)
		timestamp()
start(1)
