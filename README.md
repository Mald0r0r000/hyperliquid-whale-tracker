# Hyperliquid Whale Tracker 🐋

Real-time monitoring of top Hyperliquid traders' BTC positions with Telegram notifications.

## Features

- 🐋 **36 Whale Wallets** - High-winrate traders tracked
- 📊 **Winrate Analysis** - Performance metrics per wallet
- 🔔 **Telegram Alerts** - Instant notifications for:
  - New BTC positions opened
  - Direction changes (flips)
  - Position size increases (>50%)
- ⚡ **GitHub Actions** - Automated monitoring every 5 minutes

## Top Performers (30-day)

| Wallet | Winrate | Trades | PnL |
|--------|---------|--------|-----|
| `0x418aa6bf...` | **100%** | 103 | +$503,762 |
| `0xf97ad670...` | **100%** | 22 | +$1,247 |
| `0x11eee2e0...` | **100%** | 97 | +$16,301 |
| `0xad572a78...` | **98.5%** | 66 | +$1,324 |

## Setup

### 1. Fork this repository

### 2. Configure Secrets

Add these secrets in your GitHub repository settings:

| Secret | Description |
|--------|-------------|
| `TELEGRAM_BOT_TOKEN` | Your Telegram bot token |
| `TELEGRAM_CHAT_ID` | Your chat ID for notifications |

### 3. Enable GitHub Actions

The workflow runs automatically every 5 minutes.

## Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Run tracker
python runner.py

# Calculate winrates
python runner.py --winrates
```

## Notification Examples

**New Position:**
```
🐋 WHALE ALERT 🟢

Nouvelle position BTC
📍 0x418aa6bf...
📊 LONG 50.00 BTC
💰 Entry: $95,000
⚡ Leverage: 20x
💼 Account: $2,164,930
```

**Direction Flip:**
```
🔄 WHALE FLIP

Changement de direction!
📍 0x7ca165f3...
❌ LONG → ✅ SHORT
📊 Size: 203.53 BTC
⚡ Leverage: 13x
```

## Related Projects

- [BTC Sniper Bot](https://github.com/Mald0r0r000/btc-sniper-bot) - Institutional-grade BTC signal generator

## License

MIT
