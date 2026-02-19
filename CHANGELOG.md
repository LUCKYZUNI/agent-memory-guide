# Changelog - Persistent Memory for AI Agents

## Version 2.0 (February 19, 2026) - CRITICAL UPDATE

### 🚨 Breaking Changes
- **OpenClaw integration configuration now required** for proper directive compliance
- Agents using v1.x are vulnerable to directive ignorance failures

### ✅ New Features
- **`configure_openclaw.py`** - Automatic OpenClaw memory configuration script
- **Complete workspace indexing** - SOUL.md, AGENTS.md, PROJECTS.md, reference/ files now searchable
- **Directive compliance automation** - Rules and directives found automatically in memory searches
- **Backup and verification** - Configuration script includes safety checks and rollback
- **Enhanced setup process** - Two-step installation with critical integration warning

### 🔧 Fixes
- **Fixed: Agents ignoring workspace directives** - Root cause was missing OpenClaw memorySearch configuration
- **Fixed: Partial memory indexing** - OpenClaw now indexes all critical workspace files, not just MEMORY.md
- **Fixed: Optional directive compliance** - Memory retrieval now mandatory through infrastructure integration
- **Fixed: Memory search gaps** - No more "directive not found" when rules exist in workspace files

### 📚 Documentation
- **Updated complete guide** with OpenClaw integration section
- **New troubleshooting section** for directive compliance issues  
- **Enhanced setup instructions** with v2.0 requirements
- **Added upgrade path** for existing v1.x users

### 🎯 Impact
- **Prevents operational failures** where agents violate explicit rules
- **Ensures directive compliance** through automatic memory integration
- **Maintains backward compatibility** - v1.x installations can upgrade easily
- **Addresses community vulnerability** - 23+ stars, 4+ forks now protected

---

## Version 1.0 (February 16, 2026) - Initial Release

### ✅ Features
- **Three-layer memory architecture** - Markdown + ChromaDB + NetworkX
- **Semantic search** - Vector similarity search with sentence-transformers
- **Knowledge graph** - Relationship traversal between concepts
- **Auto-indexing** - Single command updates all memory layers
- **Sync monitoring** - Health checks and out-of-sync detection
- **OpenClaw skill packaging** - One-command installation

### 📚 Documentation  
- **Complete implementation guide** - Step-by-step with working code
- **Architecture documentation** - Visual diagrams and data flow
- **Troubleshooting guide** - Common issues and solutions
- **Lessons learned** - 11 hard-learned insights from production use

### 🐛 Known Issues (Fixed in v2.0)
- ❌ **Agents could ignore memory** - Memory retrieval was optional, not mandatory
- ❌ **Partial OpenClaw indexing** - Only MEMORY.md indexed, not directive files
- ❌ **Directive compliance gaps** - Agents violated rules not found in memory searches
- ❌ **Setup complexity** - Required manual OpenClaw configuration (now automated)

---

## Upgrade Instructions

### From v1.x to v2.0

**Critical:** v1.x users are vulnerable to directive compliance failures.

```bash
# Download configure_openclaw.py from this repository
python configure_openclaw.py

# Restart OpenClaw to apply changes
openclaw gateway restart

# Verify directive files are now indexed
openclaw memory search "your directive keywords"
```

### New Installation

```bash
# Use OpenClaw skill (recommended)
openclaw skills install persistent-memory
bash skills/persistent-memory/scripts/setup.sh
python skills/persistent-memory/scripts/configure_openclaw.py

# Verify everything works
vector_memory/venv/bin/python vector_memory/auto_retrieve.py --status
```

---

## Version Compatibility

- **v2.0**: OpenClaw 2026.2.17+ (includes memorySearch configuration)  
- **v1.0**: OpenClaw 2026.2.15+ (partial memory integration)

## Support

**Directive compliance issues?** You likely need the v2.0 OpenClaw integration.  
**Memory not syncing?** Check the troubleshooting guide in the complete documentation.  
**Installation problems?** Ensure you're running both setup steps (memory system + OpenClaw config).

---

*Version 2.0 addresses the critical infrastructure gap that allowed agents to ignore their own directives. Every v1.x installation should upgrade immediately.*