# Give Your OpenClaw Bot a Real Memory
### A Step-by-Step Guide for the OpenClaw Community

---

**The problem:** Your bot wakes up every session with amnesia. MEMORY.md helps, but it's limited — no search, no relationships, no way to guarantee the bot actually uses it. This guide gives your bot a three-layer memory system it *can't* ignore.

**Time required:** ~2 hours across 3 sessions
**Skill level:** You should be comfortable editing SOUL.md and running Python scripts
**What you'll have when done:** Semantic search across all your bot's memories + a knowledge graph of connected concepts + a sync watchdog that catches when things drift

---

## What You're Building

| Layer | What It Does | Tech |
|-------|-------------|------|
| **L1: Markdown** | Human-readable memory (you already have this) | MEMORY.md |
| **L2: Vector Search** | "Find memories *similar to* this question" | ChromaDB + SentenceTransformers |
| **L3: Knowledge Graph** | "What concepts are *connected to* this?" | NetworkX |
| **Glue: Auto-Retrieve** | Forces the bot to check memory before every response | Python script |

---

## Before You Start

Your bot needs:
- A `MEMORY.md` file structured with `##` headers (each header = one searchable chunk)
- Python 3.10+ on the host
- ~500MB disk space for the ML model (downloads once)

---

## Phase 1: Install the Memory Stack

**Add this to your SOUL.md** (tells your bot what to build during idle cycles):

```markdown
## Memory Upgrade Roadmap (execute in order during idle cycles)

**Phase 1: Dependency Setup**
- Use only libraries available in standard Python environments or easily installable via pip in a virtualenv.
- Preferred stack (2026 state-of-the-art, lightweight):
  - Embeddings: sentence-transformers (all-MiniLM-L6-v2 or all-mpnet-base-v2 for best quality/speed)
  - Vector DB: chromadb (persistent, simple, no server needed) or faiss-cpu
  - Graph: networkx + optional neo4j (start with networkx in-memory, persist to JSON)
- During next 3 idle sessions: Research and propose exact pip install commands + version pins for a minimal, conflict-free setup. Commit to a new requirements.txt.

**Phase 2: Vector Memory Layer**
- Create vector_memory/ directory.
- Index all existing MEMORY.md sections + SQLite entries as embeddings.
- Add semantic search function: query → top-k similar memories.
- Fallback to keyword if embeddings fail.

**Phase 3: Graph Layer**
- Build a knowledge graph where nodes = concepts/decisions/code patterns, edges = relations (e.g. "depends_on", "improved_by", "tested_in").
- Auto-extract relations during every MEMORY.md update.
- Enable queries like "show chain of decisions leading to current control loop".

All phases must:
- Be committed step-by-step to GitHub
- Include rollback instructions
- Update MEMORY.md with progress
- Never break existing text/SQLite memory
```

**Or install it yourself** (if you don't want to wait for idle cycles):

```bash
cd ~/.openclaw/workspace
mkdir -p vector_memory && cd vector_memory
python3 -m venv venv
venv/bin/pip install sentence-transformers chromadb networkx
```

---

## Phase 2: Build the Vector Layer

### Option A: Let Your Bot Do It

Send this to your bot in a fresh session:

> Begin Phase 1 of the Memory Upgrade Roadmap immediately.
>
> Research the optimal, minimal, conflict-free dependency stack for local vector + graph memory using up-to-date 2026 knowledge.
>
> Prioritize:
> - Lightweight, high-quality embeddings (prefer all-MiniLM-L6-v2 class or better)
> - Persistent local vector DB with zero-config setup (ChromaDB strongly preferred over FAISS for simplicity and built-in persistence)
> - Simple graph handling (NetworkX)
>
> Propose:
> - Exact pip install commands with pinned versions
> - A new file: requirements-memory.txt
> - Brief rationale for each choice
>
> Commit the new file and update MEMORY.md with the full proposal. You have full autonomy for this.

After it finishes Phase 1, send:

> Phase 1 approved. Proceed to Phase 2: Vector Memory Layer.

Then validate:

> Proceed with Phase 2 verification:
> 1. Run the indexer to build the initial vector index from MEMORY.md
> 2. Perform test searches:
>    - "What are my current projects?"
>    - "What lessons have I learned?"
>    - "What's blocked right now?"
> 3. Report the top 3 results for each query + indexing stats
>
> Update MEMORY.md with Phase 2 completion summary and example outputs.

### Option B: Do It Yourself

Grab the scripts from our repo:
```bash
cd ~/.openclaw/workspace
git clone https://github.com/Jakebot-ops/agent-memory-guide.git /tmp/mem-guide
cp /tmp/mem-guide/vector_memory/*.py vector_memory/
```

Run the indexer:
```bash
vector_memory/venv/bin/python vector_memory/indexer.py
```

Test it:
```bash
vector_memory/venv/bin/python vector_memory/search.py "your test query"
```

---

## Phase 3: Add the Knowledge Graph

Send this to your bot:

> Phase 2 complete and verified.
>
> 1. Demonstrate the graph:
>    - Load the current memory_graph.json
>    - Show all nodes and edges
>    - Run example queries
>
> 2. Enhance graph extraction:
>    - Update build_from_chunks() to extract "depends_on", "improved_by", "blocks", "enables" from chunk text
>    - Re-run indexer and show improved edge count
>
> 3. Commit all changes and update MEMORY.md with Phase 3 completion summary and graph stats.

If you installed manually, the graph builds automatically when you run the indexer — `graph.py` is called by `indexer.py`.

---

## Phase 4: Make It Mandatory (The Critical Step)

**This is where most people stop — and where the real value begins.**

Without this phase, your bot has a memory system it can *choose to ignore*. And it will.

### Step 1: Add Memory Rules to AGENTS.md

Add this block to your `AGENTS.md` (or equivalent instruction file):

```markdown
### ⚠️ THREE-LAYER MEMORY SYSTEM (ALL MANDATORY)

You have THREE memory layers. ALL must be consulted for ANY memory-related task. No exceptions.

| Layer | Technology | Location | Purpose |
|-------|-----------|----------|---------|
| L1: Markdown | MEMORY.md + daily logs | MEMORY.md, memory/*.md | Human-readable curated knowledge |
| L2: Vector | ChromaDB + all-MiniLM-L6-v2 | vector_memory/chroma_db/ | Semantic search across all memories |
| L3: Graph | NetworkX | vector_memory/memory_graph.json | Relationship traversal between concepts |

Rules:
1. NEVER do memory maintenance without updating ALL THREE layers
2. NEVER answer a memory/history question without querying L2 (vector search) first
3. After editing MEMORY.md, ALWAYS re-index: vector_memory/venv/bin/python vector_memory/indexer.py
4. Re-indexing updates BOTH ChromaDB (L2) AND the graph (L3) automatically
5. If any layer is out of sync, fix it immediately
```

### Step 2: Add the Query Protocol to SOUL.md

```markdown
## Advanced Memory Query Protocol (always active)
Before generating any response or plan:
1. Silently perform a vector search for the current query/context (top 5-7 results)
2. Load the latest knowledge graph
3. Traverse relevant nodes/edges connected to the top vector results
4. Incorporate the most relevant memories, decisions, and relations into your reasoning
5. If high-relevance memories found, briefly reference them in your response

Never say "searching memory" — just use it seamlessly.
```

### Step 3: Add the Sync Watchdog to HEARTBEAT.md

```markdown
## Memory Sync Check
Run `vector_memory/venv/bin/python vector_memory/auto_retrieve.py --status` and if status is OUT_OF_SYNC, re-index with `vector_memory/venv/bin/python vector_memory/indexer.py`.
```

### Step 4: Deploy the Auto-Retrieve Hook

Copy `auto_retrieve.py` from the repo into your `vector_memory/` directory. This script:
- Queries ChromaDB for semantically similar memories
- Traverses the NetworkX graph for related concepts
- Checks sync health between all three layers
- Returns formatted context ready for prompt injection

```bash
# Test it
vector_memory/venv/bin/python vector_memory/auto_retrieve.py "your test query"

# Check sync health
vector_memory/venv/bin/python vector_memory/auto_retrieve.py --status
```

---

## Verify Everything Works

Send this to your bot:

> Re-run indexer to rebuild vector + graph.
>
> You now have long-term memory. Confirm integration and demonstrate on this query: "Summarize our progress and recommend next 3 actions."

Your bot should:
1. ✅ Query ChromaDB and find relevant sections
2. ✅ Traverse the knowledge graph for connected concepts
3. ✅ Reference specific memories in its response
4. ✅ Show sync status as healthy

---

## Troubleshooting

**"No relevant results found"**
- Your distance threshold may be too tight. All-MiniLM-L6-v2 with L2 distance returns 1.0-2.0 for relevant content. The default cutoff in auto_retrieve.py is 2.0.
- Make sure you ran the indexer after your last MEMORY.md edit.

**SIGSEGV / Segfault when importing**
- sentence-transformers loads PyTorch which is memory-hungry. On VMs with <2GB RAM, it can crash.
- Solution: Make sure you're using the venv (`vector_memory/venv/bin/python`), not the system Python.
- If it still crashes, try `all-MiniLM-L6-v2` (smaller) instead of `all-mpnet-base-v2`.

**"Collection does not exist"**
- The collection name in auto_retrieve.py must match the indexer. Default is `memory_chunks`. Check both files.

**Bot still ignores memory**
- Add the explicit checklist to AGENTS.md (Phase 4, Step 1)
- Add the query protocol to SOUL.md (Phase 4, Step 2)
- Both are needed — instructions alone aren't enough, but they help

**Stale search results after editing MEMORY.md**
- The indexer was using `add()` instead of `upsert()`. Make sure your indexer uses `collection.upsert()`. Grab the latest version from the repo.

---

## The Full File Structure

```
~/.openclaw/workspace/
├── MEMORY.md                    # L1: Your curated knowledge
├── AGENTS.md                    # Bot instructions (add memory rules here)
├── SOUL.md                      # Bot personality (add query protocol here)
├── HEARTBEAT.md                 # Periodic checks (add sync watchdog here)
├── memory/
│   ├── YYYY-MM-DD.md           # Daily session logs
│   └── heartbeat-state.json    # Sync tracking
└── vector_memory/
    ├── indexer.py              # Chunks MEMORY.md → ChromaDB + NetworkX
    ├── search.py               # CLI semantic search
    ├── auto_retrieve.py        # Pre-response memory injection
    ├── graph.py                # Knowledge graph builder
    ├── inspect_graph.py        # Graph debugging
    ├── memory_graph.json       # L3: Persisted graph
    ├── chroma_db/              # L2: Vector database (git-ignore this)
    └── venv/                   # Python environment (git-ignore this)
```

---

## Why This Matters

Without persistent memory, your bot:
- Forgets decisions you made yesterday
- Can't search its own knowledge by meaning
- Has no concept of how ideas connect
- Will forget its own memory system exists (yes, really — this happened to us)

With this system:
- Semantic search across everything it's ever learned
- Knowledge graph showing how concepts relate
- Automatic sync monitoring so nothing drifts
- Explicit rules that make memory non-optional

**The key insight:** A memory system the bot can choose to ignore is not a memory system. Make it mandatory. Make it infrastructure. Make it impossible to skip.

---

**Code & full technical writeup:** [github.com/Jakebot-ops/agent-memory-guide](https://github.com/Jakebot-ops/agent-memory-guide)

*Built by Jason Bennett & Jakebot over 5 days of production use — including the day the bot forgot its own database existed.*
