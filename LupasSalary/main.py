class Pupa:
  def __init__(self, name):
      self.name = name
      self.work_list = []

  def do_work(self, spisok1, spisok2):
      self.work_list = [x + y for x, y in zip(spisok1, spisok2)]
      print(f"{self.name} выполнил работу: {self.work_list}")

  def take_salary(self, bonus):
      salary = len(self.work_list) * bonus
      print(f"{self.name} получил зарплату: {salary}")
      return salary


class Lupa:
  def __init__(self, name):
      self.name = name
      self.work_list = []

  def do_work(self, spisok1, spisok2):
      self.work_list = [x - y for x, y in zip(spisok1, spisok2)]
      print(f"{self.name} выполнил работу: {self.work_list}")

  def take_salary(self, bonus):
      salary = len(self.work_list) * bonus
      print(f"{self.name} получил зарплату: {salary}")
      return salary


class Accountant:
  def give_salary(self, worker):
      bonus = float(input("Введите бонус: "))
      old_salary = getattr(worker, 'salary', 0)
      salary = old_salary + worker.take_salary(bonus)
      setattr(worker, 'salary', salary)
      return salary


if __name__ == "__main__":
  pupa = Pupa("Pupa")
  lupa = Lupa("Lupa")
  accountant = Accountant()

  while True:
      try:
          spisok1 = [int(x) for x in input("Введите первый список чисел для Pupa через пробел: ").split()]
          spisok2 = [int(x) for x in input("Введите второй список чисел для Pupa через пробел: ").split()]
          spisok3 = [int(x) for x in input("Введите первый список чисел для Lupa через пробел: ").split()]
          spisok4 = [int(x) for x in input("Введите второй список чисел для Lupa через пробел: ").split()]
      except ValueError:
          print("Введите корректные числа.")
          continue

      pupa.do_work(spisok1, spisok2)
      lupa.do_work(spisok3, spisok4)

      pupa_salary = accountant.give_salary(pupa)
      lupa_salary = accountant.give_salary(lupa)

      print(f"Итоговая зарплата Pupa: {pupa_salary}")
      print(f"Итоговая зарплата Lupa: {lupa_salary}")

      answer = input("Хотите еще посчитать зарплату? (да/нет): ").lower()
      if answer != 'да':
          break
