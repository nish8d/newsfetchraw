API_KEYS = {
    "newsdata": "pub_3b747791334743199b282538d6ce7a83",
    "newsapi": "ae4083beabfc4fb48bacee5c03f7cf4a",
    "gnews": "ab52db50b1d8a4a8e2b6f231e4368e5b"
}

EMBED_MODEL_NAME = "all-mpnet-base-v2"
EMBED_CACHE_DB = "embedding_cache.sqlite"

# Cache settings
EMBED_CACHE_MAX_ITEMS = 50_000  # LRU eviction

# Deduplication clustering
DBSCAN_EPS = 0.20     # 1 - cosine similarity threshold (~0.8)
DBSCAN_MIN_SAMPLES = 1
