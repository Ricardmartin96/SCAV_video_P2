import subprocess

def videoCutter (N, input, output):
    subprocess.call(["ffmpeg", "-ss", str(0), "-i", input, "-c",
                     "copy", "-t", N, output])

def yuvHist (input, output):
    subprocess.call(["ffmpeg", "-i", input, "-vf", "split=2[a][b],"
                                                           "[b]histogram,"
                                                           "format=yuva444p[hh],"
                                                           "[a][hh]overlay",
                     output])

def videoResizer(input, output1, output2, output3, output4):
    subprocess.call(["ffmpeg", "-i", input, "-s", "1280x720",
                     "-c:a", "copy", output1])

    subprocess.call(["ffmpeg", "-i", input, "-s", "640x480",
                     "-c:a", "copy", output2])

    subprocess.call(["ffmpeg", "-i", input, "-s", "360x240",
                     "-c:a", "copy", output3])

    subprocess.call(["ffmpeg", "-i", input, "-s", "160x120",
                     "-c:a", "copy", output4])

def audioConverter(input, output1, output2):
    # convert to mono:  ffmpeg -i Efectos_Vocales.flac -ac 1 EV_mono.flac
    subprocess.call(["ffmpeg", "-i", input, "-ac", "1",
                     output1])

    # change audio codec: ffmpeg -i Efectos_Vocales.flac -c:a aac EV_converted.aac
    subprocess.call(["ffmpeg", "-i", input, "-c:a", "aac",
                     output2])

if __name__ == "__main__":
    N = input("Insert the duration of the portion: ")

    original_video = "Big_Buck_Bunny.mp4"
    input_video = "BBB_cut.mp4"
    output_video = "BBB_hist.mp4"

    input_audio = "Efectos_Vocales.flac"
    output_audio_1 = "EV_mono.flac"
    output_audio_2 = "EV_ac_changed.aac"

    output_resized_1 = "BBB_720.mp4"
    output_resized_2 = "BBB_480.mp4"
    output_resized_3 = "BBB_240.mp4"
    output_resized_4 = "BBB_120.mp4"

    videoCutter(N, original_video, input_video)
    yuvHist(input_video,output_video)
    videoResizer(input_video, output_resized_1, output_resized_2, output_resized_3, output_resized_4 )
    audioConverter(input_audio, output_audio_1, output_audio_2)