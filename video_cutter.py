import subprocess

if __name__ == "__main__":
    N = input("Insert the duration of the portion: ");
    subprocess.call(["ffmpeg", "-ss", str(0), "-i", "Big_Buck_Bunny.mp4", "-c",
                     "copy", "-t", N, "BBB_cut.mp4"])
