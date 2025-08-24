# Simple G-code Generator for 2-Axis CNC Machines

This is a lightweight desktop application designed to generate G-code tailored for use with **2-axis CNC machines**. It’s ideal for quick toolpath generation and can be freely customized to suit your design and workflow needs.

## ✨ Features

- ✅ Generate basic G-code for 2-axis CNC operations
- 🖥️ Simple and customizable desktop interface
- ⚙️ Output G-code structure can be adjusted to match your specific machine setup
- 🆓 Free to download, modify, and redistribute

## 🔧 Customization

You can:
- Modify the **user interface** to better fit your workflow
- Adjust the **G-code output** format to suit different machine requirements
- Add or remove features depending on your use case

## 📦 Packaging as Windows App

To create a standalone `.exe` file for running the application on Windows, use [`PyInstaller`](https://pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller --onefile -w main.py


This will generate a Windows executable in the dist/ folder.


💻 Requirements
Python 3.7+

Required libraries (if any): Tkinter.

🚀 Getting Started
Clone or download this repository

Run the script with Python:

python main.py

Or generate a .exe as described above to run it standalone

📄 License

Free to use and modify. No license restrictions unless specified.

📬 Contact

If you have questions or want to contribute improvements, feel free to open an issue or a pull request!
