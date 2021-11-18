import subprocess

if __name__ == "__main__":
    # convert to mono:  ffmpeg -i Efectos_Vocales.flac -ac 1 EV_mono.flac
    subprocess.call(["ffmpeg", "-i", "Efectos_Vocales.flac", "-ac", "1",
                    "EV_mono.flac"])

    # change audio codec: ffmpeg -i Efectos_Vocales.flac -c:a aac EV_converted.aac
    subprocess.call(["ffmpeg", "-i", "Efectos_Vocales.flac", "-c:a", "aac",
                     "EV_ac_changed.aac"])