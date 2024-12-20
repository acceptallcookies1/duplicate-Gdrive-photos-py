import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def authenticate_google_drive():
    """Authenticate and return Google Drive service."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    service = build('drive', 'v3', credentials=creds)
    return service

def list_google_drive_photos_recursive(service, folder_id):
    """Recursively list all photo filenames in a Google Drive folder and its subfolders."""
    photos = set()

    # Query for files in the current folder
    query = f"'{folder_id}' in parents and (mimeType contains 'image/')"
    results = service.files().list(q=query, fields="files(name)").execute()
    files = results.get('files', [])
    for file in files:
        photos.add(file['name'])

    # Query for subfolders
    query_folders = f"'{folder_id}' in parents and mimeType = 'application/vnd.google-apps.folder'"
    results = service.files().list(q=query_folders, fields="files(id, name)").execute()
    subfolders = results.get('files', [])

    # Recursively list photos in subfolders
    for subfolder in subfolders:
        subfolder_id = subfolder['id']
        photos.update(list_google_drive_photos_recursive(service, subfolder_id))

    return photos

def list_local_photos_recursive(local_folder):
    """Recursively list all photo filenames in a local folder and its subfolders."""
    photos = set()
    for root, _, files in os.walk(local_folder):  # os.walk traverses directories recursively
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                photos.add(file)
    return photos

def compare_photos(google_photos, local_photos):
    """Compare Google Drive and local photos."""
    missing_photos = local_photos - google_photos
    extra_photos = google_photos - local_photos
    return missing_photos, extra_photos

def process_multiple_folders(service):
    """Compare multiple pairs of folders (Google Drive ↔ Local)."""
    pairs = []
    
    # User input for folder pairs
    num_folders = int(input("Enter the number of folder pairs to compare: "))
    for i in range(num_folders):
        print(f"\nPair {i + 1}:")
        local_folder = input("Enter the path to the local folder: ").strip()
        google_drive_folder_id = input("Enter the Google Drive folder ID: ").strip()
        pairs.append((local_folder, google_drive_folder_id))

    # Process each folder pair
    for i, (local_folder, google_drive_folder_id) in enumerate(pairs):
        print(f"\n### Comparing Pair {i + 1} ###")
        print(f"Local Folder: {local_folder}")
        print(f"Google Drive Folder ID: {google_drive_folder_id}")

        google_photos = list_google_drive_photos_recursive(service, google_drive_folder_id)
        local_photos = list_local_photos_recursive(local_folder)

        missing_photos, extra_photos = compare_photos(google_photos, local_photos)

        if missing_photos:
            print("\nPhotos missing in Google Drive:")
            for photo in missing_photos:
                print(f" - {photo}")
        else:
            print("\nAll photos from the local folder are backed up to Google Drive.")

        if extra_photos:
            print("\nPhotos in Google Drive but not on your PC:")
            for photo in extra_photos:
                print(f" - {photo}")
        else:
            print("\nNo extra photos found on Google Drive.")

if __name__ == '__main__':
    # Authenticate Google Drive API
    service = authenticate_google_drive()

    # Compare multiple folder pairs
    process_multiple_folders(service)
    print("\nComparison complete.")
