# Installation and setup

Python is one of the most popular programming languages in the world. It's simple, versatile, and widely used in fields like web development, data science, automation, machine learning, and more. But before you can start writing code, you need to install and set up Python properly on your computer.

This guide walks you step-by-step through installing Python on Windows, macOS, and Linux, along with setting up your environment for development.

## 1. Check if Python is Already Installed

Most systems, especially Linux and macOS, come with Python pre-installed. To check:

- Open **Command Prompt (Windows)** or **Terminal (macOS/Linux)**.
- Type:

```bash
python --version
```

or

```bash
python3 --version
```

If you see a version number (e.g., `Python 3.11.6`), Python is already installed.
If you get an error like _command not found_, you need to install it.

## 2. Installing Python on Windows

### Step 1: Download Python

1. Go to the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Click **Download Python 3.x.x** (the latest stable version).

### Step 2: Run the Installer

1. Double-click the downloaded file (`python-3.x.x.exe`).
2. On the setup screen:

   - Check **Add Python to PATH** (important).
   - Select **Install Now**.

### Step 3: Verify Installation

Open **Command Prompt** and type:

```bash
python --version
```

or

```bash
py --version
```

If you see a version number, Python is installed correctly.

## 3. Installing Python on macOS

### Option 1: Install via Official Installer

1. Download the macOS installer from [python.org/downloads](https://www.python.org/downloads/).
2. Open the `.pkg` file and follow the on-screen instructions.

### Option 2: Install via Homebrew (recommended)

If you use **Homebrew** (a popular macOS package manager):

```bash
brew install python
```

Verify installation:

```bash
python3 --version
```

## 4. Installing Python on Linux

Most Linux distros have Python pre-installed. To install or upgrade:

### For Debian/Ubuntu:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

### For Fedora:

```bash
sudo dnf install python3
```

### For Arch Linux:

```bash
sudo pacman -S python
```

Check version:

```bash
python3 --version
```

## 5. Installing pip (Python Package Manager)

`pip` is Python's package manager, used to install libraries. It often comes pre-installed with Python 3.

Check if `pip` is installed:

```bash
pip --version
```

or

```bash
pip3 --version
```

If not installed:

- **Windows/macOS/Linux**:
  Download and run:

  ```bash
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python get-pip.py
  ```

## 6. Setting Up a Virtual Environment

A **virtual environment** allows you to create isolated spaces for your projects, so libraries don't conflict.

### Step 1: Install `venv` (if not available)

```bash
pip install virtualenv
```

### Step 2: Create a Virtual Environment

```bash
python -m venv myenv
```

### Step 3: Activate the Environment

- **Windows (Command Prompt):**

  ```bash
  myenv\Scripts\activate
  ```

- **macOS/Linux:**

  ```bash
  source myenv/bin/activate
  ```

To deactivate:

```bash
deactivate
```

## 7. Installing an IDE or Code Editor

While you can write Python code in any text editor, using a proper IDE makes development easier. Popular choices:

- **VS Code** (lightweight, extensions for Python, free)
- **PyCharm** (powerful IDE, free Community Edition)
- **Jupyter Notebook** (great for data science & experimentation)

Example: To install Jupyter Notebook:

```bash
pip install notebook
jupyter notebook
```

## 8. Your First Python Program

Once Python is installed, let's test it.

1. Open a text editor and create a file: `hello.py`
2. Add the following code:

```python
print("Hello, World!")
```

3. Run it from terminal:

```bash
python hello.py
```

If you see **Hello, World!**, your setup is complete. 🎉

## 9. Troubleshooting Common Issues

- **`python` not recognized** → Add Python to PATH during installation or manually update environment variables.
- **Multiple versions (python vs python3)** → Use `python3` explicitly if both Python 2 and 3 exist.
- **Permission issues (Linux/macOS)** → Use `sudo` or a virtual environment.

## 10. Next Steps

Now that Python is installed, you can:

- Learn **Python basics** (variables, loops, functions).
- Explore **pip libraries** like NumPy, Pandas, Flask, Django.
- Start a **real project** (web app, automation script, data analysis).

You now have Python installed and ready for development. With the right environment set up, you can dive straight into coding and building projects.
