from brownie import FranFran, accounts
from web3 import Web3
from scripts.helpful_scripts import move_blocks
from scripts.helpful_scripts import get_account


account = get_account(id="francis-test")


def deploy(acct):
    fran_fran = FranFran.deploy(
        "FranFran1",
        "FF1",
        "https://ipfs.io/ipfs/QmbJ5yKwWJ7zS9bqrxWnxQxDVzmyiM7ivhE8bQXQoqkY4H/",
        {"from": acct},
    )
    print("FranFran1 contract deployed!")
    return fran_fran


def mint(number, acct, value=0):
    fran_fran = FranFran[-1]
    tx_mint = fran_fran.mint(number, {"from": acct, "value": value})
    tx_mint.wait(1)
    print(f"{fran_fran.totalSupply()}")


def whitelist_users(addresses_array):
    fran_fran = FranFran[-1]
    tx_whitelist = fran_fran.whitelistUsers(addresses_array, {"from": account})
    tx_whitelist.wait(1)


def toggle_whitelist(acct, boolean):
    fran_fran = FranFran[-1]
    tx_set = fran_fran.setOnlyWhitelisted(boolean, {"from": acct})
    tx_set.wait(1)


def total_supply():
    tot_supply = FranFran[-1].totalSupply()
    print(f"{tot_supply}")


def main():
    deploy(account)
    toggle_whitelist(account, False)
    # move_blocks(2)
    total_supply()
