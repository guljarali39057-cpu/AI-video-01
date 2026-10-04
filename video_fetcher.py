import os
import time
import random
import shutil

def fetch_latest_instagram_reel():
    print("Switching to secure, zero-error Free Video Source (No rate limits)...")
    
    # Ensure directory exists
    if not os.path.exists("instagram_downloads"):
        os.makedirs("instagram_downloads")
        
    # Yahan hum local fallback ya direct free stock source use kar rahe hain taaki 
    # 24/7 hosting par bina kisi 429 error ke non-stop videos banti rahein.
    if os.path.exists("source_gameplay.mp4"):
        # Har baar ek fresh copy bana do taaki pipeline confuse na ho
        target_file = "instagram_downloads/downloaded_video.mp4"
        shutil.copy("source_gameplay.mp4", target_file)
        print("Free source video successfully loaded for processing!")
        return True
    else:
        print("Error: source_gameplay.mp4 file missing in folder!")
        return False
