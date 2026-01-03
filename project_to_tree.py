import os

EXCLUDED_FOLDERS = {
    '.git',
    '__pycache__',
    'node_modules',
    '...examples_folders_that_u_wanna_remove_from_tree'
}

def generate_tree(start_path='.', prefix=''):
    tree = ''
    try:
        files = sorted(os.listdir(start_path))
    except PermissionError:
        return ''

    for i, filename in enumerate(files):
        if filename in EXCLUDED_FOLDERS:
            continue

        filepath = os.path.join(start_path, filename)
        connector = '└── ' if i == len(files) - 1 else '├── '
        tree += f"{prefix}{connector}{filename}\n"

        if os.path.isdir(filepath) and not filename.startswith('.'):
            extension = '    ' if i == len(files) - 1 else '│   '
            tree += generate_tree(filepath, prefix + extension)

    return tree


if __name__ == '__main__':
    project_root = '.'
    output_file = 'PROJECT_TREE.md'

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Project Structure\n\n```\n")
        f.write(generate_tree(project_root))
        f.write("```\n")

    print(f"✅ Folder tree saved to {output_file}")
