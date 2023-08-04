# coding=utf-8
"""
@project: Student Result System .py
@Author: Megan Li
@file: stusystem.py
@date: 2023-7-19 19:49
"""
import os.path
filename = 'student.txt'
format_title = '{:^6}\t{:^12}\t{:^8}\t{:^12}\t{:^12}\t{:^12}' # Printing format
def main():
    while True:
        menu()
        try:
            choice = int(input('Which operaiton would like to perform (e.g.key in 1 if you want to insert the information of a new student.)\n'))
        except :
            continue # Return to the menu if user doesn't key in the a number.
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input('Are you sure you wanna quit the system?y/n').lower()
                if answer == 'y':
                    print('Thank you for using the system. ')
                    break # Quit the system
                else:
                    continue # Return to the menu
            elif choice == 1:
                insert() # Insert student's information into the system
            elif choice == 2:
                search() # Search for the student from the database
            elif choice == 3:
                delete() # Delete the student information from the database
            elif choice == 4:
                modify() # Edit the student's information
            elif choice == 5:
                sort() # Print student's result in order based on the chosen criteria
            elif choice == 6:
                total() # Get the total score of a student
            elif choice == 7:
                show() # Show all the student information

def insert():
    student_list = []
    while True:
        id = input('Please enter student\'s ID (e.g.1001):')
        if not id:  # If ID is not empty continue the program
            pass
        name = input('Please enter the name of the student: ')
        if not name:  # If name is not empty continue on the program
            pass
        try:
            eng_score = int(input('Please enter the result of English subject: '))
            python = int(input('Please enter the result of Python subject: '))
            java = int(input('Plese enter the result of Java subject: '))
        except:
            print('The score of the subject must be integer...')
            continue
        # Save the information of the student into a dictionary
        student = {'id': id, 'name': name, 'eng_score': eng_score, 'python': python, 'java': java}
        # Add the information of the student to the list
        student_list.append(student)
        answer = input('Is there any student information you want to add in？y/n\n').lower()
        if answer == 'y':
            continue
        else:
            print('All the information have been saved into the database')
            save(student_list)
            return

def search():
    if os.path.exists(filename):
        while True:
            choice = int(input('Search by student ID, enter 1; Search by name, enter 2: \n'))
            ans_id = '' # Set the original ans_id to be empty
            ans_name='' # Set the original ans_name to be empty
            if choice == 1:
                ans_id = input('Please enter a student ID: \n')
            elif choice == 2:
                ans_name = input('Please enter a student name: \n')
            else:
                print('Please enter 1 or 2.')

            with open(filename, 'r', encoding='utf-8') as f:  # Get the datails from the database
                lines = f.readlines()
                for item in lines:
                    d = dict(eval(item))
                    if d['id'] == ans_id or d['name'] == ans_name:
                        print_item(d) # Print details by the designated format
                        break
                    else:
                        continue
            ans = input('Would you like to search other student info?y/n\n').lower()
            if ans == 'y':
                continue
            else:
                return
        else:
            print('There is no student information in the database.')

def print_item(item):
    '''
    The purpose of this function is to print the title in a designated format
    :param item: None
    :return: None
    '''
    print(format_title.format('ID', 'Name', 'English Score', 'Python score', 'Java Score','Total Score'))
    print(format_title.format(item['id'], item['name'], item['eng_score'], item['python'], item['java'],item['eng_score']+item['python']+item['java']))

def delete():
    new_student = []
    if os.path.exists(filename):
        while True:
            id = input('Please enter the student ID you want to delete: ')
            if id != '':
                with open(filename,'r',encoding = 'utf-8') as f:
                    lines = f.readlines()
                    for item in lines:
                        d = dict(eval(item))
                        if d.get('id') == id:
                            print(f'The student with student ID {id} have been removed.')
                            continue # If student id was found, skip this info
                        else:
                            new_student.append(d)
                    if len(new_student) ==len(lines): # If the number of student is the same as the number of student in database,the student id is not found
                        print(f'The student with student ID {id} does\' exist.')
                with open(filename, 'w',encoding='utf-8') as f:
                            for item in new_student:
                                f.write(str(item) + '\n')
            answer = input('Do you want to delete other student info?y/n').lower()
            if answer == 'y':
                continue
            else:
                break

def modify():
    while True:
        id = input('Please enter the student ID that you want to midify: \n')
        if id != '' and os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as rfile: # Obtain all the information from the database
                lines = rfile.readlines()
        else:
            print('The entered student id is not found.')
            break
        with open(filename, 'w', encoding='utf-8') as wfile:
            for item in lines:
                d = dict(eval(item))
                if d['id'] == id:
                    print('The information of student is found, you can modify his/her information now.')
                    d['name']  = input('Please enter student\'s name: ')
                    try:
                        d['eng_score'] = int(input('Please enter the English Result: '))
                        d['python'] = int(input('Please enter the Python result: '))
                        d['java'] = int(input('Please enter the Java result'))
                        wfile.write(str(d) + '\n')
                        print('The information of the student have been modified')
                    except:
                            print('The result of the subject shoule be a number.')
                else:
                    wfile.write(str(d) + '\n') # Restore the information of other student to the database
        answer = input('Still want to modify other student\'s information?y/n').lower()
        if answer == 'y':
            continue
        else:
            return

def sort():
    if os.path.exists(filename): # Obtain all the information from the database
        student = []
        with open(filename,'r',encoding='utf-8') as f:
            lines = f.readlines()
        for item in lines:
            d = dict(eval(item))
            student.append(d)
        patten = input('Enter 0 to sort student\'s information in ascending order, enter 1 for the descending order: ')
        if patten == '0':
            is_des = False
        elif patten =='1':
            is_des = True
        criteria = int(input('Choose the soring criteria(1.English result，2.Python result 3.Java result，0.Total score): '))
        if criteria == 1:
            student.sort(key=lambda x : x['eng_score'],reverse= is_des)
        elif criteria == 2:
            student.sort(key=lambda x: x['python'],reverse= is_des)
        elif criteria == 3:
            student.sort(key=lambda x:x['java'],reverse= is_des)
        elif criteria == 0:
            student.sort(key=lambda x:(x['java']+ int(x['python'])+ int(x['eng_score'])),reverse= is_des)
        else:
            print('Please enter the correct sorting criteria.')
            sort()
        format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}' # print format
        print(format_title.format('ID', 'Name', 'English Result', 'Python Result', 'Java Result', 'Total Score'))
        for i in student:
            print(format_title.format(i.get('id'),
                                      i.get('name'),
                                      i.get('eng_score'),
                                      i.get('python'),
                                      i.get('java'),
                                      i.get('java') + i.get('python') + i.get('eng_score')
                                      ))
    else:
        print('暂未保存信息')


def total():
    # Get the total number of student in the database
    if os.path.exists(filename):
        with open(filename) as f:
            lines = f.readlines()
            total = len(lines)
            if total == 0:
                print('There is no student information in the database.')
                total()
            print(f'There are {total} students in tatal.')
    else:
        print('There is no student information in the database.')

def show():
    if os.path.exists(filename):
        format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
        print(format_title.format('ID', 'Name', 'English Result', 'Python Result', 'Java Result', 'Total Score') +'\n')
        with open(filename,'r',encoding='utf-8') as f:
            lines = f.readlines()
            if lines:
                for item in lines:
                    item = dict(eval(item))
                    print(format_title.format(item.get('id'),
                                          item.get('name'),
                                          item.get('eng_score'),
                                          item.get('python'),
                                          item.get('java'),
                                          item.get('java') + item.get('python')+item.get('eng_score')
                                          ))
    else:
        print('There is no data in the database.')

def save(lst):
    with open(filename,'a', encoding= 'utf-8') as f:
        for item in lst:
            f.write(str(item) + '\n')


def menu():
    print('=' * 12 + 'Student Result System' + '=' * 12)
    print('-' * 12 + 'Menu' + '-' * 12)
    print('\t\t1. Insert the information of a new student')
    print('\t\t2.Search student\'s information')
    print('\t\t3.Delete student\'s information')
    print('\t\t4.Modify student\'s information')
    print('\t\t5.Sort the student based on the score')
    print('\t\t6.The total number of student')
    print('\t\t7.Show the information of all student')
    print('\t\t0.Exit the system')
    print('----------------------------------------------')



if __name__ == '__main__':
        main()