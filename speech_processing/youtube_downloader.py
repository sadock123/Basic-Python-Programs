import  os
import speech_recognition as sr 
import moviepy.editor as mp
from pytube import YouTube

def download_360p_mp4_videos(url: str, outpath: str = "./"):

    yt = YouTube(url)

    yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath)


if __name__ == "__main__":

    download_360p_mp4_videos(
        "https://www.youtube.com/watch?v=D702x_u0rts",
    )
    clip=mp.VideoFileClip(r"./spiderman.mp4")
    clip.audio.write_audiofile(r'converted.wav')