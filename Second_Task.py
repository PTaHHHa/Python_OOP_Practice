"""Напишите программу по следующему описанию:
Есть класс Person, конструктор которого принимает три параметра (не учитывая self) – имя,
фамилию и квалификацию специалиста.
Квалификация имеет значение заданное по умолчанию, равное единице.

У класса Person есть метод, который возвращает строку, включающую в себя всю информацию о сотруднике.
Класс Person содержит деструктор, который выводит на экран фразу "До свидания, мистер …"
(вместо троеточия должны выводиться имя и фамилия объекта).

В основной ветке программы создайте три объекта класса Person.
Посмотрите информацию о сотрудниках и увольте самое слабое звено."""


class Person:
    def __init__(self, first_name, last_name, qualification=1):
        self.first_name = first_name
        self.last_name = last_name
        self.qualification = qualification

    def __str__(self):
        return self.first_name + " " + self.last_name + "--> " + str(self.qualification)

    def __del__(self):
        print(f"\nGoodbye Mr.{self.last_name}")


person1 = Person("John", "Malkovic", 8)
print(person1.__str__())
person2 = Person("Douglas", "MacArthur", 4)
print(person2.__str__())
person3 = Person("Gabe", "Newell", 5)
print(person3.__str__())
person4 = Person("Richie", "Salieri")
print(person4.__str__())

persons_list = []
for qual in person1.qualification, person2.qualification, person3.qualification, person4.qualification:
    persons_list.append(qual)
min_qualification = min(persons_list)
print(min_qualification)
for person in person1, person2, person3, person4:
    if person.qualification == min_qualification:
        person.__del__()
        break

