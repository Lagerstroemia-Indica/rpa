import os
import zipfile
from yt_dlp import YoutubeDL
from moviepy.editor import VideoFileClip

def download_video(url, output_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        downloaded_file = ydl.prepare_filename(info)
        return downloaded_file

def convert_to_mp3(input_file, output_file):
    with VideoFileClip(input_file) as video:
        audio = video.audio
        audio.write_audiofile(output_file, codec='mp3')
    os.remove(input_file)  # Optionally, remove the original file after conversion

def create_zip(audio_files, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in audio_files:
            zipf.write(file, os.path.basename(file))
            os.remove(file)  # Optionally, remove the file after adding to zip to save space

def main(video_urls, output_dir, zip_name):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    audio_files = []
    for url in video_urls:
        print(f"Downloading and converting: {url}")
        video_file = download_video(url, output_dir)
        base, ext = os.path.splitext(video_file)
        mp3_file = base + '.mp3'
        convert_to_mp3(video_file, mp3_file)
        audio_files.append(mp3_file)
    
    print(f"Creating zip file: {zip_name}")
    create_zip(audio_files, zip_name)
    print("All tasks completed!")


# 파일 읽기
def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()
    return urls

if __name__ == "__main__":
    file_path = './hongsi_playlist.txt'
    video_urls = read_urls_from_file(file_path)
    # video_urls = [
    #     'https://www.youtube.com/watch?v=GFGPSx6cPN0',
    #     'https://www.youtube.com/watch?v=g-qF3GuAozw',
    #     # Add more video URLs here
    # ]
    output_dir = "audio_files"
    zip_name = "audio_files.zip"
    
    main(video_urls, output_dir, zip_name)
