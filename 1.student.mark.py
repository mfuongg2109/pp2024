def input_numStudent():
    num = input("Enter number of students:")
    if num == "exit":
        return
    elif num.isdigit() and int(num) > 0:
        return num
    else:
        print("the input number is not natural")

def input_numCourse():
    num = input("Enter number of courses:")
    if num == "exit":
        return
    elif num.isdigit() and int(num) > 0:
        return num
    else:
        print("the input number is not natural")


def input_student(numStudent):
    student_data = []
    for i in range(numStudent):
        stu_id = str(input("Enter id of student "))
        stu_name = str(input("\nEnter name of student"))
        dob = str(input("\n Enter student's dob (YYYY-MM-DD):"))
        student_data.append({"id":stu_id,"name":stu_name,"dob":dob,"marks" : {}})
    return student_data


def input_course(numCourse):
    course_data = []
    for i in range(numCourse): 
        course_id = str(input("Enter course id:"))
        course_name = str(input("\n Enter course name:"))
        course_data.append({"id":course_id,"name":course_name})
    return course_data

def input_marks(course_data, student_data):
    entered_course = input("Enter course id you want to input marks:")
    
    for i in range(len(course_data)):
        if entered_course == course_data[i]["id"]:
            for j in range(len(student_data)):
                mark = int(input(f"Input mark for {student_data[j]['name']} in the course {course_data[i]['name']}: "))
                student_data[j]['marks'][course_data[i]['id']] = mark
        else:
            print("Course not found.")

def listing_student(student_data):
    for i in range(len(student_data)):
        print(student_data[i])
        
def listing_course(course_data):
    for i in range(len(course_data)):
        print(course_data[i])






num_student = int(input_numStudent())            
num_course = int(input_numCourse())

student_data = input_student(num_student)
course_data = input_course(num_course)

while True:
    print("1 Listing students:")    
    print("2 Listing courses:")    
    print("3 Input marks:")
    print("4 Exit")
    print("Select option(1,2,3,4):")
    user_option = input()
    if user_option.isdigit():
        if int(user_option) == 4:
            break
        
        elif int(user_option) == 3:
            input_marks(course_data,student_data)

        elif int(user_option) == 2:
            listing_course(course_data)
            
        elif int(user_option) == 1:
            listing_student(student_data)
            
        else:
            print("Enter your selection again")

    else:
        print("Enter your selection again")

    
    

    