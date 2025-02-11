from LAB1_Task1_Kobeliatskii import Library, Worker, Student

if __name__ == "__main__":
    library = Library("Городская библиотека", 2)
    student = Student("Анна", 10, 3.5)
    worker = Worker("Иван", "Менеджер", 50000)

    try:
        library.add_book("Книга 1")
        library.add_book("Книга 2")
        library.add_book("Книга 3")
    except ValueError:
        print('Ошибка: библиотека заполнена')

    try:
        student.update_gpa(6.0)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        worker.update_salary(-1000)  # Это вызовет ошибку
    except ValueError:
        print('Ошибка: неправильные данные')
