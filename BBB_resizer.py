import subprocess

# resize video
#ffmpeg -i BBB_cut.mp4 -s 1280x720 -c:a copy BBB_720.mp4

if __name__ == "__main__":
    subprocess.call(["ffmpeg", "-i", "BBB_cut.mp4", "-s", "1280x720",
                     "-c:a", "copy", "BBB_720.mp4"])

    subprocess.call(["ffmpeg", "-i", "BBB_cut.mp4", "-s", "640x480",
                     "-c:a", "copy", "BBB_480.mp4"])

    subprocess.call(["ffmpeg", "-i", "BBB_cut.mp4", "-s", "360x240",
                     "-c:a",  "copy", "BBB_240.mp4"])

    subprocess.call(["ffmpeg", "-i", "BBB_cut.mp4", "-s", "160x120",
                     "-c:a",  "copy", "BBB_120.mp4"])
