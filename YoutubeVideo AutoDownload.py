from pytube import YouTube

# Replace with the YouTube video URL you want to download
video_url = "https://www.youtube.com/watch?v=your_video_id_here"

try:
    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the highest resolution stream
    stream = yt.streams.get_highest_resolution()

    # Specify the download location (replace with your desired path)
    download_path = "C:/Downloads/"

    # Download the video
    stream.download(output_path=download_path)

    print("Video downloaded successfully!")

except Exception as e:
    print(f"An error occurred: {str(e)}")