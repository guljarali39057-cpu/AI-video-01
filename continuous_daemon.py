import os
import time
import random
import logging

# Logging setup
logging.basicConfig(
    filename='snake_channel_daemon.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_full_pipeline():
    logging.info("Starting automated video generation cycle...")
    print("\n==========================================")
    print("Starting Automated Generation & Upload Cycle...")
    print("==========================================")
    
    # Step 1: Trending generator chalayenge jo topic ke hisab se title aur video banayega
    try:
        import trending_generator
        trending_generator.generate_trending_short()
        logging.info("Video generation successful.")
    except Exception as e:
        logging.error(f"Error in video generation: {e}")
        print(f"Error in video generation: {e}")
        return False

    time.sleep(5)
    
    # Step 2: YouTube uploader chalayenge jo dynamic title aur description ke sath upload karega
    try:
        import animal_channel_daemon
        animal_channel_daemon.run_background_pipeline()
        logging.info("Video uploaded successfully to @SnakeMystryShorts.")
        print("Video uploaded successfully!")
    except Exception as e:
        logging.error(f"Error in YouTube upload: {e}")
        print(f"Error in YouTube upload: {e}")
        return False
        
    return True

if __name__ == "__main__":
    print("SnakeMystry Shorts 24/7 Automation Daemon Started!")
    logging.info("Daemon started for 24/7 automated pipeline.")
    
    # 24 ghante mein 10 videos matlab har 2.4 ghante (approx 144 minutes) mein 1 video
    UPLOAD_INTERVAL_SECONDS = 144 * 60 
    
    while True:
        success = run_full_pipeline()
        
        if success:
            print( اگla upload 144 minute baad hoga... )
        else:
            print("Kuch error aaya, thodi der baad retry karenge...")
            
        # Agle run ke liye wait karenge
        time.sleep(UPLOAD_INTERVAL_SECONDS)
