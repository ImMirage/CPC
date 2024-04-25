# Command Prompt Closer (CPC)

Command Prompt Closer, affectionately known as CPC, is a lightweight Python script designed to swiftly close all active Command Prompt windows on your system. Say goodbye to cluttered screens and streamline your workflow with CPC.

## Features

- **Efficiency:** CPC quickly terminates Command Prompt processes, saving you time and effort.
- **User-Friendly Interface:** With a simple execution, CPC provides a hassle-free solution for managing your system resources.
- **Countdown Timer:** CPC features a built-in countdown timer to inform you of the imminent closure, ensuring a smooth experience.
- **Convenience:** Whether you're tidying up your workspace or need a clean slate for your next task, CPC is your go-to solution for swift and effective Command Prompt management.

## Installation

To get started with Command Prompt Closer (CPC), you can clone the repository to your local machine using Git. Follow these steps:

1. Open a terminal or command prompt on your computer.

2. Navigate to the directory where you want to clone the repository. You can use the `cd` command to change directories. For example:
cd path/to/desired/directory


3. Once you're in the desired directory, use the `git clone` command followed by the repository URL:
git clone https://github.com/ImMirage/CPC.git


4. After running the command, the repository will be cloned to your local machine.

5. You can now navigate to the cloned repository directory and start using CPC.

## Compilation (Recommended)

For seamless access and enhanced convenience, we recommend compiling Command Prompt Closer (CPC) using the Python module named pyinstaller. Follow these steps to compile CPC into a standalone executable:

1. Install pyinstaller if you haven't already. You can do this using pip, the Python package installer, by running the following command:
pip install pyinstaller

2. Once pyinstaller is installed, navigate to the directory where CPC is located using the terminal or command prompt.
3. Run the following command to compile CPC into a single executable file:
pyinstaller --onefile cpc.py

4. After the compilation process is complete, navigate to the `dist` directory within the CPC repository.
5. Locate the compiled executable file (it should be named `cpc.exe` if you're on Windows).
6. Move the executable file to a directory of your choice, preferably one within your user directory for easy access.
7. You can now pin the compiled CPC executable to your taskbar for quick and effortless usage.

With CPC compiled into a standalone executable, you can enjoy even greater accessibility and efficiency in managing your Command Prompt windows.

## Compatibility

CPC is compatible with Windows operating systems.

## Contributing

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests to help improve CPC.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
