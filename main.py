import os
import re


def main():
    for file in os.listdir("data"):
        if file == ".keep":
            continue

        with open(os.path.join("data", file)) as srt_file:
            subtitle_data = srt_file.read()

        subtitles = subtitle_data.split("\n\n")
        cleaned_subtitles = []

        for subtitle in subtitles:
            subtitle_data = subtitle.split("\n")

            if len(subtitle_data) <= 2:
                continue

            subtitle_number, _, *content = subtitle_data
            content = "\n".join(content)

            content = re.sub(r"<b><font [a-zA-Z0-9''=#]*>", "", content)
            content = re.sub(r"</font></b>", "", content)
            cleaned_subtitles.append(f"{subtitle_number} {content}")

        cleaned_subtitles_string = "\n".join(cleaned_subtitles)

        with open(os.path.join("data", f"{file}-cleaned.srt"), "w") as cleaned_file:
            cleaned_file.write(cleaned_subtitles_string)


if __name__ == "__main__":
    main()
