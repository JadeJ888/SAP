import vlc
import tkinter as tk

audiofile = "\\audio\\sanctuary.mp3" 
vlcinstance = vlc.Instance()
medialist = vlcinstance.media_list_new() #defines list of files to be played
mediaplayer = vlcinstance.media_list_player_new() 
media = vlcinstance.media_new_path(audiofile) #choose audio file to be loaded
medialist.add_media(media) #adds media to media list
mediaplayer.set_media_list(medialist) #sets media list to media player
mediaplayer.set_playback_mode(vlc.PlaybackMode.loop) #sets playback mode to loop

def main():
    root = tk.Tk()
    root.configure(bg='#000000')
    button = tk.Button(root, bg='#000000', fg='#000000', activebackground='#000000', text="Play/Pause", command=handle_play)
    button.pack(fill="both", expand=True) #makes the button as big as the window
    
    root.mainloop()
    mediaplayer.play()

def handle_play():
    if mediaplayer.is_playing():
        print("Pausing...")
        mediaplayer.pause()
    else:
        print("Playing...")
        mediaplayer.play()

main()