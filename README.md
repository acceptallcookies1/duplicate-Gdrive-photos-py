# Beginner Python Projects

This repository contains a collection of beginner-friendly Python scripts to automate file management tasks. Each script focuses on practical use cases like comparing folders, finding duplicates, and organizing photos.

---

## 📂 Project Structure

TBD


---

## 🛠️ Scripts Overview

1. **compare_photos.py**
   - **Purpose**: Compare local photo folders with a Google Drive folder and identify missing files.
   - **Requirements**:
      - `credentials.json` (Google Drive API key – not included).
      - Python libraries: `google-api-python-client`, `oauth2client`.

2. **Duplicate Photo Finder**
   - **Purpose**: Find duplicate files in a directory and log their paths.
   - **Output**: Logs duplicates in `Logs/duplicates_log_<timestamp>.txt`.

---

## 🚀 Setup and Usage

### **Prerequisites**
- Python 3.x installed.
- Required libraries:
   ```bash
   pip install google-api-python-client oauth2client


   
1. Run the Duplicate Finder Script
python duplicate_finder.py
Follow prompts to enter the folder path.
Check the Logs/ folder for the results.
2. Compare Google Drive and Local Folders
Place your credentials.json file in the project root (not included).
Run:
python compare_photos.py


Follow prompts to input folder paths and Google Drive IDs.


🔒 Notes on Security
credentials.json contains sensitive API keys. It is excluded using .gitignore to prevent accidental uploads.
Avoid sharing this file publicly.


🤝 Contributions
Feel free to fork this repository, open issues, or submit pull requests!

