# ZeroBounce Email Validation Setup

## Installation
```bash
pip3 install zerobounce
```

## API Key Setup

1. **Get API Key:**
   - Go to https://www.zerobounce.net/
   - Create a free account
   - Get your API key from the dashboard
   - Free tier: 100 validations/month

2. **Set API Key:**
   ```bash
   export ZEROBOUNCE_API_KEY="your-api-key-here"
   ```
   
   Or add to your `~/.zshrc`:
   ```bash
   echo 'export ZEROBOUNCE_API_KEY="your-api-key-here"' >> ~/.zshrc
   ```

## Usage

### Validate Single Email
```bash
python3 /Users/julienuhlig/.openclaw/workspace/tools/zerobounce_check.py "test@example.com"
```

### Batch Validation (Coming Soon)
```bash
python3 /Users/julienuhlig/.openclaw/workspace/tools/zerobounce_check.py --file emails.txt
```

## Response Status Codes

| Status | Meaning |
|--------|---------|
| valid | Email is valid |
| invalid | Email is invalid |
| catch-all | Domain accepts all emails |
| unknown | Cannot verify |
| spamtrap | Known spam trap |
| abuse | Known complainer |
| do_not_mail | Do not email this address |

## Status: Ready
ZeroBounce is installed at: `/Users/julienuhlig/.openclaw/workspace/tools/zerobounce_check.py`

**Next step:** Get API key from zerobounce.net and set ZEROBOUNCE_API_KEY environment variable.
