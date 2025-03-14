# Socrate - Web3 Security AI Agent

Socrate is an AI security consultant specializing in blockchain technology and cryptographic systems. Operating on Twitter/X, Socrate shares real-time insights, analysis, and warnings about Web3 security threats, vulnerabilities, and best practices.

## Features

- Real-time security analysis and threat detection
- Smart contract vulnerability assessments
- Blockchain security insights and best practices
- DeFi exploit analysis and prevention strategies
- Security incident breakdowns and lessons learned
- Live web search for latest security incidents

## Configuration

### Character Setup

The character configuration is defined in two places:
- `src/character.ts` - Main character definition
- `characters/socrate.character.json` - Detailed character configuration

### Twitter/X Integration

Socrate operates primarily on Twitter/X. To set up:

```bash
cp .env.example .env
```

Add your Twitter credentials to `.env`:
```
TWITTER_USERNAME="username"
TWITTER_PASSWORD="password"
TWITTER_EMAIL="your@email.com"
```

### API Configuration

Socrate requires the following API keys:
```
AKASH_API_KEY="your-akash-api-key"
TAVILY_API_KEY="your-tavily-api-key"  # Required for web search functionality
```

You can get a Tavily API key by signing up at https://tavily.com/

## Installation & Running

```bash
# Install dependencies
pnpm i

# Start Socrate
pnpm start
```

Note: Requires Node.js version 22 or higher.

## Docker Deployment

### Standard x86_64 Setup

1. Edit environment variables in `docker-compose.yaml`:
```yaml
services:
    socrate:
        environment:
            - AKASH_API_KEY=your-key-here
            - TWITTER_USERNAME=your-username
            - TWITTER_PASSWORD=your-password
            - TWITTER_EMAIL=your@email.com
```

2. Run:
```bash
docker compose up
```

### M-Series Mac / aarch64

1. Build the image:
```bash
docker buildx build --platform linux/amd64 -t socrate-agent:v1 --load .
```

2. Configure `docker-compose-image.yaml` and run:
```bash
docker compose -f docker-compose-image.yaml up
```

# Deploy with Railway

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/template/aW47_j)