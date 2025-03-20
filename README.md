# Password Manager

A simple and secure password manager built with Python and Tkinter. This application allows users to generate, store, and retrieve passwords easily. Passwords are encrypted using the cryptography library and saved locally in a JSON file, ensuring security while keeping access convenient.

## Requirements

| Dependency | Version | Link |
|------------|---------|------|
| Python | 3.12.7 | [Download](https://www.python.org/downloads/release/python-3127/) |
| cryptography | 44.0.2 | [PyPI](https://pypi.org/project/cryptography/) |

## Installation

1. **Clone the repository:**
```
git clone https://github.com/fullstacksam23/Password-Manager.git
```
2. Navigate to the project directory:
```
cd password-manager
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Generate a key
```
Run gen.py to generate a key which will be saved in the pass_key.key file 🔒
Keep this key safe! It is required for encrypting and decrypting passwords.
```

## Usage

1. Run the `main.py` file:
```
python main.py
```
2. The application window will appear, allowing you to:
   - Generate a random password
   - Save a new password for a website
   - Search for a saved password

## API

The application uses the following APIs:

- `tkinter`: for the graphical user interface
- `random`: for generating random passwords
- `json`: for storing and retrieving password data
- `cryptography`: for encrypting and decrypting passwords

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them
4. Push your changes to your forked repository
5. Submit a pull request
