from pytubeX import YouTube, Playlist
import tkinter as tk
import re
import os
from tkinter import filedialog
from tkinter import ttk
import moviepy.editor as mp  # moviepy needs ffmpeg
import threading


def main():
    # setting up the window itself
    window = tk.Tk()
    window.resizable(False, False)
    window.geometry("720x720")  # set the size
    window.title("songs downloader")
    window.iconbitmap(r"C:\Users\levin\Downloads\logo.ico")

    # convert seconds to minutes and seconds
    def convert_seconds_to_minutes(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes}:{seconds}"

    def check_link(link, type):  # check if it is YouTube song or playlist link
        if type == 'p':
            if re.search('www.youtube.com/playlist' or 'youtube.com/playlist', link):  # playlist
                # www... dependent on the copy of the link
                return True
            else:
                return False
        else:
            if re.search('www.youtube.com/watch' or 'youtube.com/watch', link):  # song
                return True
            else:
                return False

    class buttons:
        def __init__(self):
            self.folder_path = tk.StringVar(window)  # tk.StringVar changes by the value
            self.format_type = tk.StringVar(window)
            self.download_type = tk.StringVar(window)
            self.link = tk.StringVar(window)
            self.message = tk.StringVar(window)

        def browse_button(self):
            # Allow user to select a directory and store it in global var
            # called folder_path
            filename = filedialog.askdirectory()
            self.folder_path.set(filename)

        def format_Button(self):
            # set up variable
            formatChoices = ["video/mp4", "video/3gpp", "audio/mp3", "video/webm", "audio/webm"]
            option_menu = ttk.OptionMenu(window, self.format_type, formatChoices[0], *formatChoices)
            # formatChoices[0] is for start in the first option and not pass it
            return option_menu

        def type_button(self):
            txt = ttk.Label(window, text="Choose the type of the download")
            txt.pack()
            R1 = ttk.Radiobutton(window, text="Playlist", variable=self.download_type, value="p")
            R1.pack()
            R2 = ttk.Radiobutton(window, text="Song", variable=self.download_type, value="s")
            R2.pack()

        def Url_box(self):
            txt = ttk.Label(window, text="Enter the youtube Url")
            txt.pack()
            url_Box = tk.Entry(window, width=70, borderwidth=5, textvariable=self.link)
            url_Box.pack()

        # noinspection PyTypeChecker
        def download_button(self):
            response_display = ttk.Label(window, textvariable=self.message, text=str(self.message.get()))
            response_display.pack()
            download_butt = ttk.Button(window, text="download",
                                       command=lambda: threading.Thread(target=download_video(self.link.get(),
                                                                                              self.format_type.get(),
                                                                                              self.folder_path.get(),
                                                                                              self.download_type.get())).start())
            download_butt.pack()

    def convert_to_mp3(path, format):
        if re.search(format, path):
            mp4_path = os.path.join(path)
            mp3_path = os.path.join(os.path.splitext(path)[0] + '.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)

    def download_video(link, format_type, path, type):
        response = butt.message
        real_type = None
        print("run")
        if check_link(link, type):  # check if it is YouTube song or playlist link
            type_space_index = format_type.index("/")
            if "mp3" in format_type:  # pytube not supporting mp3, so it will be on mp4 and then will convert
                format_type = format_type[:type_space_index + 1] + "mp4"
                real_type = "mp3"
            v_or_a = format_type[:type_space_index]  # video or audio
            format = format_type[type_space_index + 1:]  # mp4,webm....
            if type == "s":  # song
                video = YouTube(link)
                print("work")
                response.set(f"Downloading {video.title} | {convert_seconds_to_minutes(video.length)};")
                print("work2")
                video.streams.filter(
                    mime_type=f"{v_or_a}/{format}", progressive=False).first().download(path)
                if real_type == "mp3":
                    file_path = f"{path}/{video.title}.{format}"
                    convert_to_mp3(file_path, format)
                response.set(f"Downloaded {video.title} | {convert_seconds_to_minutes(video.length)};")
                response.set('Error: the video is private or not working.\n check the link please')

            elif type == "p":  # playlist
                try:
                    playlist = Playlist(link)
                    didnt_work_list = []
                    for video in playlist.video_urls:
                        try:
                            video = YouTube(video)
                            tk.Label(text=f"Downloading {video.title} | {convert_seconds_to_minutes(video.length)};")
                            video.streams.filter(
                                mime_type=f"{v_or_a}/{format}", progressive=False).first().download(path)
                            if real_type == "mp3":
                                file_path = f"{path}/{video.title}.{format}"
                                convert_to_mp3(file_path, format)
                            response.set(f"Downloaded {video.title} | {convert_seconds_to_minutes(video.length)};")
                            print(f"Downloaded {video.title} | {convert_seconds_to_minutes(video.length)};")
                        except:
                            print("eror")
                            didnt_work_list.append(video.title)
                    if len(didnt_work_list) != 0:
                        print("eror with some songs " + str(len(didnt_work_list)))
                        response.set(f'Downloaded {playlist.title} | {playlist.length};\n'
                                     f'there was a problem with some of the song,here is a list of them:{didnt_work_list}\n'
                                     f'recommend to download them separately')
                    else:
                        response.set(f"Downloaded {playlist.title} | {convert_seconds_to_minutes(playlist.length)};")
                except:
                    response.set('Error:the playlist is private or not working.\n check the link please')
            else:
                tk.messagebox.showerror(title="you need to choose one of the options(playlist or video", message=type)
        else:
            tk.messagebox.showerror(title="Invaild Link", message="Invalid  link!")
        return None

    # buttons:
    butt = buttons()

    # directory choosing:
    directory_button = ttk.Button(text="choose Directory to save", command=butt.browse_button)
    directory_text = ttk.Label(window, textvariable=butt.folder_path)

    # format button:
    format_line = tk.Label(window, text="Choose the format to download")
    format_choices = butt.format_Button()

    # type button:
    butt.type_button()

    # URL box:
    butt.Url_box()

    # dowlond button:
    butt.download_button()


    directory_button.pack()
    directory_text.pack()
    format_line.pack()
    format_choices.pack()
    window.mainloop()


if __name__ == "__main__":
    main()
