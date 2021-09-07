# This is a sample Python script.

from concurrent.futures import ThreadPoolExecutor
from concurrent import futures

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import eth_utils
from web3 import Web3


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/9b5196e976fe40babdbf6d83d497f074'))


def print_transaction():
    transaction = w3.eth.getTransaction("0x43c4669cb248554d1d20edf166c2f79335eda2b7df5101bf483723b2b2904f21")
    for k, v in transaction.items():
        if k == "hash" or k == "blockHash":
            print(k, v.hex())
        else:
            print(k, v)


def print_designated_block(from_block, end_block):
    for block_number in range(from_block, end_block):
        # block = w3.eth.getBlock("0xdc0e0021f8b9c63c0b0217026eddb9ec9ad81156442fdfc8b6be90f38a131abb")
        block = w3.eth.getBlock(block_number)
        # for k, v in block.items():
        #     print(k, v)
        burn = eth_utils.from_wei(block.get("baseFeePerGas") * block.get("gasUsed"), "ether")
        print(f"block_number={block_number}, burn={burn}")


executor = ThreadPoolExecutor(max_workers=10)


def print_block():
    from_block = 13079315
    end_block = w3.eth.get_block_number()
    fs = []
    while from_block < end_block:
        to_block = from_block + 1000
        fs.append(executor.submit(print_designated_block, from_block, to_block))
        # print(f"from_block={from_block}, to_block={to_block}")
        from_block = to_block
    for f in futures.as_completed(fs):
        result = f.result()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(w3.eth.coinbase)
    print()
    print_block()
