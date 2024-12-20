import os

def get_duplicate_size(log_file_path):
    """Reads a log file, calculates the total size of duplicate files."""
    total_size = 0
    processed_files = set()  # To avoid double-counting duplicates

    # Read the log file and extract paths
    try:
        with open(log_file_path, 'r') as log_file:
            lines = log_file.readlines()

        print("\nCalculating total size of duplicate files...\n")

        for line in lines:
            if line.startswith("Duplicate 1:") or line.startswith("Duplicate 2:"):
                file_path = line.split(": ", 1)[1].strip()
                
                # Check if the file exists and avoid duplicates
                if os.path.exists(file_path) and file_path not in processed_files:
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                    processed_files.add(file_path)

                    print(f"Found file: {file_path} ({file_size / (1024 * 1024):.2f} MB)")

        print("\n--- Duplicate Size Summary ---")
        print(f"Total size of duplicate files: {total_size / (1024 * 1024):.2f} MB")

    except FileNotFoundError:
        print(f"Error: The file '{log_file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Duplicate File Size Calculator")
    log_file_path = input("Enter the path of the log file: ").strip()
    
    # Calculate duplicate size
    get_duplicate_size(log_file_path)
