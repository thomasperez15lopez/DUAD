def students_information():
    list_of_students = []
    number_of_students = int(input("Let me know the amount of students: "))
    print("Please provide the following information for each student")

    for student in range(number_of_students):
        while True:
            try:
                name = input("Student full name: ")
                section = input("Section: ")
                english_note = float(input("Enter the English note: "))
                social_note = float(input("Enter the Social note: "))
                science_note = float(input("Enter the Science note: "))
                spanish_note = float(input("Enter the Spanish note: "))

                if not all(0 <= grade <= 100 for grade in [english_note, social_note, science_note, spanish_note]):
                    print("Grades must be between 0 and 100")
                    continue
                break

            except ValueError as e:
                print(f"Invalid note, please try again. Details: {e}")

        list_of_students.append ({
            "name": name,
            "section": section,
            "spanish": spanish_note,
            "english": english_note,
            "social": social_note,
            "science": science_note
        })
    return list_of_students


def menu_information():
    while True:
        print("Choose one of the following options:")
        print("1. view information for all incoming students")
        print("2. see the top 3 students with the best average grade")
        print("3. View each student's average grade")
        print("4. export all current data to a CSV file")
        print("5. import all current data from a previously exported CSV file")
    
        try:
            option =  int(input( "enter number a number from 1-5: "))
        except ValueError as e:
            print(f"Invalid number, please try again. Details: {e}")
            continue

        if option not in [1,2,3,4,5]:
            print(f"Entered number {option} is not in the range 1-5. Please try again")
            continue
        else:
            break
    return option


def view_incoming_students(list_of_students):
    print("These are all registered students: ")

    for student in list_of_students:
        print(student)


def best_average_grade(list_of_students):
    average_list = []

    for value in list_of_students:
        each_average_grade = ( 
            value["english"] +
            value["social"] +
            value["science"] +
            value["spanish"]
        ) / 4

        average_list.append({
            "name": value["name"],
            "average": each_average_grade
        })

    return sorted(average_list, key=lambda student: student["average"],
        reverse=True)


def view_each_average_grade(each_average_list):

    for student in each_average_list:
        print(f"This is the average grade for {student['name']}: {student['average']} ")


def save_data_to_a_CSV_file(input_path, student_data):
    import csv
    
    content_headers = (
	'name',
	'section',
	'spanish',
	'english',
    'social',
    'science',
    )

    with open(input_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=content_headers)
        writer.writeheader()
        writer.writerows(student_data)  

def import_data_from_CSV_file(input_path):
    import csv

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        for student in data:
            student["spanish"] = float(student["spanish"])
            student["english"] = float(student["english"])
            student["social"] = float(student["social"])
            student["science"] = float(student["science"])

        return data

    except FileNotFoundError:
        print("No previously exported CSV file was found.")
        return []
    

def main():

    user_option = menu_information()
    file_path = "students.csv"

    if user_option == 5:
        imported_students = import_data_from_CSV_file(file_path)

        if imported_students:
            print("Data imported successfully.")
            view_incoming_students(imported_students)

    else:
        list_of_students = students_information()
        best_average_list = best_average_grade(list_of_students)

    if user_option == 1:
        view_incoming_students(list_of_students)
    elif user_option == 2:
        print("These are the top 3 students with the best average grade:")
        for student in best_average_list[:3]:
            print(f"{student['name']}: {student['average']}")
    elif user_option == 3:
        view_each_average_grade(best_average_list)
    elif user_option == 4:
        save_data_to_a_CSV_file(file_path, list_of_students)
        print("Data exported successfully.")


if __name__ == "__main__":
    main()


