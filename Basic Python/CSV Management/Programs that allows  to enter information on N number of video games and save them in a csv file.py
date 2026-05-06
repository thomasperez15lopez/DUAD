import csv

Video_games_list = [
    {
        'Name': 'Grand Theft Auto IV',
        'Gender': 'Accion',
        'Developer': 'Rockstar Games',
        'ESRB_Rating': 'M',
    },
    {
        'Name': 'The Elder Scrolls IV: Oblivion',
        'Gender': 'RPG',
        'Developer': 'Bethesda',
        'ESRB_Rating': 'M',
    },
    {
        'Name': "Tony Hawk's Pro Skater 2",
        'Gender': 'Deportes',
        'Developer': 'Activision',
        'ESRB_Rating': 'T',
    }
]

video_games_headers = (
	'Name',
	'Gender',
	'Developer',
	'ESRB_Rating',
)

def write_csv_file(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, headers)
    writer.writeheader()
    writer.writerows(data)

def main():
    write_csv_file('convert to CSV.txt', Video_games_list, video_games_headers)
    print("File created successfully!")


if __name__ == "__main__":
    main()


