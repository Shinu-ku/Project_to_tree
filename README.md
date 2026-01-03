---

# Project to Tree

A simple Python utility that generates a **tree-style directory diagram** from an existing project folder.

This tool helps document project structures, share folder layouts, and quickly create tree diagrams that can be used in READMEs, documentation, or fed back into tools like ChatGPT.

---

## Features

* Generates a clean tree diagram of a project folder
* Uses standard `tree` symbols (`├──`, `└──`, `│`)
* Skips common junk and hidden folders
* No external dependencies
* Works on Windows, Linux, and macOS

---

## Requirements

* Python 3.x

---

## Usage

Run the script from the **root directory of your project**:

```bash
python project_to_tree.py
```

---

## Output

A file named `PROJECT_TREE.md` will be created in the same directory.

---

## Example Output

```
├── my-project
│   ├── src
│   │   ├── main.py
│   │   └── utils.py
│   ├── tests
│   │   └── test_main.py
│   └── README.md
```

The tree is wrapped in a Markdown code block, making it easy to paste directly into documentation.

---

## How It Works

* The script recursively scans folders starting from the current directory
* Files and folders are sorted alphabetically
* Common folders like `.git` and `__pycache__` are ignored
* Permission-restricted folders are skipped safely

---

## Customization

You can exclude additional folders by editing:

```python
EXCLUDED_FOLDERS = {
    '.git',
    '__pycache__',
    'node_modules'
}
```

---

## Real-World Use Cases

### 1. Document project structure

Generate a tree diagram and include it in your README or docs to clearly show project layout.

### 2. Share structure with ChatGPT or teammates

Paste the generated tree into ChatGPT to ask for architecture reviews or improvements.

### 3. Recreate the project later

Use the generated tree as input for directory-creation tools.

### 4. Teaching and learning

Helpful for explaining folder structures in tutorials or assignments.

---

## Limitations

* The tool only generates structure, not file contents
* Output reflects the current state of the directory
* Deep or very large folders may produce long trees

---

## License

MIT License (optional)

---

## Author

Created by **Soumya Kushwah**
A lightweight utility for visualizing project structures.

---
