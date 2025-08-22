# 🤖 DISCORD BOT COMMANDS

## 📋 SUMMARY COMMANDS

### Basic Summary Commands
- `!summarize` - Generate 12-hour summary with premium AI (Gemini 2.5 Pro)
- `!summarize [hours]` - Generate summary for specified hours (1-72)
- `!summarize [model] [hours]` - Generate summary with specific AI model
- `!sum [hours]` - Quick summary shortcut command
- `!summary [hours]` - Alternative summary command

### Summary Examples
```
!summarize                    → Last 12 hours with premium AI
!summarize 6                  → Last 6 hours summary
!summarize v3 24              → Last 24 hours with DeepSeek V3
!summarize free 48            → Last 48 hours with free model
!sum 12                       → Quick 12-hour summary
```

## 🔍 WORD SEARCH COMMANDS ✨ NEW!

### Basic Search Commands
- `!wordsearch "term" [hours] [details]` - Search with sentiment analysis
- `!ws "term" [hours]` - Quick word search (shortcut)
- `!search "term" [hours]` - Alternative search command

### Search Parameters
- **term**: Word or phrase to search (use quotes for phrases)
- **hours**: Hours to look back (1-168, default: 7)
- **details**: Show examples? (yes/no, default: no)

### Search Examples
```
!wordsearch "bitcoin"         → Search "bitcoin" in last 7 hours with sentiment
!ws "pump" 24                 → Search "pump" in last 24 hours
!search "DeFi protocol" 12 yes → Search phrase with detailed examples
!wordsearch "moon" 48         → Search "moon" in last 48 hours
!ws "rugpull" 72 yes          → Search with sentiment examples
!search "alpha" 6             → Search "alpha" in last 6 hours
```

## ℹ️ HELP COMMANDS

- `!helpbot` - Show all available commands overview
- `!help_summary` - Detailed help for summary commands
- `!help_search` - Detailed help for search commands

## ⚙️ AI MODEL OPTIONS

### Available Models
- **`pro`** 🔥 - Gemini 2.5 Pro (best quality, default)
- **`v3`** 💰 - DeepSeek V3 (budget option)
- **`free`** 🆓 - DeepSeek R1 Distill (zero cost)

### Model Usage Examples
```
!summarize pro 12             → Premium model, 12 hours
!summarize v3 24              → Budget model, 24 hours
!summarize free 6             → Free model, 6 hours
```

## 📊 WORD SEARCH FEATURES

### Sentiment Analysis
- 😊 **Positive sentiment** - Detects bullish, optimistic mentions
- 😔 **Negative sentiment** - Detects bearish, pessimistic mentions
- 😐 **Neutral sentiment** - Detects factual, objective mentions

### Search Results Include
- 📝 **Total mentions** count
- 📊 **Sentiment breakdown** with percentages
- 👥 **Unique user counts** who mentioned the term
- 📈 **Overall sentiment trends**
- 📍 **Channel breakdown** showing mentions per channel
- 💬 **Example quotes** (most positive/negative mentions when details=yes)

### Sample Search Output
```
📊 Search Results for "bitcoin" (Last 24 hours)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 Total Mentions: 23
😊 Positive: 14 (61%)
😔 Negative: 6 (26%)
😐 Neutral: 3 (13%)

👥 Unique Users: 8
📈 Overall Sentiment: Mostly Positive (61%)

📊 Channel Breakdown:
• general: 12 mentions
• trading: 8 mentions
• defi-alpha: 3 mentions
```

## ⏰ TIME RANGES

- **Summary Commands**: 1-72 hours
- **Search Commands**: 1-168 hours (1 week maximum)
- **Default**: 12 hours (summary), 7 hours (search)

## 🎯 QUICK REFERENCE

### Most Common Commands
```
!summarize                    → Quick daily summary
!ws "bitcoin"                 → Bitcoin sentiment check
!search "alpha" 24 yes        → Alpha mentions with examples
!sum 6                        → Quick 6-hour summary
!helpbot                      → Show all commands
```

### Advanced Usage
```
!wordsearch "pump and dump" 48 yes    → Multi-word phrase search
!summarize v3 72                       → Long-term budget summary
!ws "moon" 168                         → Week-long sentiment tracking
```

## 🚀 BOT STATUS

- ✅ **Status**: Online and ready
- 🔄 **Last Updated**: Added sentiment-powered word search
- 🤖 **Bot Name**: SS#6709
- 📡 **Channels Monitored**: 4 channels
- 🕐 **Daily Summary**: 7:30 AM Arizona Time

---

**Need help?** Use `!helpbot` for interactive assistance or `!help_search` for detailed search help.
