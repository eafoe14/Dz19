import math

def speed():
      speedKmH = int(input("Введите скорость в км/ч"))
      speedKmS = speedKmH * (5/18)
      print(speedKmS)

def minimum():
      num1 = int(input("Введите первое число: "))
      num2 = int(input("Введите второе число: "))
      num3 = int(input("Введите третье число: "))
      if num2 >= num1 <= num3:
            print(num1)
      elif num1 >= num2 <= num3:
            print(num2)
      else:
            print(num3)

def exponentiation():
      a = 1
      stepen = int(input("Введите степень в которую будет переводиться число: "))
      number = int(input("Введите возводимое число: "))
      for i in range(stepen):
            a *= number
      print(a)

def recursion():
      print("a = 1:\n"
            "print(a)")
      recursion()

def factorial():
      n = int(input("Введите n: "))
      fact = 1
      for i in range(2, n+1):
            fact *= i
      print(fact)

def exponentiation2():
      chislo = int(input("Введите число"))
      step = int(input("Введите степень"))
      print(chislo^step)

def modul():
      numModul = int(input("Введите число"))
      print(abs(numModul))

def logarithm():
      osnovanie = int(input("Введите основание логарифма"))
      numLog = int(input("Введите значение логарифма"))
      print(math.log(osnovanie, numLog))

print("**********************************************************************************************************")
print("1 - Перевод км/ч в м/с\n"
      "2 - Наименьшее из трёх чисел\n"
      "3 - Возведение в степень\n"
      "4 - Бесконечно пишет какой-то код в терминал\n"
      "5 - Лямба-функция возведения суммы(разности) 2-ух чисел в куб\n"
      "6 - Расчёт факториала\n"
      "7 - Возведение в степень"
      "8 - Модуль"
      "9 - Логарифм(основание тоже вводится)\n"
      "10 - Расчёт процентного соотношения\n"
      "11 - Выход из программы")
print("**********************************************************************************************************")

option = 0
while option != 11:
      option = int(input("Выберите действие: "))
      if option == 1:
            speed()
      elif option == 2:
            minimum()
      elif option == 3:
            exponentiation()
      elif option == 4:
            recursion()
      elif option == 5:
            print()
      elif option == 6:
            factorial()
      elif option == 7:
            exponentiation2()
      elif option == 8:
            modul()
      elif option == 9:
            logarithm()
      elif option == 10:
            print("Не понял как сделать")
      else:
            print("Вы покинули программу")