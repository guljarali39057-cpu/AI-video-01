import os
import google.auth.transport.requests
import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_authenticated_service():
    creds = None
    if os.path.exists('token.json'):
        try:
            creds = google.oauth2.credentials.Credentials.from_authorized_user_file('token.json', SCOPES)
        except Exception as e:
            print(f"Error loading existing token: {e}")
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(google.auth.transport.requests.Request())
            except Exception as e:
                print(f"Error refreshing token: {e}")
                creds = None
        
        if not creds:
            if not os.path.exists('client_secret.json'):
                print("Error: client_secret.json file is missing!")
                return None
            
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', 
                SCOPES, 
                redirect_uri='urn:ietf:wg:oauth:2.0:oob'
            )
            auth_url, _ = flow.authorization_url(prompt='consent')
            
            print("\n==========================================")
            print("GOOGLE ACCOUNT AUTHORIZATION REQUIRED:")
            print("1. Copy this link and open it in your phone browser:")
            print(auth_url)
            print("2. Allow permission and copy the authorization code.")
            print("==========================================")
            
            code = input("Paste the authorization code here: ").strip()
            flow.fetch_token(code=code)
            creds = flow.credentials
            
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('youtube', 'v3', credentials=creds)

def upload_video_to_youtube(video_file="gta6_clip.mp4", title="Amazing Animal Facts #shorts", description="Fascinating facts about animals! Subscribe for more daily shorts. #shorts #animals"):
    print("Initializing YouTube upload service...")
    youtube = get_authenticated_service()
    
    if not youtube:
        print("Failed to authenticate with YouTube.")
        return False

    if not os.path.exists(video_file):
        print(f"Error: Video file {video_file} not found for upload!")
        return False

    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': ['animals', 'facts', 'shorts', 'wildlife'],
            'categoryId': '15'  # Pets & Animals category
        },
        'status': {
            'privacyStatus': 'public',
            'selfDeclaredMadeForKids': False
        }
    }

    media = MediaFileUpload(video_file, chunksize=-1, resumable=True)

    print(f"Uploading {video_file} to YouTube...")
    request = youtube.videos().insert(
        part='snippet,status',
        body=body,
        media_body=media
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Upload progress: {int(status.progress() * 100)}%")

    print(f"Video uploaded successfully! Video ID: {response.get('id')}")
    return True

def run_background_pipeline():
    # video_metadata.txt se dynamic title aur description read karenge jo trending_generator ne banaya hai
    title = "Amazing Animal Facts #shorts"
    description = "Fascinating facts about animals! Subscribe for more daily shorts. #shorts #animals"
    
    if os.path.exists("video_metadata.txt"):
        try:
            with open("video_metadata.txt", "r", encoding="utf-8") as mf:
                content = mf.read()
                for line in content.splitlines():
                    if line.startswith("Title:"):
                        title = line.replace("Title:", "").strip()
                    elif line.startswith("Description:"):
                        description = line.replace("Description:", "").strip()
        except Exception as e:
            print(f"Error reading metadata file: {e}")

    upload_video_to_youtube(title=title, description=description)

if __name__ == "__main__":
    run_background_pipeline()
