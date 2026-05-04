from argparse import ArgumentParser
import os
import re


def main():
    parser = ArgumentParser()
    parser.add_argument("clean_type", help="Either \"full\" or \"remove_font\"")
    args = parser.parse_args()

    for file in os.listdir("data"):
        if file == ".keep":
            continue

        if "cleaned" in file:
            continue

        with open(os.path.join("data", file)) as srt_file:
            subtitle_data = srt_file.read()

        subtitles = subtitle_data.split("\n\n")
        
        if args.clean_type == "full":
            full_clean(file, subtitles)
        elif args.clean_type == "remove_font":
            remove_font(file, subtitles)

def full_clean(file, subtitles):
    cleaned_subtitles = []

    for subtitle in subtitles:
        subtitle_data = subtitle.split("\n")

        if len(subtitle_data) <= 2:
            continue

        subtitle_number, _, *content = subtitle_data
        content = "\n".join(content)

        content = remove_font_regex(content)
        cleaned_subtitles.append(f"{subtitle_number} {content}")

    cleaned_subtitles_string = "\n".join(cleaned_subtitles)

    with open(os.path.join("data", f"{file.removesuffix(".srt")}-cleaned-full.srt"), "w") as cleaned_file:
        cleaned_file.write(cleaned_subtitles_string)

def remove_font(file, subtitles):
    full_subtitles = "\n\n".join(subtitles)
    cleaned_subtitles = remove_font_regex(full_subtitles)

    with open(os.path.join("data", f"{file.removesuffix(".srt")}-cleaned-font.srt"), "w") as cleaned_file:
        cleaned_file.write(cleaned_subtitles)

def remove_font_regex(string):
    string = re.sub(r"<b><font [a-zA-Z0-9''=#]*>", "", string)
    return re.sub(r"</font></b>", "", string)
    

if __name__ == "__main__":
    main()
