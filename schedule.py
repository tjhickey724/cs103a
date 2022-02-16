'''
schedule.py contains helper files for analyzing the Brandeis courses from 2004-2021
'''

import csv
import matplotlib.pyplot as plt
import numpy as np

class Schedule():
    '''
        Schedule is a class representing all of the Brandeis courses from 2004-2021
        with info about the instructor and enrollment
    '''
    
    def __init__(self):
        ''' creating a Courses object loads the dataset from a csv file '''
        with open("data/courses.csv",'r') as csvfile:
            reader = csv.DictReader(csvfile)
            self.courses = [row for row in reader]
            csvfile.close()
        self.clean_data() # make the data easier to manipulate, e.g. convert enrollments to integer from string
        self.codes = sorted({c['code'] for c in self.courses})
        self.terms = [self.code_to_term(code) for code in self.codes]




    def code_to_term(self,code):
        ''' convert a code to a term, 

             e.g. 1083 -> "Fall 2008", 1211 -> "Spring 2021" 
             the middle two digits give the last two digits of the year
             the last digit is 1 for Spring, 2 for Summer, 3 for Fall
             the first digit is always 1
        '''
        year = "20"+code[1:-1]
        semester = code[-1]
        assert semester in "123", 'semester should be 1,2, or 3'  # assert CONDITION, MESSAGE is a sanity check feature of Python
        if semester=="1":
            return "Spring "+year
        elif semester=="2":
            return "Summer "+year
        else:
            return "Fall "+year


    def clean_data(self):
        for c in self.courses:
            c['enr']=int(c['enr'])


    def enrolled_in_term(self,code):
        ''' returns the number of students enrolled in courses in the specified term (using the code) '''
        return sum([c['enr'] for c in self.courses if c['code']==code])
    
    def enrolled_by_term(self):
        ''' returns the number of students enrolled at Brandeis by term for each term in the dataset'''
        return [self.enrolled_in_term(code) for code in self.codes]
    
    def plot_enrollment_by_term(self):
        plt.figure(figsize=(20,15))
        plt.barh(self.terms,self.enrolled_by_term())
        plt.title("Enrollment by Term",fontsize=24)

    def enrolled_in_term_by_condition(self,condition,code):
        ''' returns the number of students enrolled in the specified term satisfying the condition '''
        return sum([c['enr'] for c in self.courses if c['code']==code and condition(c)])
    
    def enrolled_by_condition(self,condition):
        '''  returns the number of students enrolled in each term in courses satisfying the condition '''
        return [self.enrolled_in_term_by_condition(condition,code) for code in self.codes]
    
    def plot_enrolled_by_condition(self,title,condition):
        plt.figure(figsize=(20,15))
        plt.barh(self.terms,self.enrolled_by_condition(condition))
        plt.title(title,fontsize=24)




