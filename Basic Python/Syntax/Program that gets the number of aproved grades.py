
note_counter = 1
passed_grades_count = 0
average_passed_grades = 0
average_failed_grades = 0
failed_grades_count = 0
average_total_grades = 0

total_notes = int(input("Ingrese la cantidad de notas: "))  

while note_counter <= total_notes:
    current_grade = float(input(f"Ingrese la nota número {note_counter}: "))
    if current_grade < 70:
        failed_grades_count += 1
        average_failed_grades += current_grade
    else:	
        passed_grades_count  += 1
        average_passed_grades += current_grade
    average_total_grades += current_grade
    note_counter += 1
	
if failed_grades_count > 0:
    average_failed_grades /= failed_grades_count
else:
    print("No hay notas desaprobadas")

if passed_grades_count > 0:
    average_passed_grades /= passed_grades_count
else:
    print("No hay notas aprobadas")
	
average_total_grades /= total_notes

print(f"El estudiante tiene esta cantidad de notas aprobadas: {passed_grades_count}")
print(f"El estudiante tiene esta cantidad de notas desaprobadas: {failed_grades_count}")

if passed_grades_count > 0:
    print(f"Promedio de notas aprobadas: {average_passed_grades}")

if failed_grades_count > 0:
    print(f"Promedio de notas desaprobadas: {average_failed_grades}")
print(f"Este es el promedio total de notas: {average_total_grades}")
