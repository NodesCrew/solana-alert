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

# Add monitor.py to crontab (15 min)
*/15 * * * * (cd /home/tools/solana-alerts; python3 monitor.py)
```