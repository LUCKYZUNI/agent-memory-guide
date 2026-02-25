# Building Persistent Memory for AI Agents

[![GitHub Sponsors](https://img.shields.io/github/sponsors/Jakebot-ops?style=flat&logo=github&label=Sponsor%20Jakebot%20Labs&color=ea4aaa)](https://github.com/sponsors/Jakebot-ops)


## 🚨 CRITICAL UPDATE: Version 2.0 (February 2026)

**If you're using version 1.x, you MUST upgrade to prevent agents ignoring workspace directives.**

### The Problem We Discovered

OpenClaw's built-in memory system only indexes `MEMORY.md` by default - it completely ignores critical files like:
- `SOUL.md` (agent directives)
- `AGENTS.md` (behavior rules) 
- `PROJECTS.md` (active work)
- `reference/` (institutional knowledge)

**Result:** Agents violate explicit rules because the rules aren't found in memory searches.

### The Fix

Version 2.0 includes `configure_openclaw.py` which automatically configures OpenClaw to index ALL workspace files, making directive compliance automatic rather than optional.

---

## Quick Start

### New Installation (v2.0)

```bash
# Option 1: Use OpenClaw Skill (Recommended)
openclaw skills install persistent-memory
bash skills/persistent-memory/scripts/setup.sh
python skills/persistent-memory/scripts/configure_openclaw.py

# Option 2: Manual Installation
# Download scripts from this repository and run:
bash setup.sh
python configure_openclaw.py
```

### Upgrade from v1.x

```bash
# Just run the configuration fix
python configure_openclaw.py
```

### Verify It Works

```bash
# Test that directive files are now searchable
openclaw memory search "your directive keywords"
# Should find content from SOUL.md, AGENTS.md, etc.
```

---

## What You Get

### Three-Layer Memory Architecture

1. **Layer 1: Markdown** - Human-readable knowledge in `MEMORY.md` + daily logs
2. **Layer 2: Vector** - ChromaDB semantic search across all memories  
3. **Layer 3: Graph** - NetworkX relationship traversal between concepts

### The Critical Integration

**v2.0 bridges OpenClaw's automatic memory system with comprehensive workspace indexing.**

Without this integration, agents can ignore their own directives. With it, directive compliance becomes automatic.

---

## The Complete Guide

**[📖 Read the Full Guide](GUIDE.md)** - Step-by-step instructions for building production-ready agent memory, including:

- Why markdown alone isn't enough
- How to implement vector search with ChromaDB
- Building knowledge graphs with NetworkX
- Making memory retrieval mandatory (not optional)
- The failure that taught us everything
- 12 hard-learned lessons with solutions
- Complete working code

---

## Key Features

- **🧠 Semantic Memory** - Find related information by meaning, not keywords
- **🕸️ Knowledge Graph** - Understand relationships between concepts
- **🔒 Mandatory Retrieval** - Agents cannot bypass memory searches
- **📊 Sync Monitoring** - Automatic detection when memory goes stale
- **⚡ Fast Setup** - One command installation with OpenClaw
- **🛡️ Production Ready** - Tested in real operational environments

---

## The Story

This guide was born from a real failure: our AI agent forgot it had its own memory database during a routine maintenance task. It spent hours rebuilding information that was already stored in ChromaDB.

**The lesson:** A memory system the agent can choose to ignore is not a memory system. It's a suggestion.

Version 2.0 solves this by making memory retrieval **infrastructure-level** rather than **tool-level**.

---

## Community

- **Stars:** 23+ GitHub users depending on this solution
- **Forks:** 4+ active development branches
- **Impact:** Prevents operational failures in production AI agents

---

## Files in This Repository

- **`GUIDE.md`** - Complete implementation guide
- **`configure_openclaw.py`** - OpenClaw integration script (v2.0 fix)
- **`setup.sh`** - Automated setup script
- **`SKILL_REFERENCE.md`** - OpenClaw skill documentation

---

## Support

If you're experiencing agents that ignore workspace directives, you likely need the v2.0 OpenClaw integration fix. Run `configure_openclaw.py` and restart OpenClaw.

For other issues, see the troubleshooting section in the complete guide.

---

*Built through 5 days of real production failures, including every mistake documented. The agent memory system that forgot itself exists.*