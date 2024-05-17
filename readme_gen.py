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

def process_module(module, level=1, toc_lines=None):
    if toc_lines is None:
        toc_lines = []

    readme_lines = []
    header_prefix = "#" * level
    module_header = f"{header_prefix} {module['module_name']}\n"
    readme_lines.append(module_header)
    toc_lines.append(f"{'  ' * (level - 1)}- [{module['module_name']}](#{module['module_name'].lower().replace(' ', '-')})")
    
    for file in module['files']:
        file_path = file['path']
        comments = extract_doc_comments(file_path)
        if comments:
            readme_lines.append(comments + "\n")
    
    readme_lines.append("**[Back to Top](#table-of-contents)**\n")
    
    if 'submodules' in module:
        for submodule in module['submodules']:
            submodule_lines, toc_lines = process_module(submodule, level + 1, toc_lines)
            readme_lines.extend(submodule_lines)
    
    return readme_lines, toc_lines

def generate_readme(yaml_file):
    with open(yaml_file, 'r') as file:
        project = yaml.safe_load(file)
    
    readme_lines = [
        f"# {project['project']['name']}\n",
        f"{project['project']['description']}\n",
        "# Table of Contents\n"
    ]
    
    toc_lines = []
    for module in project['project']['hierarchy']:
        module_lines, toc_lines = process_module(module, toc_lines=toc_lines)
        readme_lines.extend(module_lines)
    
    readme_lines.insert(3, "\n".join(toc_lines) + "\n")
    
    with open("README.md", 'w') as readme_file:
        readme_file.write("\n".join(readme_lines))

# Example usage
generate_readme("project_structure.yaml")
