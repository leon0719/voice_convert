import argparse
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def download_video_audio(video_url, title,output_dir):
    yt = YouTube(video_url)
    os.makedirs(output_dir, exist_ok=True)
    file_name = yt.streams.filter(subtype="mp4")[0].download(output_dir)

    audio = AudioFileClip(file_name)
    audio.write_audiofile(os.path.join(output_dir, title +".wav"))
    os.remove(file_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download audio from a YouTube video")
    parser.add_argument("--video_url","-v", required=True ,help="The URL of the YouTube video")
    parser.add_argument("--title","-t",default="name" ,help="The Title of the wav name e.x. 'name'.wav")
    parser.add_argument("--output_dir","-o",default="wav/", help="The directory where the audio file should be saved")
    args = parser.parse_args()
    download_video_audio(args.video_url,args.title,args.output_dir)