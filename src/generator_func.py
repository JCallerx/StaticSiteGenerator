from md_to_html import *
import os
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        from_content = f.read()
    
    with open(template_path, "r") as f:
        template_content = f.read()

    result = markdown_to_html_node(from_content).to_html()
    title = extract_title(from_content)
    new_file = template_content.replace("{{ Title }}", title)
    new_file = new_file.replace("{{ Content }}", result)
    destination = os.path.dirname(dest_path)
    os.makedirs(destination, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(new_file)
