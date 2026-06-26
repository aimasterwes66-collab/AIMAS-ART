#!/usr/bin/env python3
"""
AIMAS Corpus Importer
Script to import AIMAS corpus modifiers into the DB-air framework
"""

import json
import os
from datetime import datetime

def import_aimas_corpus():
    """Import AIMAS corpus into DB-air framework"""
    
    # Paths
    aimas_corpus_path = os.path.expanduser("~/AIMAS-ART/aimas_corpus.json")
    db_air_path = os.path.expanduser("~/AIMAS/DB-air")
    
    print("Importing AIMAS corpus into DB-air framework...")
    
    # Load AIMAS corpus
    with open(aimas_corpus_path, 'r') as f:
        aimas_data = json.load(f)
    
    print(f"Loaded AIMAS corpus: {aimas_data['_meta']['name']} v{aimas_data['_meta']['version']}")
    print(f"Total categories: {len(aimas_data['categories'])}")
    
    # Create modifiers directory if it doesn't exist
    modifiers_dir = os.path.join(db_air_path, "modifiers")
    os.makedirs(modifiers_dir, exist_ok=True)
    
    # Create a comprehensive taxonomy from AIMAS corpus
    taxonomy = {
        "modifier_taxonomy": {
            "visual_characteristics": {},
            "conceptual_framework": {},
            "technical_attributes": {},
            "stylistic_elements": {},
            "contextual_descriptors": {}
        }
    }
    
    # Process each category
    for cat_key, category in aimas_data['categories'].items():
        print(f"Processing category {cat_key}: {category['name']}")
        
        # Add to conceptual framework
        taxonomy["modifier_taxonomy"]["conceptual_framework"][category['name']] = {
            "description": category.get('description', ''),
            "entries": [],
            "weight_range": category.get('weight_range', [0.1, 1.0])
        }
        
        # Add entries
        for entry in category['entries']:
            taxonomy["modifier_taxonomy"]["conceptual_framework"][category['name']]["entries"].append({
                "name": entry['name'],
                "tags": entry.get('tags', []),
                "weight_suggest": entry.get('weight_suggest', 1.0),
                "slots": entry.get('slots', [])
            })
    
    # Save the taxonomy
    taxonomy_path = os.path.join(modifiers_dir, "aimas_corpus_taxonomy.json")
    with open(taxonomy_path, 'w') as f:
        json.dump(taxonomy, f, indent=2)
    
    print(f"Saved taxonomy to {taxonomy_path}")
    
    # Also save as CSV for easy viewing
    csv_path = os.path.join(modifiers_dir, "aimas_corpus_modifiers.csv")
    with open(csv_path, 'w') as f:
        f.write("category,category_name,entry_name,tags,weight_suggest,slots\n")
        for cat_key, category in aimas_data['categories'].items():
            for entry in category['entries']:
                tags = "|".join(entry.get('tags', []))
                slots = "|".join(entry.get('slots', []))
                f.write(f"{cat_key},{category['name']},{entry['name']},{tags},{entry.get('weight_suggest', 1.0)},{slots}\n")
    
    print(f"Saved CSV to {csv_path}")
    
    # Update the existing taxonomy template
    taxonomy_template_path = os.path.join(modifiers_dir, "taxonomy_template.json")
    if os.path.exists(taxonomy_template_path):
        with open(taxonomy_template_path, 'r') as f:
            existing_taxonomy = json.load(f)
        
        # Merge AIMAS corpus into existing taxonomy
        for section in taxonomy["modifier_taxonomy"]:
            if section not in existing_taxonomy["modifier_taxonomy"]:
                existing_taxonomy["modifier_taxonomy"][section] = {}
            
            # Add conceptual framework from AIMAS
            for key, value in taxonomy["modifier_taxonomy"]["conceptual_framework"].items():
                existing_taxonomy["modifier_taxonomy"]["conceptual_framework"][key] = value
        
        # Save updated taxonomy
        with open(taxonomy_template_path, 'w') as f:
            json.dump(existing_taxonomy, f, indent=2)
        
        print(f"Updated existing taxonomy template at {taxonomy_template_path}")
    
    # Create a summary report
    summary = {
        "import_date": datetime.now().isoformat(),
        "source": "AIMAS Corpus",
        "categories_imported": len(aimas_data['categories']),
        "entries_imported": sum(len(cat['entries']) for cat in aimas_data['categories'].values()),
        "categories": list(aimas_data['categories'].keys())
    }
    
    summary_path = os.path.join(db_air_path, "inventory", "aimas_corpus_import_summary.json")
    os.makedirs(os.path.dirname(summary_path), exist_ok=True)
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"Import summary saved to {summary_path}")
    print("Import completed successfully!")

if __name__ == "__main__":
    import_aimas_corpus()