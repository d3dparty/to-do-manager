import os
import time

class ToDoManager():
    def __init__(self):
        self.notasks = True
        self.nofiltertasks = True
        self.nocompletetasks = True
        self.menuFlag = 0
        self.taskText = []
        self.taskPriority = []
        self.taskComplete = []
    def config(self):
        try:                                                        
            f = open("data.txt", 'r')
        except FileNotFoundError as err:
            f = open("data.txt", 'w')
        finally:
            f.close()
    def start(self):
        f = open("data.txt", 'r')
        inputstring = f.readline()
        if inputstring != "":
            self.notasks = False
            temp = ""
            while inputstring != "":
                self.taskPriority.append(int(inputstring[0]))
                self.taskComplete.append(int(inputstring[2]))
                for i in range(4, len(inputstring)):                
                    if inputstring[i] != '\n':
                        temp += str(inputstring[i])
                self.taskText.append(temp)
                temp = ""
                inputstring = f.readline()
        del inputstring
        self.menu()
    def menu(self):
        os.system("cls")

        print("================  Менеджер задач  ================", '\n')
        print("Выберите действие:")
        print("1. Список задач")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выход", '\n')

        self.menuFlag = int(input())
        print()

        if self.menuFlag == 1:
            self.viewTasks()
        elif self.menuFlag == 2:
            self.addTask()
        elif self.menuFlag == 3:
            self.deleteTask()
        elif self.menuFlag == 4:
            self.exit()
        else:
            print("Неверный пункт, попробуйте снова")
            time.sleep(3)
            self.menu()
        
    def viewTasks(self):
        os.system("cls")
        print("================  Менеджер задач  ================", '\n')
        if self.notasks == False:
            print("Задачи:")
            for i in range(0, len(self.taskText)):
                print(self.taskText[i])
                if self.taskPriority[i] == 0:
                    print("Приоритет: отсутствует")
                elif self.taskPriority[i] == 1:
                    print("Приоритет: низкий")
                elif self.taskPriority[i] == 2:
                    print("Приоритет: средний")
                elif self.taskPriority[i] == 3:
                    print("Приоритет: высокий")
                
                if self.taskComplete[i] == 1:
                    print("Выполнено!")
                print()
            
            print("Выберите действие:")
            print("1. Фильтр")
            print("2. Отметить как выполненное")
            print("0. Назад", '\n')

            self.menuFlag = int(input())
            print()

            if self.menuFlag == 1:
                self.filter()
            if self.menuFlag == 2:
                self.complete()
            elif self.menuFlag == 0:
                self.menu()
            else:
                print("Неверный пункт, попробуйте снова")
                time.sleep(3)
                self.viewTasks()
        else:
            print("Задач нет!")
            time.sleep(3)
            self.menu()
    def filter(self):
        os.system("cls")
        print("================  Менеджер задач  ================", '\n')
        print("Выберите фильтр:")
        print("1. Приоритет (нет)")
        print("2. Приоритет (низкий)")
        print("3. Приоритет (средний)")
        print("4. Приоритет (высокий)")
        print("5. Не выполнено")
        print("6. Выполнено")
        print("9. Назад")
        print("0. Меню", '\n')

        self.menuFlag = int(input())
        print()

        if self.menuFlag == 1:
            for i in range(0, len(self.taskText)):
                if self.taskPriority[i] == 0:
                    self.nofiltertasks = False
                    break
            if self.nofiltertasks == False:
                os.system("cls")
                print("================  Менеджер задач  ================", '\n')
                print("Задачи с отсутствующим приоритетом:", '\n')
                for i in range(0, len(self.taskText)):
                    if self.taskPriority[i] == 0:
                        print(self.taskText[i])
                print()
                print("Выберите действие:")
                print("1. Назад")
                print("0. Меню", '\n')

                self.menuFlag = int(input())
                print()

                if self.menuFlag == 1:
                    self.filter()
                elif self.menuFlag == 0:
                    self.menu()
                else:
                    print("Неверный пункт, попробуйте снова")
                    time.sleep(3)
                    self.filter()
            else:
                os.system("cls")
                print("================  Менеджер задач  ================", '\n')
                print("По выбранному фильтру задач нет!", '\n')
                print("Выберите действие:")
                print("1. Назад")
                print("0. Меню", '\n')

                self.menuFlag = int(input())
                print()

                if self.menuFlag == 1:
                    self.filter()
                if self.menuFlag == 0:
                    self.menu()
                else:
                    print("Неверный пункт, попробуйте снова")
                    time.sleep(3)
                    self.filter()
        elif self.menuFlag == 2:
            for i in range(0, len(self.taskText)):
                if self.taskPriority[i] == 1:
                    self.nofiltertasks = False
                    break
            if self.nofiltertasks == False:
                os.system("cls")
                print("================  Менеджер задач  ================", '\n')
                print("Задачи с низким приоритетом:", '\n')
                for i in range(0, len(self.taskText)):
                    if self.taskPriority[i] == 1:
                        print(self.taskText[i])
                print()
                print("Выберите действие:")
                print("1. Назад")
                print("0. Меню", '\n')

                self.menuFlag = int(input())
                print()

                if self.menuFlag == 1:
                    self.filter()
                elif self.menuFlag == 0:
                    self.menu()
                else:
                    print("Неверный пункт, попробуйте снова")
                    time.sleep(3)
                    self.filter()
            else:
                os.system("cls")
                print("================  Менеджер задач  ================", '\n')
                print("По выбранному фильтру задач нет!", '\n')
                print("Выберите действие:")
                print("1. Назад")
                print("0. Меню", '\n')

                self.menuFlag = int(input())
                print()

                if self.menuFlag == 1:
                    self.filter()
                if self.menuFlag == 0:
                    self.menu()
                else:
                    print("Неверный пункт, попробуйте снова")
                    time.sleep(3)
                    self.filter()
        elif self.menuFlag == 3:
            for i in range(0, len(self.taskText)):
                if self.taskPriority[i] == 2:
                    self.nofiltertasks = False
                    break
            if self.nofiltertasks == False:
                os.system("cls")
                print("================  Менеджер задач  ================", '\n')
                print("Задачи с средним приоритетом:", '\n')
                for i in range(0, len(self.taskText)):
                    if self.taskPriority[i] == 2:
                        print(self.taskText[i])
                print()
                print("Выберите действие:")
                print("1. Назад")
                print("0. Меню", '\n')

                self.menuFlag = int(input())
                print()

                if self.menuFlag == 1:
                    self.filter()
                elif self.menuFlag == 0:
                    self.menu()
                else:
                    print("Неверный пункт, попробуйте снова")
                    time.sleep(3)
                    self.filter()
            else:
                os.system("cls")
                print("================  Менеджер задач  ================", '\n')
                print("По выбранному фильтру задач нет!", '\n')
                print("Выберите действие:")
                print("1. Назад")
                print("0. Меню", '\n')

                self.menuFlag = int(input())
                print()

                if self.menuFlag == 1:
                    self.filter()
                if self.menuFlag == 0:
                    self.menu()
                else:
                    print("Неверный пункт, попробуйте снова")
                    time.sleep(3)
                    self.filter()
        elif self.menuFlag == 4:
            for i in range(0, len(self.taskText)):
                if self.taskPriority[i] == 3:
                    self.nofiltertasks = False
                    break
            if self.nofiltertasks == False:
                os.system("cls")
                print("================  Менеджер задач  ================", '\n')
                print("Задачи с высоким приоритетом:", '\n')
                for i in range(0, len(self.taskText)):
                    if self.taskPriority[i] == 3:
                        print(self.taskText[i])
                print()
                print("Выберите действие:")
                print("1. Назад")
                print("0. Меню", '\n')

                self.menuFlag = int(input())
                print()

                if self.menuFlag == 1:
                    self.filter()
                elif self.menuFlag == 0:
                    self.menu()
                else:
                    print("Неверный пункт, попробуйте снова")
                    time.sleep(3)
                    self.filter()
            else:
                os.system("cls")
                print("================  Менеджер задач  ================", '\n')
                print("По выбранному фильтру задач нет!", '\n')
                print("Выберите действие:")
                print("1. Назад")
                print("0. Меню", '\n')

                self.menuFlag = int(input())
                print()

                if self.menuFlag == 1:
                    self.filter()
                if self.menuFlag == 0:
                    self.menu()
                else:
                    print("Неверный пункт, попробуйте снова")
                    time.sleep(3)
                    self.filter()
        elif self.menuFlag == 5:
            for i in range(0, len(self.taskText)):
                if self.taskComplete[i] == 0:
                    self.nofiltertasks = False
                    break
            if self.nofiltertasks == False:
                os.system("cls")
                print("================  Менеджер задач  ================", '\n')
                print("Не выполненные задачи:", '\n')
                for i in range(0, len(self.taskText)):
                    if self.taskComplete[i] == 0:
                        print(self.taskText[i])
                print()
                print("Выберите действие:")
                print("1. Назад")
                print("0. Меню", '\n')

                self.menuFlag = int(input())
                print()

                if self.menuFlag == 1:
                    self.filter()
                elif self.menuFlag == 0:
                    self.menu()
                else:
                    print("Неверный пункт, попробуйте снова")
                    time.sleep(3)
                    self.filter()
            else:
                os.system("cls")
                print("================  Менеджер задач  ================", '\n')
                print("По выбранному фильтру задач нет!", '\n')
                print("Выберите действие:")
                print("1. Назад")
                print("0. Меню", '\n')

                self.menuFlag = int(input())
                print()

                if self.menuFlag == 1:
                    self.filter()
                if self.menuFlag == 0:
                    self.menu()
                else:
                    print("Неверный пункт, попробуйте снова")
                    time.sleep(3)
                    self.filter()
        elif self.menuFlag == 6:
            for i in range(0, len(self.taskText)):
                if self.taskComplete[i] == 1:
                    self.nofiltertasks = False
                    break
            if self.nofiltertasks == False:
                os.system("cls")
                print("================  Менеджер задач  ================", '\n')
                print("Выполненные задачи:", '\n')
                for i in range(0, len(self.taskText)):
                    if self.taskComplete[i] == 1:
                        print(self.taskText[i])
                print()
                print("Выберите действие:")
                print("1. Назад")
                print("0. Меню", '\n')

                self.menuFlag = int(input())
                print()

                if self.menuFlag == 1:
                    self.filter()
                elif self.menuFlag == 0:
                    self.menu()
                else:
                    print("Неверный пункт, попробуйте снова")
                    time.sleep(3)
                    self.filter()
            else:
                os.system("cls")
                print("================  Менеджер задач  ================", '\n')
                print("По выбранному фильтру задач нет!", '\n')
                print("Выберите действие:")
                print("1. Назад")
                print("0. Меню", '\n')

                self.menuFlag = int(input())
                print()

                if self.menuFlag == 1:
                    self.filter()
                if self.menuFlag == 0:
                    self.menu()
                else:
                    print("Неверный пункт, попробуйте снова")
                    time.sleep(3)
                    self.filter()
        elif self.menuFlag == 9:
            self.viewTasks()
        elif self.menuFlag == 0:
            self.menu()
        else:
            print("Неверный пункт, попробуйте снова")
            time.sleep(3)
            self.filter()
    def complete(self):
        os.system("cls")
        print("================  Менеджер задач  ================", '\n')
        for i in range(0, len(self.taskText)):
            if self.taskComplete[i] == 0:
                self.nocompletetasks = False
        if self.nocompletetasks == False:
            print("Задачи:")
            for i in range(0, len(self.taskText)):
                if self.taskComplete[i] == 0:
                    print(str(i+1)+".", self.taskText[i])
            self.menuFlag = int(input("\nВыберите задачу, чтобы отметить её как выполненную (0 - Назад): "))
            if self.menuFlag == 0:
                self.viewTasks()
            else:
                self.taskComplete[self.menuFlag-1] = 1
        
                print()
                print("Задача выполнена!")
                time.sleep(3)
                self.viewTasks()
        else:
            print("Все задачи выполнены!")
            time.sleep(3)
            self.viewTasks()
    def addTask(self):
        os.system("cls")
        print("================  Менеджер задач  ================", '\n')
        temp = input("Введите текст задачи: ")
        self.taskText.append(str(temp))
        temp = input("Введите приоритет задачи (0 - отсутствует, по шкале 1-3): ")
        temp = int(temp)
        self.taskPriority.append(int(temp))
        self.taskComplete.append(0)
        self.notasks = False

        print()
        print("Задача добавлена!")
        time.sleep(2)
        
        del temp
        self.menu()
    def deleteTask(self):
        os.system("cls")
        print("================  Менеджер задач  ================", '\n')
        if self.notasks == True:
            print("Нет задач!")
            time.sleep(3)
            self.menu()
        else:
            print("Задачи:")
            for i in range (0, len(self.taskText)):
                print(str(i+1)+".", self.taskText[i])
            self.menuFlag = int(input("\nВыберите задачу для удаления (0 - Назад): "))
            if int(self.menuFlag) == 0:
                self.menu()
            else:
                self.taskText.pop(self.menuFlag-1)
                self.taskPriority.pop(self.menuFlag-1)
                self.taskComplete.pop(self.menuFlag-1)
                print()
                print("Задача удалена!")
                time.sleep(3)
                self.menu()
    def exit(self):
        os.system("cls")
        print("Выход...")

        f = open("data.txt", 'w')

        for i in range(0, len(self.taskText)):
            temp = str(self.taskPriority[i]) + " " + str(self.taskComplete[i]) + " " + self.taskText[i] + "\n"
            f.write(str(temp))
        
        f.close()

td = ToDoManager()

td.config()
td.start()