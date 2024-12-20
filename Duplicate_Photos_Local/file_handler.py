import os
import shutil
import logging
from datetime import datetime


def organize_files(source_folder):
    # Validate the folder path
    if not os.path.exists(source_folder):
        print("The folder does not exist. Please provide a valid path.")
        return

    # Set up logging to create a log file in the source folder
    log_filename = os.path.join(source_folder, f"organize_log_{
                                datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    logging.basicConfig(
        filename=log_filename,
        filemode='w',  # Overwrite file if it exists
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    logger = logging.getLogger(__name__)

    logger.info("Starting file organization...")

    # Define folder categories
    folders = {
        "Text": [".txt", ".log", ".md"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".doc", ".pptx"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Scripts": [".py", ".js", ".sh"],
        "Others": []
    }

    # Create the necessary folders if they don't exist
    for folder in folders.keys():
        folder_path = os.path.join(source_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            logger.info(f"Created folder: {folder_path}")

    # Loop through all files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        if filename.startswith("organize_log_") and filename.endswith(".log"):
            continue

        # Extract file extension
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Move file to the correct folder
        moved = False
        for folder, extensions in folders.items():
            if extension in extensions:
                dest_folder = os.path.join(source_folder, folder)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                logger.info(f"Moved file '{filename}' to '{folder}' folder.")
                moved = True
                break

        # If no matching folder, move to "Others"
        if not moved:
            dest_folder = os.path.join(source_folder, "Others")
            shutil.move(file_path, os.path.join(dest_folder, filename))
            logger.info(f"Moved file '{filename}' to 'Others' folder.")

    logger.info("File organization completed successfully!")


# User Input: Source folder path
source_folder = input("Enter the path to the folder you want to organize: ")
organize_files(source_folder)
print("File organization complete. Check the generated log file for details.")
