# solana-alert
Simple Solana/Velas alerting script. All data fetched from blockchain only.

You can configure alert script for monitor you nodes in next clusters:

- solana (devnet / testnet / mainnet)
- velas (testnet / mainnet)

## What is the script tracking?

- Delinquent status in blockchain
- Vote diff from absoluteSlot
- Node identity balance

## Alert targets

- Sending SMS to multiple numbers via smsc.ru
- Sending Telegram messages (todo)

## Installation
```
git clone https://github.com/myuriy/solana-alert.git
pip install -r requirements.txt
cp config.py config_local.py
# vim config_local.py

# Add monitor.py to crontab (15 min)
*/15 * * * * (cd /home/tools/solana-alert; python3 monitor.py)
```

## Configuration example
```python
CLUSTERS = {
    "velas-mainnet": {
        "rpc": "https://api.velas.com",             # cluster RPC URL 
        "min_node_balance": 10 * 1_000_000_000,     # min identity balance in lamports
        "max_vote_diff": 1,                         # max vote diff from absolute slot
        "nodes": {
            "9Ds8XQFwboS4qedw7Nbr8iMcdXwDHMDZh82onLVzQ4Vj": "nodescrew-velas",
            "H7DfLF7KpZFnfttsU4Tyx76ZX9YivpRZV9P3fKWzhR72": "Premagine"
        }
    }
}

HANDLERS = {
    "smsc": {
        "phones": [
            "+79876543210",
            "+70123456789"
        ],
        "login": "SMSC_LOGIN",
        "password": "SMSC_API_PASSWORD"
    }
}
```