# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import eth_utils
from web3 import Web3


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/94bc20a138044cd7974fcd20b91d68ba'))


def print_transaction():
    transaction = w3.eth.getTransaction("0x43c4669cb248554d1d20edf166c2f79335eda2b7df5101bf483723b2b2904f21")
    for k, v in transaction.items():
        if k == "hash" or k == "blockHash":
            print(k, v.hex())
        else:
            print(k, v)


def print_block():
    all_burn_eth = 0
    block_count = 0
    from_block = 12965000
    to_block = w3.eth.get_block_number()
    for block_number in range(from_block, to_block + 1):
        # block = w3.eth.getBlock("0xdc0e0021f8b9c63c0b0217026eddb9ec9ad81156442fdfc8b6be90f38a131abb")
        block = w3.eth.getBlock(block_number)
        # for k, v in block.items():
        #     print(k, v)
        burn = eth_utils.from_wei(block.get("baseFeePerGas") * block.get("gasUsed"), "ether")
        print(f"block_number={block_number}, burn={burn}")
        all_burn_eth += burn
        block_count += 1
    print(f"from_block={from_block}, to_block={to_block}, all_burn_eth={all_burn_eth}, new ether={block_count * 2}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(w3.eth.coinbase)
    print()
    print_block()
