import os
import re
import chromadb
from sentence_transformers import SentenceTransformer
from graph import MemoryGraph # Import the new graph module

MEMORY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../MEMORY.md")
VECTOR_DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chroma_db")
COLLECTION_NAME = "memory_chunks"

def parse_markdown(file_path):
    """
    Parses MEMORY.md into chunks based on headers (##).
    Returns a list of dicts: {'content': text, 'metadata': {'source': 'MEMORY.md', 'section': header}}
    """
    if not os.path.exists(file_path):
        return []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    chunks = []
    # Split by headers (## Header)
    # The regex captures the header text and the following content
    sections = re.split(r'(^##\s+.*$)', content, flags=re.MULTILINE)
    
    # First part is usually empty or title
    current_header = "Intro"
    current_content = sections[0].strip()
    if current_content:
        chunks.append({
            'content': current_content,
            'metadata': {'source': 'MEMORY.md', 'section': current_header}
        })

    # Iterate through split parts (header, content, header, content...)
    for i in range(1, len(sections), 2):
        header = sections[i].strip().replace('#', '').strip()
        content = sections[i+1].strip()
        if content:
            chunks.append({
                'content': content,
                'metadata': {'source': 'MEMORY.md', 'section': header}
            })
            
    return chunks

def index_memory():
    print("🧠 Loading Sentence Transformer...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    print("📂 Connecting to ChromaDB...")
    client = chromadb.PersistentClient(path=VECTOR_DB_PATH)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)
    
    print("📄 Parsing MEMORY.md...")
    chunks = parse_markdown(MEMORY_FILE)
    
    if not chunks:
        print("⚠️ No content found in MEMORY.md")
        return

    # --- GRAPH UPDATE ---
    print("🕸️  Updating Knowledge Graph...")
    graph = MemoryGraph()
    graph.build_from_chunks(chunks)
    # --------------------

    ids = [f"mem_{i}" for i in range(len(chunks))]
    documents = [c['content'] for c in chunks]
    metadatas = [c['metadata'] for c in chunks]
    
    print(f"🔢 Generating embeddings for {len(chunks)} chunks...")
    embeddings = model.encode(documents).tolist()
    
    print("💾 Storing in Vector DB (upsert)...")
    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )
    # Clean up orphaned entries if chunk count decreased
    existing = collection.count()
    if existing > len(chunks):
        orphan_ids = [f"mem_{i}" for i in range(len(chunks), existing)]
        if orphan_ids:
            collection.delete(ids=orphan_ids)
            print(f"🧹 Cleaned {len(orphan_ids)} orphaned entries.")
    print("✅ Indexing Complete!")

if __name__ == "__main__":
    index_memory()
