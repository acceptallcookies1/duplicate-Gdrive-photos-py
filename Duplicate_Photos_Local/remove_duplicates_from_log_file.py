import os

def remove_duplicates(log_file_path, log_folder):
    """Reads a log file and removes duplicate files."""
    processed_files = set()  # To avoid processing the same file multiple times
    deleted_files = []

    # Confirmation before deletion
    print("\nWarning: This script will delete duplicate files listed in the log file.")
    confirmation = input("Do you want to continue? (yes/no): ").strip().lower()
    if confirmation != "yes":
        print("Operation cancelled.")
        return

    try:
        with open(log_file_path, 'r') as log_file:
            lines = log_file.readlines()

        # Process duplicate files
        for line in lines:
            if line.startswith("Duplicate 2:"):  # Only delete 'Duplicate 2'
                file_path = line.split(": ", 1)[1].strip()

                if os.path.exists(file_path) and file_path not in processed_files:
                    try:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                        deleted_files.append(file_path)
                        processed_files.add(file_path)
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")
                else:
                    print(f"File not found or already processed: {file_path}")

        # Log deletions
        if deleted_files:
            deletion_log = os.path.join(log_folder, "deletion_log.txt")
            with open(deletion_log, "w") as log:
                log.write("Deleted Duplicate Files:\n\n")
                for file in deleted_files:
                    log.write(f"{file}\n")
            print(f"\nDeletion log saved to: {deletion_log}")
        else:
            print("\nNo files were deleted.")

    except FileNotFoundError:
        print(f"Error: The file '{log_file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def setup_log_folder():
    """Create Logs folder in the script directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_folder = os.path.join(script_dir, "Logs")
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    return log_folder

if __name__ == "__main__":
    print("Duplicate File Remover Script")
    log_file_path = input("Enter the path of the log file: ").strip()

    # Set up Logs folder for deletion logs
    log_folder = setup_log_folder()

    # Remove duplicates
    remove_duplicates(log_file_path, log_folder)
    print("\nDuplicate file removal completed.")
import os

def remove_duplicates(log_file_path, log_folder):
    """Reads a log file and removes duplicate files."""
    processed_files = set()  # To avoid processing the same file multiple times
    deleted_files = []

    # Confirmation before deletion
    print("\nWarning: This script will delete duplicate files listed in the log file.")
    confirmation = input("Do you want to continue? (yes/no): ").strip().lower()
    if confirmation != "yes":
        print("Operation cancelled.")
        return

    try:
        with open(log_file_path, 'r') as log_file:
            lines = log_file.readlines()

        # Process duplicate files
        for line in lines:
            if line.startswith("Duplicate 2:"):  # Only delete 'Duplicate 2'
                file_path = line.split(": ", 1)[1].strip()

                if os.path.exists(file_path) and file_path not in processed_files:
                    try:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                        deleted_files.append(file_path)
                        processed_files.add(file_path)
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")
                else:
                    print(f"File not found or already processed: {file_path}")

        # Log deletions
        if deleted_files:
            deletion_log = os.path.join(log_folder, "deletion_log.txt")
            with open(deletion_log, "w") as log:
                log.write("Deleted Duplicate Files:\n\n")
                for file in deleted_files:
                    log.write(f"{file}\n")
            print(f"\nDeletion log saved to: {deletion_log}")
        else:
            print("\nNo files were deleted.")

    except FileNotFoundError:
        print(f"Error: The file '{log_file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def setup_log_folder():
    """Create Logs folder in the script directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_folder = os.path.join(script_dir, "Logs")
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    return log_folder

if __name__ == "__main__":
    print("Duplicate File Remover Script")
    log_file_path = input("Enter the path of the log file: ").strip()

    # Set up Logs folder for deletion logs
    log_folder = setup_log_folder()

    # Remove duplicates
    remove_duplicates(log_file_path, log_folder)
    print("\nDuplicate file removal completed.")
