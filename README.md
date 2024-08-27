# BlueTea
A Sleep-Prevention Program


---

### Project Requirements for a Python-Based Cross-Platform Sleep-Prevention Program

**Project Name:** Python Sleep-Prevention Program (Caffeine Clone)

**Objective:**  
To develop a lightweight, cross-platform application using Python that prevents the system from going to sleep or activating the screensaver, providing users with a reliable tool to keep their computers awake during long-running tasks, presentations, or other uninterrupted activities.

### 1. **Functional Requirements**

#### 1.1 Core Features
- **Prevent System Sleep:**
  - The application must prevent the system from entering sleep mode due to inactivity.
- **Prevent Display Sleep:**
  - The application must prevent the display from dimming or turning off due to inactivity.
- **User-Controlled Activation:**
  - Users must be able to easily activate or deactivate the sleep-prevention mode.
- **Timer Functionality:**
  - Users should be able to set a timer to automatically deactivate the sleep-prevention mode after a specified period.
- **Status Indicator:**
  - Display an on-screen indicator or icon in the system tray/menu bar showing the current status (active or inactive).

#### 1.2 Platform-Specific Features
- **Windows:**
  - Use Python's `ctypes` library to call the Windows API (`SetThreadExecutionState`) to manage sleep-prevention.
- **macOS:**
  - Use Python's `subprocess` module to execute macOS system commands (`caffeinate`) to prevent sleep.
- **Linux:**
  - Use Python's `subprocess` module to execute Linux system commands (`xset` or `systemd-inhibit`) to manage sleep-prevention.

### 2. **Non-Functional Requirements**

#### 2.1 Performance
- The application should consume minimal system resources, ensuring it does not interfere with other tasks or significantly impact system performance.

#### 2.2 Usability
- The application should have a simple, intuitive user interface that is easy to understand and operate, regardless of the user’s technical skill level.

#### 2.3 Compatibility
- **Operating Systems:** 
  - Windows 7 and later versions.
  - macOS 10.12 (Sierra) and later versions.
  - Major Linux distributions (e.g., Ubuntu, Fedora, Debian).
- **Python Versions:**
  - Support Python 3.6 and above.
- **Hardware:** 
  - The application should work on both x86_64 and ARM architectures where applicable.

#### 2.4 Security
- The application must not request unnecessary permissions and should operate with the least privileges required.
- Ensure secure coding practices to prevent potential vulnerabilities, such as injection attacks or privilege escalation.

### 3. **Technical Requirements**

#### 3.1 Development Environment
- **Language:** Python
- **Libraries and Frameworks:**
  - **PyQt5 or Tkinter:** For building the cross-platform graphical user interface (GUI).
  - **ctypes:** For interacting with system-level APIs on Windows.
  - **subprocess:** For executing system commands on macOS and Linux.
- **Package Management:** Use `pip` for managing Python dependencies.

#### 3.2 Deployment
- **Packaging:** Create platform-specific executables for distribution:
  - **Windows:** Use `PyInstaller` to create an EXE installer.
  - **macOS:** Use `PyInstaller` to create a standalone application bundle (.app).
  - **Linux:** Use `PyInstaller` to create executable binaries and packages (DEB and RPM).
- **Updates:** Implement an update mechanism to ensure users can easily update to the latest version.

### 4. **User Interface Requirements**

#### 4.1 Main Interface
- A simple, single-window interface with:
  - **Activate/Deactivate Button:** Toggle sleep-prevention mode.
  - **Timer Settings:** Set a timer to deactivate the mode.
  - **Status Display:** Show the current status (active or inactive).

#### 4.2 System Tray/Menu Bar Icon
- A small icon that sits in the system tray (Windows/Linux) or menu bar (macOS) to provide quick access.
- Right-click or click to display a menu with options to activate/deactivate, set a timer, and open the main interface.

### 5. **Testing Requirements**

#### 5.1 Testing Types
- **Unit Testing:** Test core functionalities to ensure accurate operation.
- **Integration Testing:** Verify integration between different modules and platform-specific APIs.
- **Usability Testing:** Ensure the application is user-friendly and meets the usability requirements.
- **Compatibility Testing:** Test on different OS versions and hardware configurations to ensure broad compatibility.

#### 5.2 Testing Platforms
- Test on various versions of Windows (7, 8, 10, 11), macOS (10.12+), and Linux distributions (Ubuntu, Fedora, Debian).

### 6. **Documentation Requirements**

#### 6.1 User Documentation
- Provide a user guide detailing installation, usage, and troubleshooting steps.
- Include a FAQ section for common issues and questions.

#### 6.2 Developer Documentation
- Detailed code documentation with comments explaining core functionalities and platform-specific implementations.
- Setup guide for development environments and build instructions for all supported platforms.

### 7. **Maintenance and Support**

- Plan for regular updates to support new OS versions and fix any bugs.
- Provide a mechanism for users to report issues or request features.

### 8. **Licensing and Distribution**

- Choose an appropriate open-source license (e.g., MIT, GPL) or commercial license depending on the project goals.
- Distribute through official websites, app stores, or package managers (Homebrew for macOS, Chocolatey for Windows, and APT/YUM for Linux).

### 9. **Project Timeline and Milestones**

- **Week 1-2:** Initial project setup, requirements gathering, and design phase.
- **Week 3-5:** Development of core functionality for Windows.
- **Week 6-8:** Development of core functionality for macOS.
- **Week 9-11:** Development of core functionality for Linux.
- **Week 12-13:** Integration of the GUI and platform-specific modules using PyQt5 or Tkinter.
- **Week 14-16:** Testing phase (unit, integration, and usability testing).
- **Week 17-18:** Bug fixing, optimization, and documentation.
- **Week 19:** Final review, packaging, and release preparation.
- **Week 20:** Launch and initial user support phase.

---

This revised specification focuses on using Python for development, leveraging its capabilities and libraries to create a robust, cross-platform sleep-prevention application. The use of PyQt5 or Tkinter allows for a consistent and native-looking GUI across all supported platforms, and `ctypes` and `subprocess` handle the platform-specific sleep prevention logic.
