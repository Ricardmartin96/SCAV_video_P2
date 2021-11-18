import subprocess

if __name__ == "__main__":
    subprocess.call(["ffmpeg", "-i", "BBB_cut.mp4", "-vf", "split=2[a][b],"
                                                           "[b]histogram,"
                                                           "format=yuva444p[hh],"
                                                           "[a][hh]overlay",
                     "BBB_hist.mp4"])
