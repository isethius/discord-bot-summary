# 🚀 QUICK BOT RESTART & COMMANDS

## 🔄 RESTART BOT COMMANDS
```bash
# Navigate to bot directory
cd "/Users/andrewferguson/discord summarizer/DiscordV2Bot"

# Start the bot (ordinals config)
python3 fast_summarizer.py --config ordinals

# Alternative: Start with DeFi config
python3 fast_summarizer.py --config defi

# Debug mode (prints messages, doesn't send)
python3 fast_summarizer.py --config ordinals --debug

# Check if bot is running
ps aux | grep fast_summarizer

# Kill bot if needed
pkill -f fast_summarizer
```

## 🤖 MOST USED DISCORD COMMANDS

### ⚡ Quick Commands
- `!summarize` - 12-hour summary (premium AI)
- `!sum 6` - Quick 6-hour summary
- `!ws "bitcoin"` - Search "bitcoin" with sentiment
- `!helpbot` - Show all commands

### 📊 Summary Commands
- `!summarize [hours]` - Generate summary (1-72 hours)
- `!summarize pro 24` - Premium AI, 24 hours
- `!summarize v3 12` - Budget AI, 12 hours
- `!summarize free 6` - Free AI, 6 hours

### 🔍 Word Search Commands
- `!wordsearch "term" [hours] [details]` - Full search
- `!ws "pump" 24` - Quick search, 24 hours
- `!search "DeFi" 12 yes` - Search with examples

### ℹ️ Help Commands
- `!helpbot` - All commands overview
- `!help_summary` - Summary help
- `!help_search` - Search help

## 🛠️ TROUBLESHOOTING

### If Bot Goes Down
1. Check if running: `ps aux | grep fast_summarizer`
2. Kill if stuck: `pkill -f fast_summarizer`
3. Restart: `python3 fast_summarizer.py --config ordinals`

### Common Issues
- **Port issues**: Bot uses Discord WebSocket, not HTTP ports
- **Token issues**: Check `.env` file for BOT_TOKEN and DISCORD_TOKEN
- **Permission issues**: Bot needs "Send Messages" + "Read Message History"
- **Rate limiting**: Bot has built-in delays, should handle automatically

### Debug Mode
```bash
# Test without sending messages
python3 fast_summarizer.py --config ordinals --debug --hours 2
```

## 📱 BOT STATUS
- **Config**: Ordinals
- **Daily Summary**: 7:30 AM Arizona Time
- **Models**: Gemini 2.5 Pro (default), DeepSeek V3, Free options
- **Features**: Summaries, Word Search with Sentiment Analysis

