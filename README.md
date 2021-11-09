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