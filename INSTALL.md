# Quick Install Guide

## New Installation (v2.0)

```bash
# Method 1: OpenClaw Skill (Recommended)
openclaw skills install persistent-memory
bash skills/persistent-memory/scripts/setup.sh  
python skills/persistent-memory/scripts/configure_openclaw.py

# Method 2: Manual Installation  
# Download files from this repository:
bash setup.sh
python configure_openclaw.py
```

## Upgrade from v1.x

```bash
# Download configure_openclaw.py from this repository
python configure_openclaw.py

# Restart OpenClaw
openclaw gateway restart

# Verify it works
openclaw memory search "test query"
```

## Verification

```bash
# Check that all workspace files are now indexed
openclaw memory search "your directive keywords"
# Should find content from SOUL.md, AGENTS.md, etc.

# Check memory system status  
vector_memory/venv/bin/python vector_memory/auto_retrieve.py --status
```

## Support

- Read GUIDE.md for complete instructions
- Check CHANGELOG.md for version differences
- See SKILL_REFERENCE.md for OpenClaw skill details
