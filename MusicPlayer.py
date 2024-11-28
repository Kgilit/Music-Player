import os
import customtkinter as ctk
import pygame
from tkinter import filedialog


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Music Player")
        self.root.geometry("500x300")
        ctk.set_appearance_mode("Light")  # Options: "System", "Light", "Dark"
        ctk.set_default_color_theme("dark-blue")  # Options: "blue", "green", "dark-blue"

        pygame.mixer.init()

        self.songs = []
        self.current_index = 0
        self.is_paused = False

        # Current Song Display
        self.song_label = ctk.CTkLabel(root, text="No song playing", width=400, height=40, font=("Arial", 16))
        self.song_label.pack(pady=20)

        # Control Buttons
        self.select_button = ctk.CTkButton(root, text="Select Files", command=self.select_files, width=200)
        self.select_button.pack(pady=10)

        self.play_button = ctk.CTkButton(root, text="Play", command=self.play_song, width=200)
        self.play_button.pack(pady=10)

        self.pause_button = ctk.CTkButton(root, text="Pause/Resume", command=self.pause_resume_song, width=200)
        self.pause_button.pack(pady=10)

        self.stop_button = ctk.CTkButton(root, text="Stop", command=self.stop_song, width=200)
        self.stop_button.pack(pady=10)

        # Bottom Info Label
        self.info_label = ctk.CTkLabel(root, text="Select songs to start playback.", font=("Arial", 12),
                                       text_color="gray")
        self.info_label.pack(pady=20)

    def select_files(self):

        file_selected = filedialog.askopenfilenames(
            title="Select Audio Files",
            filetypes=[("Audio Files", "*.mp3 *.wav")]
        )
        if file_selected:
            self.songs = list(file_selected)
            self.current_index = 0
            self.update_song_label(f"Loaded: {os.path.basename(self.songs[0])}")
        else:
            self.update_song_label("No files selected.")

    def play_song(self):

        if self.songs:
            pygame.mixer.music.load(self.songs[self.current_index])
            pygame.mixer.music.play()
            self.is_paused = False
            self.update_song_label(f"Playing: {os.path.basename(self.songs[self.current_index])}")
        else:
            self.update_song_label("No songs to play. Select files first.")

    def pause_resume_song(self):

        if pygame.mixer.music.get_pos() != -1:  # Ensure a song is loaded
            if self.is_paused:
                pygame.mixer.music.unpause()
                self.is_paused = False
                self.update_song_label(f"Playing: {os.path.basename(self.songs[self.current_index])}")
            else:
                pygame.mixer.music.pause()
                self.is_paused = True
                self.update_song_label(f"Paused: {os.path.basename(self.songs[self.current_index])}")
        else:
            self.update_song_label("No music is currently playing.")

    def stop_song(self):

        pygame.mixer.music.stop()
        self.is_paused = False
        self.update_song_label("Stopped playback.")

    def update_song_label(self, text):

        self.song_label.configure(text=text)


# Main Execution
if __name__ == "__main__":
    app = ctk.CTk()
    player = MusicPlayer(app)
    app.mainloop()
