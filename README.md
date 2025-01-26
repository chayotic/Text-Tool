# Text Tool Program  

A command-line tool for managing text files efficiently. With this program, you can create, edit, clear, and delete text files, all through an intuitive menu-driven interface.  

---

## Features  

### File Management  
- **View Files**: Display all `.txt` files in the current directory.  
- **Create New File**: Generate a new text file with a custom name.  
- **Delete File**: Permanently delete a selected file (with confirmation).  

### File Editing  
- **Read File**: View the content of a selected file.  
- **Replace Words**: Find and replace specific words in a file (case-sensitive).  
- **Append Text**: Add new content to the end of a file.  
- **Clear File**: Erase all content from a file (with confirmation).  

### Interactive & User-Friendly  
- Intuitive menu navigation.  
- Clear prompts and error messages for invalid inputs.  
- Color-coded output for better readability (using `termcolor`).  

---

## Getting Started  

### Prerequisites  
- Python 3.6 or later  
- Install the required package:  
  ```bash
  pip install termcolor
