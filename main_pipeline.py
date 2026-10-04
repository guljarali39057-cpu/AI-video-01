import os
import time
import shutil

def run_pipeline():
    print("==========================================")
    print("Starting SnakeMystry Shorts Pipeline...")
    print("==========================================")
    
    # Step 1: Ensure source video is ready
    print("\n[Step 1/3] Preparing source video...")
    if not os.path.exists("instagram_downloads"):
        os.makedirs("instagram_downloads")
        
    if os.path.exists("source_gameplay.mp4"):
        shutil.copy("source_gameplay.mp4", "instagram_downloads/downloaded_video.mp4")
        print("Source video ready successfully!")
    else:
        print("Error: source_gameplay.mp4 file nahi mili!")
        return

    time.sleep(1)
    
    # Step 2: Generate short video & voiceover
    print("\n[Step 2/3] Generating animal/snake fact short...")
    try:
        import trending_generator
        trending_generator.generate_trending_short()
        print("Video generation successful!")
    except Exception as e:
        print(f"Error in video generation: {e}")
        return

    time.sleep(2)
    
    # Step 3: Upload to YouTube @SnakeMystryShorts
    print("\n[Step 3/3] Uploading video to YouTube...")
    try:
        import animal_channel_daemon
        animal_channel_daemon.run_background_pipeline()
        print("Pipeline execution completed successfully!")
    except Exception as e:
        print(f"Error in YouTube upload: {e}")

if __name__ == "__main__":
    run_pipeline()
