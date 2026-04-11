import os
import pathspec

def create_context_prompt(root_dir='.'):
    # Load .gitignore patterns if they exist
    gitignore_path = os.path.join(root_dir, '.gitignore')
    patterns = []
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            patterns = f.read().splitlines()
    
    # Always exclude the .git directory
    patterns.append('.git/')
    patterns.append('*.csv')
    spec = pathspec.PathSpec.from_lines('gitwildmatch', patterns)

    output = []
    
    # Generate Directory Tree
    output.append("## Project Structure")
    output.append("```text")
    for root, dirs, files in os.walk(root_dir):
        # Filter directories and files based on gitignore
        rel_path = os.path.relpath(root, root_dir)
        if rel_path == '.':
            rel_path = ''
        
        # Modify dirs in-place to prevent os.walk from descending into ignored folders
        dirs[:] = [d for d in dirs if not spec.match_file(os.path.join(rel_path, d))]
        
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        output.append(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        
        for f in files:
            if not spec.match_file(os.path.join(rel_path, f)):
                output.append(f"{sub_indent}{f}")
    output.append("```\n")

    # Generate File Contents
    output.append("## File Contents")
    for root, dirs, files in os.walk(root_dir):
        rel_path = os.path.relpath(root, root_dir)
        if rel_path == '.':
            rel_path = ''
            
        dirs[:] = [d for d in dirs if not spec.match_file(os.path.join(rel_path, d))]
        
        for f in files:
            full_path = os.path.join(root, f)
            display_path = os.path.join(rel_path, f)
            
            if not spec.match_file(display_path):
                try:
                    with open(full_path, 'r', encoding='utf-8') as file_content:
                        content = file_content.read()
                        output.append(f"### File: {display_path}")
                        output.append("```")
                        output.append(content)
                        output.append("```\n")
                except (UnicodeDecodeError, PermissionError):
                    # Skip binary files or restricted files
                    continue

    return "\n".join(output)

if __name__ == "__main__":
    context = create_context_prompt()
    print(context)