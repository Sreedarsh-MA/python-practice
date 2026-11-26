# Deployment & Execution Guide

This guide provides step-by-step instructions on how to set up and run the **Python Learning Hub** project.

## 1. Prerequisites
Make sure you have **Python 3.6 or higher** installed on your system.
- To check your version, run: `python --version`

## 2. Project Setup
### Step A: Access the Project Folder
Open your terminal or command prompt and navigate to the project directory:
```powershell
cd python_learning_hub
```

### Step B: Set Up a Virtual Environment (Recommended)
Using a virtual environment keeps your project dependencies isolated from other Python projects.

1. **Create the environment**:
   ```powershell
   python -m venv venv
   ```
2. **Activate the environment**:
   - **Windows**: `.\venv\Scripts\activate`
   - **macOS/Linux**: `source venv/bin/activate`

### Step C: Install Dependencies
Although this project currently uses standard Python libraries, it is good practice to run:
```powershell
pip install -r requirements.txt
```

## 3. Running the Application
Once the environment is ready, launch the application using the main entry point:
```powershell
python main.py
```

## 4. Application Usage
1. Once the app starts, you will see a menu.
2. Type `1`, `2`, or `3` to launch a specific tool.
3. Type `4` to exit the application.

## 5. Troubleshooting
- **'python' is not recognized**: Ensure Python is added to your system's PATH during installation.
- **ModuleNotFoundError**: Ensure you are running the command from the `python_learning_hub` root directory.
