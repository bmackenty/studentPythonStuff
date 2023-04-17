# this file is used to check if the extensions are installed
# and if applications are in the right place
# and if students have the right applications installed

import os
import subprocess
import glob
import re

os.system("clear")


GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

def intro():
    print("="*74)
    print("Checking for installed applications and extensions")
    print(f"If you see any {RED}red{RESET} text, you need to install the application or extension")
    print(f"If you see any {GREEN}green{RESET} text, you should be okay")
    print("="*74)
    print()


def is_homebrew_installed():
    try:
        subprocess.run(["brew", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except:
        return False

def get_python_versions(bin_folders):
    python_versions = set()

    for bin_folder in bin_folders:
        python_executables = glob.glob(os.path.join(bin_folder, "python*"))
        
        for executable in python_executables:
            match = re.match(r"python(\d+\.\d+)$", os.path.basename(executable))
            
            if match:
                version = match.group(1)
                python_versions.add(version)

    return sorted(python_versions, key=lambda x: tuple(map(int, x.split('.'))))

def get_version_executable(version, bin_folders):
    for bin_folder in bin_folders:
        executable = os.path.join(bin_folder, f"python{version}")
        
        if os.path.exists(executable) and os.access(executable, os.X_OK):
            return executable

    return None

def is_vscode_installed():
    applications_folder = "/Applications"
    vscode_app_name = "Visual Studio Code.app"
    
    for item in os.listdir(applications_folder):
        if item == vscode_app_name:
            return True
    return False

def are_vscode_extensions_installed(extension_ids):
    vscode_extensions_path = os.path.expanduser("~/.vscode/extensions")
    
    if not os.path.exists(vscode_extensions_path):
        return {}

    installed_extensions = set(os.listdir(vscode_extensions_path))
    extension_status = {}
    
    for extension_id in extension_ids:
        for installed_extension in installed_extensions:
            if installed_extension.startswith(extension_id):
                extension_status[extension_id] = True
                break
        else:
            extension_status[extension_id] = False

    return extension_status


if __name__ == "__main__":
    intro()
    if is_vscode_installed():
        print(f"{GREEN}Visual Studio Code is installed in the Applications folder.{RESET}")
    else:
        print(f"{RED}Visual Studio Code is not installed in the Applications folder.{RESET}")

    # Replace with the desired extension IDs (publisher.extension-name)
    extension_ids = [
        "natizyskunk.sftp-1.16.1",
        "vincaslt.highlight-matching-tag-0.11.0"
    ]

    extension_status = are_vscode_extensions_installed(extension_ids)

    for extension_id, is_installed in extension_status.items():
        if is_installed:
            print(f"{GREEN}The extension '{extension_id}' is installed.{RESET}")
        else:
            print(f"{RED}The extension '{extension_id}' is not installed.{RESET}")
    
    if is_homebrew_installed():
        print(f"{GREEN}Homebrew is installed.{RESET}")
    else:
        print(f"{RED}Homebrew is not installed.{RESET}")
    
    bin_folders = ["/usr/bin", "/usr/local/bin", "/opt/homebrew/bin"]
    python_versions = get_python_versions(bin_folders)

    if not python_versions:
        print("No Python minor versions found.")
    else:
        for version in python_versions:
            executable = get_version_executable(version, bin_folders)
            
            if executable:
                print(f"{GREEN}Python {version} is installed at {executable}{RESET}")
            else:
                print(f"Python {version} is not installed")
