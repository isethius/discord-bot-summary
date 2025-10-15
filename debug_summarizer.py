#!/usr/bin/env python3
"""
Debug script for Discord Summarizer
This will help identify configuration and connectivity issues
"""
import os
from dotenv import load_dotenv

def check_env_vars():
    """Check all required environment variables"""
    load_dotenv()
    
    print("=== Environment Variables Check ===")
    
    # Required for all configs
    openrouter_key = os.getenv('OPENROUTER_API_KEY')
    bot_token = os.getenv('BOT_TOKEN')
    discord_token = os.getenv('DISCORD_TOKEN')
    
    print(f"OPENROUTER_API_KEY: {'✓ SET' if openrouter_key else '✗ MISSING'}")
    print(f"BOT_TOKEN: {'✓ SET' if bot_token else '✗ MISSING'}")
    print(f"DISCORD_TOKEN: {'✓ SET' if discord_token else '✗ MISSING'}")
    
    # Check DeFi config
    print("\n--- DeFi Configuration ---")
    defi_channels = os.getenv('DEFI_CHANNEL_IDS')
    defi_output = os.getenv('DEFI_OUTPUT_CHANNEL_ID')
    
    print(f"DEFI_CHANNEL_IDS: {'✓ SET' if defi_channels else '✗ MISSING'}")
    if defi_channels:
        channel_count = len([id for id in defi_channels.split(',') if id.strip()])
        print(f"  → {channel_count} channel(s) configured")
    
    print(f"DEFI_OUTPUT_CHANNEL_ID: {'✓ SET' if defi_output else '✗ MISSING'}")
    
    # Check Ordinals config
    print("\n--- Ordinals Configuration ---")
    ordinals_channels = os.getenv('ORDINALS_CHANNEL_IDS')
    ordinals_output = os.getenv('ORDINALS_OUTPUT_CHANNEL_ID')
    
    print(f"ORDINALS_CHANNEL_IDS: {'✓ SET' if ordinals_channels else '✗ MISSING'}")
    if ordinals_channels:
        channel_count = len([id for id in ordinals_channels.split(',') if id.strip()])
        print(f"  → {channel_count} channel(s) configured")
    
    print(f"ORDINALS_OUTPUT_CHANNEL_ID: {'✓ SET' if ordinals_output else '✗ MISSING'}")
    
    return {
        'openrouter_key': bool(openrouter_key),
        'bot_token': bool(bot_token),
        'discord_token': bool(discord_token),
        'defi_complete': bool(defi_channels and defi_output),
        'ordinals_complete': bool(ordinals_channels and ordinals_output)
    }

def test_openrouter_connection():
    """Test OpenRouter API connectivity"""
    import requests
    
    print("\n=== OpenRouter API Test ===")
    
    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        print("✗ Cannot test - OPENROUTER_API_KEY not set")
        return False
    
    # Test with a simple request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://github.com/DiscordV2Bot",
        "X-Title": "Discord Fast Channel Summarizer - Debug"
    }
    
    payload = {
        "model": "anthropic/claude-3.7-sonnet",
        "messages": [
            {"role": "user", "content": "Say 'API test successful' if you can read this."}
        ],
        "max_tokens": 20
    }
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            print("✓ OpenRouter API connection successful")
            result = response.json()
            if "choices" in result and len(result["choices"]) > 0:
                print(f"✓ API Response: {result['choices'][0]['message']['content']}")
            return True
        else:
            print(f"✗ OpenRouter API error: {response.status_code}")
            print(f"  Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"✗ OpenRouter API connection failed: {e}")
        return False

def test_discord_bot_connection():
    """Test Discord bot token validity"""
    import discord
    import asyncio
    
    print("\n=== Discord Bot Token Test ===")
    
    bot_token = os.getenv('BOT_TOKEN')
    if not bot_token:
        print("✗ Cannot test - BOT_TOKEN not set")
        return False
    
    async def test_bot():
        try:
            client = discord.Client(intents=discord.Intents.default())
            
            @client.event
            async def on_ready():
                print(f"✓ Bot token valid - logged in as {client.user}")
                await client.close()
            
            await client.start(bot_token)
            return True
            
        except discord.LoginFailure:
            print("✗ Invalid BOT_TOKEN")
            return False
        except Exception as e:
            print(f"✗ Bot connection error: {e}")
            return False
    
    try:
        return asyncio.run(test_bot())
    except Exception as e:
        print(f"✗ Bot test failed: {e}")
        return False

def main():
    """Run all diagnostic tests"""
    print("Discord Summarizer Debug Tool")
    print("=" * 40)
    
    # Check environment variables
    env_status = check_env_vars()
    
    # Test API connections
    openrouter_ok = test_openrouter_connection()
    bot_ok = test_discord_bot_connection()
    
    # Summary
    print("\n" + "=" * 40)
    print("DIAGNOSIS SUMMARY")
    print("=" * 40)
    
    all_good = True
    
    if not (env_status['bot_token'] or env_status['discord_token']):
        print("✗ CRITICAL: No Discord tokens configured")
        all_good = False
    
    if not env_status['openrouter_key']:
        print("✗ CRITICAL: OpenRouter API key missing")
        all_good = False
    
    if not (env_status['defi_complete'] or env_status['ordinals_complete']):
        print("✗ CRITICAL: No complete channel configuration found")
        all_good = False
    
    if not openrouter_ok:
        print("✗ WARNING: OpenRouter API not accessible")
        all_good = False
    
    if not bot_ok and env_status['bot_token']:
        print("✗ WARNING: Bot token invalid or connection failed")
        all_good = False
    
    if all_good:
        print("✓ All checks passed! Your configuration looks good.")
        print("\nNext steps:")
        print("1. Try running in debug mode: python fast_summarizer.py --debug")
        print("2. If debug works, try normal mode: python fast_summarizer.py")
    else:
        print("\n✗ Issues found. Please fix the above problems before running the summarizer.")
    
    print("\nFor more help, check your .env file and ensure all required variables are set.")

if __name__ == "__main__":
    main()