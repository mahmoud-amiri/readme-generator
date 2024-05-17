import yaml
import os

def extract_doc_comments(file_path):
    doc_comments = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            inside_doc = False
            for line in lines:
                if '//doc init' in line or '--doc init' in line:
                    inside_doc = True
                elif '//doc end' in line or '--doc end' in line:
                    inside_doc = False
                elif inside_doc:
                    cleaned_line = line.strip()
                    if cleaned_line.startswith('//'):
                        cleaned_line = cleaned_line[2:].strip()
                    elif cleaned_line.startswith('--'):
                        cleaned_line = cleaned_line[2:].strip()
                    doc_comments.append(cleaned_line)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return "\n".join(doc_comments)

def process_module(module, level=1):
    readme_lines = []
    header_prefix = "#" * level
    readme_lines.append(f"{header_prefix} {module['module_name']}\n")
    for file in module['files']:
        file_path = file['path']
        comments = extract_doc_comments(file_path)
        if comments:
            readme_lines.append(comments + "\n")
    if 'submodules' in module:
        for submodule in module['submodules']:
            readme_lines.extend(process_module(submodule, level + 1))
    return readme_lines

def generate_readme(yaml_file):
    with open(yaml_file, 'r') as file:
        project = yaml.safe_load(file)
    
    readme_lines = [
        f"# {project['project']['name']}\n",
        f"{project['project']['description']}\n"
    ]
    
    for module in project['project']['hierarchy']:
        readme_lines.extend(process_module(module))
    
    with open("README.md", 'w') as readme_file:
        readme_file.write("\n".join(readme_lines))

# Example usage
generate_readme("project_structure.yaml")
