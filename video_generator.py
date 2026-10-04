from moviepy import VideoFileClip

def generate_short_clip(input_file, output_file, duration=30):
    print(f"Processing '{input_file}' to generate auto clip...")
    
    # Load the raw gameplay video
    clip = VideoFileClip(input_file)
    
    # Cut the clip (e.g., from 0th second to 30th second)
    # Aap chahein toh start aur end time apne hisab se set kar sakte hain
    short_clip = clip.subclipped(0, min(duration, clip.duration))
    
    # Save the generated video
    short_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')
    print(f"Auto-generated video saved as: {output_file}")

if __name__ == "__main__":
    # Yahan apni raw video ka naam dein aur output mein wahi naam dein jo upload script use kare
    input_video = "source_gameplay.mp4" 
    output_video = "gta6_clip.mp4"
    
    generate_short_clip(input_video, output_video, duration=30)
