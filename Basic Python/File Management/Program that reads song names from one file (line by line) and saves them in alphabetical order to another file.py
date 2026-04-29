import os

def read_line_by_line(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()


def save_content_alphabetically(lines, output_path):
    cleaned_lines = []

    for line in lines:
        cleaned_lines.append(line.strip())

    cleaned_lines.sort(key=str.lower)

    with open(output_path, 'w', encoding='utf-8') as file:
        for line in cleaned_lines:
            file.write(line + "\n")
            print(line)

def main():
    base_path = os.path.dirname(__file__)

    input_file = os.path.join(base_path, "songs.txt")
    output_file = os.path.join(base_path, "sorted_songs.txt")

    print("Looking for file at:", input_file)
    print("File exists?", os.path.exists(input_file))

    song_read = read_line_by_line(input_file)
    save_content_alphabetically(song_read, output_file)

    print("Songs have been sorted and saved successfully.")
    

if __name__ == "__main__":
    main()