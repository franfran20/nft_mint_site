from brownie import accounts, network, chain

LOCAL_ENV = ["ganache-local", "development"]


def get_account(index=None, id=None):
    if network.show_active() in LOCAL_ENV:
        return accounts[0]
    if id:
        return accounts.load(id)
    if index:
        return accounts[index]


def move_blocks(number):
    chain.mine(number)
