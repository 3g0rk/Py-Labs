from LAB1_Task1 import Library, Worker, Student

if __name__ == "__main__":
 # TODO: инстанцировать все описанные классы, создав три объекта.C()
 library = Library("Городская библиотека", 2)
 student = Student("Анна", 10, 3.5)
 worker = Worker("Иван", "Менеджер", 50000)

     # TODO: вызвать метод с некорректными аргументами(b)
try:
    library.add_book("Книга 1")
    library.add_book("Книга 2")
    library.add_book("Книга 3")
except ValueError:
         print('Ошибка: библиотека заполнена')

    # TODO: вызвать метод с некорректными аргументами(a)
try:
    student.update_gpa(6.0)
except ValueError:
         print('Ошибка: неправильные данные')
     # TODO: вызвать метод с некорректными аргументами(a)
try:
        worker.update_salary(-1000)  # Это вызовет ошибку
except ValueError:
    print('Ошибка: неправильные данные')
