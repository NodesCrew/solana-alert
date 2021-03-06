# coding: utf-8

DIR_LOGS = "log"

CLUSTERS = {
    "solana-devnet": {
        "rpc": "",
        "max_vote_diff": 1,
        "min_node_balance": 0 * 1_000_000_000,
        "nodes": {
            "identity": "name"
        }
    },

    "solana-mainnet": {
        "rpc": "https://api.mainnet-beta.solana.com",
        "max_vote_diff": 1,
        "min_node_balance": 1 * 1_000_000_000,
        "nodes": {
            "identity": "name"
        }
    },

    "solana-testnet": {
        "rpc": "https://api.testnet.solana.com",
        "max_vote_diff": 1,
        "min_node_balance": 10 * 1_000_000_000,
        "nodes": {
            "identity": "name"
        }
    },

    "velas-mainnet": {
        "rpc": "https://api.velas.com",
        "min_node_balance": 10 * 1_000_000_000,
        "max_vote_diff": 1,
        "nodes": {
            "9Ds8XQFwboS4qedw7Nbr8iMcdXwDHMDZh82onLVzQ4Vj": "nodescrew-velas",
            "H7DfLF7KpZFnfttsU4Tyx76ZX9YivpRZV9P3fKWzhR72": "Premagine"
        }
    },

    "velas-testnet": {
        "rpc_url": "https://api.testnet.velas.com",
        "max_vote_diff": 10,
        "min_node_balance": 0 * 1_000_000_000,
        "nodes": {
            "identity": "name"
        }
    },
}


HANDLERS = {
    "smsc": {
        "phones": [
            "+79876543210",
            "+70123456789"
        ],
        "login": "SMSC_LOGIN",
        "password": "SMSC_API_PASSWORD"
    },

    "telegram": {
        "token": "INT:STR",
    }
}

try:
    from config_local import *
except ImportError:
    print("Unable to load local config")
    exit(-1)