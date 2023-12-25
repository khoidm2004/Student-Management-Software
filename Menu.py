from Logic import Logic

class Menu:
    def __init__(self) -> None:
        self.Logic = Logic()

    def display_menu(self)->None:
        while True:
            print("""You may select one the following:
                1) Add student
                2) Search student
                3) Add course 
                4) Search course 
                0) Exit
What is your selection?""")
            try:
                self.selection = int(input("Your selection: "))
                print()
                if self.selection not in [0,1,2,3,4,5]:
                    raise ValueError("Unknown selection.")
                elif self.selection == 0:
                    print("Exiting...")
                    break
                elif self.selection == 1:
                    self.Logic.insert_student_data()
                elif self.selection == 2:
                    self.Logic.display_student_info()
                elif self.selection == 3:
                    self.Logic.insert_course_data()
                elif self.selection == 4:
                    self.Logic.display_course_info()
            except ValueError:
                print("Unknown selection. Try again.")
                print()