"""Build corpus maps from corrected JSONs"""
import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

import build_corpus_maps

# Redirect to corrected JSON
build_corpus_maps.JSON_DIR = PROJECT_ROOT / "research_kb" / "papers" / "json_corrected"

# Build
corpus = build_corpus_maps.build_all()
print("Corpus maps generated from corrected papers")
