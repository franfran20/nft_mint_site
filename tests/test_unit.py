from brownie import accounts, network
import pytest
import brownie
from web3 import Web3
from scripts.helpful_scripts import LOCAL_ENV, get_account
from scripts.deploy import deploy


def test_owner_can_mint_free():
    account = get_account()
    if network.show_active() not in LOCAL_ENV:
        pytest.skip("only for dev chain...")
    fran_fran = deploy(account)
    fran_fran.mint(2, {"from": account})
    tokenid1_owner = fran_fran.ownerOf(1)
    assert tokenid1_owner == account.address
    with brownie.reverts():
        fran_fran.mint(1, {"from": accounts[2], "amount": Web3.toWei(0.1, "ether")})


def test_whitelist_users():
    account = get_account()
    if network.show_active() not in LOCAL_ENV:
        pytest.skip("only for dev chain...")
    fran_fran = deploy(account)
    fran_fran.whitelistUsers(
        [accounts[1].address, accounts[2].address], {"from": account}
    )
    assert fran_fran.isWhitelisted(accounts[1].address) == True
    assert fran_fran.isWhitelisted(accounts[2].address) == True


def test_normal_user_cant_mint_during_whitelist():
    account = get_account()
    if network.show_active() not in LOCAL_ENV:
        pytest.skip("only for dev chain...")
    fran_fran = deploy(account)
    with brownie.reverts():
        fran_fran.mint(2, {"from": accounts[1], "amount": Web3.toWei(0.02, "ether")})


def test_normal_user_can_mint_after_whitelist():
    account = get_account()
    if network.show_active() not in LOCAL_ENV:
        pytest.skip("only for dev chain...")
    fran_fran = deploy(account)
    fran_fran.setOnlyWhitelisted(False, {"from": account})
    fran_fran.mint(2, {"from": accounts[1], "amount": Web3.toWei(0.02, "ether")})


def test_cant_mint_more_than_allowed_whitelist_limit():
    account = get_account()
    if network.show_active() not in LOCAL_ENV:
        pytest.skip("only for dev chain...")
    fran_fran = deploy(account)
    fran_fran.whitelistUsers(
        [accounts[1].address, accounts[2].address], {"from": account}
    )
    with brownie.reverts():
        fran_fran.mint(2, {"from": accounts[1], "amount": Web3.toWei(0.02, "ether")})
