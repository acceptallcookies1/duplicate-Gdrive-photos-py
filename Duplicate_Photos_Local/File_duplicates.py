import os
import hashlib
from datetime import datetime

def calculate_file_hash(file_path, chunk_size=8192):
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                hash_md5.update(chunk)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None
    return hash_md5.hexdigest()

def find_duplicates(directory, log_folder):
    """Find and log duplicate files based on their hash."""
    hashes = {}  # To store file hashes and their paths
    duplicates = []  # To store duplicate file paths

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)

            if file_hash:
                if file_hash in hashes:
                    # Duplicate found
                    print(f"Duplicate Found:\n  - {file_path}\n  - {hashes[file_hash]}")
                    duplicates.append((file_path, hashes[file_hash]))
                else:
                    # Store hash and path
                    hashes[file_hash] = file_path

    # Write duplicates to a log file
    if duplicates:
        log_file = os.path.join(log_folder, f"duplicates_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        with open(log_file, "w") as log:
            log.write("Duplicate Files Found:\n\n")
            for dup1, dup2 in duplicates:
                log.write(f"Duplicate 1: {dup1}\nDuplicate 2: {dup2}\n\n")
        print(f"\nDuplicate file paths logged to: {log_file}")
    else:
        print("\nNo duplicate files found.")

def setup_log_folder():
    """Create Logs folder in the script directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_folder = os.path.join(script_dir, "Logs")
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    return log_folder

if __name__ == "__main__":
    print("Duplicate File Finder Script")
    directory_to_scan = input("Enter the path of the folder to scan for duplicates: ").strip()

    # Set up Logs folder
    log_folder = setup_log_folder()

    # Run the duplicate finder
    find_duplicates(directory_to_scan, log_folder)
    print("\nDuplicate scan completed.")
