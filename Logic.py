from db_conn import DB_CONN, DB_CONN1
import random

class Logic:
    def __init__(self) -> None:
        pass

    # Function 1: Add student to the database
    def add_student(self)->tuple:
        print("Names should contain only letters and start with capital letters.")
        while True:
            try:
                fname = input("Enter the first name of the student:\n")   
                lname = input("\nEnter the last name of the student:\n")
                if fname.isalpha() and fname[0].isupper() and lname.isalpha() and lname[0].isupper():
                    student_name = f"{fname} {lname}"
                    break
                else:
                    raise ValueError("Names should contain only letters and start with capital letters.")
            except ValueError as error:
                print(error)
                print()

        while True:
            try:
                print("""\nSelect student's major:
                            CE: Computational Engineering
                            EE: Electrical Engineering
                            ET: Energy Technology
                            ME: Mechanical Engineering
                            SE: Software Engineering""")
                major = input("What is your selection?\n").upper()
                print()
                option = ["CE","EE","ET","ME","SE"]
                if major in option:
                    break
                else:
                    raise ValueError("Unknown major. Please try again")
            except ValueError as error:
                print(error)
        
        while True:
            student_id = random.randint(100000,999999)
            checking_student_id = self.check_student_id(student_id)
            if checking_student_id == False:
                print(f"Student ID: {student_id}")
                print()
                break
            else:
                pass

        Student_info = self.insert_keyboard(student_id,student_name,major)
        return Student_info

    def insert_keyboard(self,id,name,optional_content)->tuple:
        insert_obj = (id,name,optional_content)
        return insert_obj
    
    def insert_student_data(self)->None:
        cursor = DB_CONN.cursor()
        INSERT_STATEMENT = ("INSERT INTO SM (id,name,major) VALUES(?,?,?)")
        obj = self.add_student()
        cursor.execute(INSERT_STATEMENT,obj)
        DB_CONN.commit()
        cursor.close()
    
    def check_student_id(self,student_id)->bool:
        cursor = DB_CONN.cursor()
        STUDENT_ID_CHECKING_STATEMENT = ("SELECT * FROM SM WHERE id = ? ")
        cursor.execute(STUDENT_ID_CHECKING_STATEMENT,(student_id,))
        result = cursor.fetchone()
        DB_CONN.commit()
        cursor.close()

        if result:
            return True # Existed
        else:
            return False # Not exist

    # Function 2: Search student from database by id
    def get_student_info(self)->list:
        search_id = int(input("Enter the student id number: "))
        cursor = DB_CONN.cursor()
        GET_STUDENT_INFO_STATEMENT = """SELECT * FROM SM
        WHERE id = ?;
        """ 
        cursor.execute(GET_STUDENT_INFO_STATEMENT,(search_id,))
        student_info = cursor.fetchall()
        DB_CONN.commit()
        cursor.close()

        if student_info:
            return student_info
        else:
            return None
    
    def display_student_info(self)->None:
        rawData = self.get_student_info()
        if rawData:
            print("STUDENTS INFO:")
            for i in rawData:
                print(f"id: {i[0]} Name: {i[1]} Major: {i[2]}")
                print()
        else:
            print("Student does not exist.")
            print()

    # Function 3: Add course
    def add_course(self)->tuple:
        print("Course names should contain only letters and start with the capital letters.")
        while True:
            try:
                course_name = input("Enter the course name:\n")
                if course_name.replace(" ","").isalpha() and course_name.istitle():
                  print()
                  break
                else:
                    raise ValueError("Course names should contain only letters and start with capital letters.")
            except ValueError as error:
                print(error)
                print()
        
        print("Names should contain only letters and start with capital letters.")

        while True:
            try:
                teacher = input("Enter the name of the teacher:\n")
                if teacher.replace(" ","").isalpha() and teacher.istitle():
                    print()
                    break
                else:
                    raise ValueError("Teacher names should contain only letters and start with capital letters.")
            except ValueError as error:
                print(error)
                print()
    

            # Course ID example A0490
        while True:
            Fcharacter = random.randint(65,90) 
            course_id_Fcharcter = chr(Fcharacter)
            Nchatracter = random.randint(100,999)
            course_id = f"{course_id_Fcharcter}0{Nchatracter}"
            checking_course_id = self.check_course_id(course_id)
            if checking_course_id == False:
                print(f"Course ID: {course_id}")
                print()
                break
            else:
                pass
        
        Course_info = self.insert_keyboard(course_id,course_name,teacher)
        return Course_info


    def insert_course_data(self)->None:
        cursor1 = DB_CONN1.cursor()
        INSERT_STATEMENT = ("INSERT INTO CM (id,name,teacher) VALUES(?,?,?)")
        obj = self.add_course()
        cursor1.execute(INSERT_STATEMENT,obj)
        DB_CONN1.commit()
        cursor1.close()

    def check_course_id(self,course_id)->bool:
        cursor1 =DB_CONN1.cursor()
        COURSE_ID_CHECKING_STATEMENT = ("SELECT * FROM CM WHERE id = ? ")
        cursor1.execute(COURSE_ID_CHECKING_STATEMENT,(course_id,))
        result1 = cursor1.fetchone()
        DB_CONN1.commit()
        cursor1.close()

        if result1:
            return True # Existed
        else:
            return False # Not exist

    # Function 4: Search course
    def get_course_info(self)->list:
        search_term = input("Give the name of the course:\n")
        cursor1 = DB_CONN1.cursor()
        GET_COURSE_INFO_STATEMENT = """SELECT * FROM CM
        WHERE name=?;
        """
        cursor1.execute(GET_COURSE_INFO_STATEMENT,(search_term,))
        course_info = cursor1.fetchall()
        
        if course_info:
            return course_info
        else:
            return None

    def display_course_info(self)->None:
        rawData1 = self.get_course_info()
        if rawData1:
            for i in rawData1:
                print(f"ID: {i[0]}, Name: {i[1]}, Teacher: {i[2]}")
        else:
            print("Course not found.")
            print()


