### Step-by-Step Python Code

**Prerequisites:**
- Install Python 3.6 or above.
- Install the required Python libraries using `pip`:
  ```bash
  pip install PyQt5
  ```

**Code Implementation:**
    - Check SleepPrevention.py 
 
### Explanation of the Code:

1. **Importing Libraries:**
   - **`sys`**: Used for accessing system-specific parameters and functions.
   - **`ctypes`**: A foreign function library for Python to call Windows API functions.
   - **`subprocess`**: Used to spawn new processes, connect to their input/output/error pipes, and obtain their return codes, especially for macOS and Linux commands.
   - **`PyQt5.QtWidgets`**, **`PyQt5.QtGui`**, and **`PyQt5.QtCore`**: These are the primary libraries used for creating the GUI.

2. **Class `SleepPreventionApp`**:
   - Inherits from `QWidget` to create a window.
   - Initializes the user interface (UI) and sets up a system tray icon.

3. **`initUI` Method**:
   - Sets up the main window, including buttons and labels.
   - Creates a system tray icon with a context menu for easy access to start/stop the sleep prevention and quit the application.

4. **`toggle_sleep_prevention` Method**:
   - This method toggles the sleep prevention state. It changes the text on the button and the status label and calls the appropriate method (`prevent_sleep` or `allow_sleep`) based on the current state.

5. **`prevent_sleep` Method**:
   - Contains platform-specific code to prevent the system from sleeping:
     - **Windows**: Uses `ctypes` to call `SetThreadExecutionState`.
     - **macOS**: Uses `subprocess` to execute the `caffeinate` command.
     - **Linux**: Uses `subprocess` to execute `xset` commands to manage display power settings.

6. **`allow_sleep` Method**:
   - Restores the system's default sleep behavior:
     - **Windows**: Calls `SetThreadExecutionState` to reset sleep settings.
     - **macOS and Linux**: Terminates the process created by `caffeinate` or `xset`.

7. **`quit_app` Method**:
   - Ensures that sleep settings are restored to default before exiting the application.

8. **Main Block**:
   - Initializes the PyQt application and runs the event loop.

### Running the Program

1. **Python Environment**: Ensure Python 3.x is installed and `PyQt5` is installed using `pip install PyQt5`.
2. **Execution**: Save the script to a file named `sleep_prevention.py` and run it using:
   ```bash
   python sleep_prevention.py
   ```
3. **Tray Icon**: A tray icon will appear that allows quick access to start/stop the sleep prevention and quit the application.

### Notes:

- **Windows**: The program uses the Windows API via `ctypes` to prevent sleep.
- **macOS**: Uses the `caffeinate` command to prevent sleep.
- **Linux**: Uses `xset` to manage display power settings. You may need to adjust this for specific Linux distributions or environments (like GNOME, KDE, etc.).
- **Icon**: You need to have an `icon.png` file for the system tray icon. You can use any icon file you prefer.

This program provides a cross-platform solution for preventing sleep using Python, with a simple and intuitive user interface.
