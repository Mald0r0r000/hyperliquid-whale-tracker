#!/usr/bin/env python3
"""
Hyperliquid Whale Tracker - Runner
Monitors whale positions and sends Telegram alerts
"""
import argparse
import json
from datetime import datetime
from whale_tracker import WhaleTracker


def main():
    parser = argparse.ArgumentParser(description='Hyperliquid Whale Tracker')
    parser.add_argument('--winrates', action='store_true',
                       help='Calculate and display winrates for all whales')
    parser.add_argument('--sentiment', action='store_true',
                       help='Display current whale sentiment')
    parser.add_argument('--monitor', action='store_true', default=True,
                       help='Monitor positions and send alerts (default)')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🐋 HYPERLIQUID WHALE TRACKER")
    print("=" * 60)
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    tracker = WhaleTracker()
    
    if args.winrates:
        print("\n📊 Calculating winrates (30 days, min 5 trades)...\n")
        winrates = tracker.get_all_winrates(days=30, min_trades=5)
        
        print("\n" + "=" * 60)
        print("🏆 TOP WHALES BY WINRATE")
        print("=" * 60)
        
        for i, wr in enumerate(winrates[:15], 1):
            pnl_emoji = "🟢" if wr['total_pnl'] > 0 else "🔴"
            print(f"{i:2}. {wr['address_short']}: {wr['winrate']:5.1f}% WR | "
                  f"{wr['closed_trades']:4} trades | "
                  f"{pnl_emoji} ${wr['total_pnl']:>12,.0f}")
        
        return
    
    if args.sentiment:
        print("\n📊 Getting current sentiment...\n")
        sentiment = tracker.get_current_sentiment()
        
        print(f"🐋 Whales with BTC positions: {sentiment['whale_count']}")
        print(f"🟢 Total LONG: {sentiment['total_long_btc']:.2f} BTC")
        print(f"🔴 Total SHORT: {sentiment['total_short_btc']:.2f} BTC")
        print(f"📊 Long Ratio: {sentiment['long_ratio_pct']:.1f}%")
        print(f"🎯 Sentiment: {sentiment['sentiment']}")
        
        return
    
    # Default: monitor and alert
    print("\n🔍 Monitoring whale positions...\n")
    
    result = tracker.monitor_and_alert()
    
    print("\n" + "=" * 60)
    print("📋 SUMMARY")
    print("=" * 60)
    print(f"Changes detected: {result['changes_detected']}")
    print(f"Alerts sent: {result['alerts_sent']}")
    
    if result['changes']:
        print("\nChanges:")
        for change in result['changes']:
            emoji = "🟢" if change.get('direction') == 'LONG' or change.get('new_direction') == 'LONG' else "🔴"
            print(f"  {emoji} {change['type']}: {change['address_short']}")
    else:
        print("\n✅ No position changes detected")
    
    print("\n" + "=" * 60)
    print("✅ Done!")


if __name__ == "__main__":
    main()
