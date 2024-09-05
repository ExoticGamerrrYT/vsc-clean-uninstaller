import os
import shutil
import subprocess
import sys


def is_vscode_installed():
    """Check if VS Code is installed and if it is, where.

    Returns:
        str: The path where VS Code is installed.
    """
    # Check both uninstaller paths
    program_files_uninstall = r"C:\Program Files\Microsoft VS Code\unins000.exe"
    user_uninstall = os.path.expandvars(
        r"%LocalAppData%\Programs\Microsoft VS Code\unins000.exe"
    )

    if os.path.exists(program_files_uninstall):
        return program_files_uninstall
    elif os.path.exists(user_uninstall):
        return user_uninstall
    else:
        return None


def uninstall_vscode():
    """Execute the VS Code default uninstaller."""
    uninstall_path = is_vscode_installed()

    if uninstall_path:
        try:
            if "Program Files" in uninstall_path:
                print("Starting VS Code uninstaller from Program Files...")
            else:
                print("Starting VS Code uninstaller from user installation...")

            subprocess.run([uninstall_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running the uninstaller: {e}")
    else:
        print("VS Code is not installed in the default paths.")


def clean_uninstall():
    """Remove the configuration folders and extensions."""
    try:
        # Delete user configuration and data folders
        print("Cleaning up residual VS Code files...")
        paths_to_delete = [
            os.path.expandvars(r"%AppData%\Code"),
            os.path.expandvars(r"%UserProfile%\.vscode"),
            os.path.expandvars(r"%LocalAppData%\Programs\Microsoft VS Code"),
        ]
        for path in paths_to_delete:
            if os.path.exists(path):
                shutil.rmtree(path, ignore_errors=True)
                print(f"Deleted: {path}")
            else:
                print(f"Folder not found: {path}")
    except Exception as e:
        print(f"Error cleaning up files: {e}")


def delete_shortcuts():
    """Remove the shortcuts on the Desktop and Start Menu if they exist."""
    try:
        # Paths to the Desktop and Start Menu shortcuts
        desktop_shortcut = os.path.expandvars(
            r"%UserProfile%\Desktop\Visual Studio Code.lnk"
        )
        start_menu_shortcut = os.path.expandvars(
            r"%AppData%\Microsoft\Windows\Start Menu\Programs\Visual Studio Code.lnk"
        )

        print("Deleting shortcuts if they exist...")
        shortcuts = [desktop_shortcut, start_menu_shortcut]
        for shortcut in shortcuts:
            if os.path.exists(shortcut):
                os.remove(shortcut)
                print(f"Deleted: {shortcut}")
            else:
                print(f"Shortcut not found: {shortcut}")

    except Exception as e:
        print(f"Error deleting shortcuts: {e}")


def user_confirmation():
    """Asking the user if they really want to delete VS Code and all its folders.

    Returns:
        bool: User choice.
    """
    while True:
        confirmation = (
            input(
                "Are you sure you want to uninstall Visual Studio Code? This will delete everything (Y/N): "
            )
            .strip()
            .lower()
        )
        if confirmation in ["y", "n"]:
            return confirmation == "y"
        else:
            print("Invalid option. Enter 'Y' for yes or 'N' for no.")


def main():
    if user_confirmation():
        print("Uninstalling Visual Studio Code...")
        uninstall_vscode()
        print("Running clean uninstall...")
        clean_uninstall()
        print("Removing shortcuts...")
        delete_shortcuts()
        print("VS Code has been successfully uninstalled.")
    else:
        print("VS Code uninstallation canceled.")
    input("Press Enter to exit...")  # Wait for the user to press Enter before exiting


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation canceled by user.")
        sys.exit(0)
