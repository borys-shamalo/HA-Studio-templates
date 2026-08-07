import os
import yaml
import json
import glob

def build():
    templates = []
    # Find all yaml files in the templates directory
    files = glob.glob("templates/*.yaml")
    
    # Sort files to ensure deterministic output
    files.sort()
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                template_data = yaml.safe_load(f)
                if template_data:
                    templates.append(template_data)
            except yaml.YAMLError as e:
                print(f"Error parsing {filepath}: {e}")
                exit(1)
                
    # Dump all templates to templates.json
    with open("templates.json", 'w', encoding='utf-8') as f:
        json.dump(templates, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully compiled {len(templates)} templates into templates.json")

if __name__ == "__main__":
    build()
