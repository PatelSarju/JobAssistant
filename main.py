import re
from extract_job_details import scrape_job_details

class JobAssistant:
    def get_user_preferences(self):
        self.location=input("Enter the job location at which you want to do job:").title()
        self.title=input("For which role you want to do job:").title()
        self.salary_range=input("Enter your expected salary range, (starting and ending salary write seperated by white space):")
        self.starting_salary=self.salary_range.split(' ')[0]
        self.ending_salary=self.salary_range.split(' ')[1]
    
    def validate_input(self):
        salary_pattern=r'^\d{1,3}(,\d{3})*\s\d{1,3}(,\d{3})*$'
        title_pattern=r'^[A-Za-z\s&-]+$'
        location_pattern=r'^[A-Za-z\s,]+$'
            
        if re.match(salary_pattern,self.salary_range):
            if re.match(title_pattern,self.title):
                if re.match(location_pattern,self.location):
                    scrape_job_details(self.title,self.location)
                else:
                    print("location is not accepted!")
            else:
                print("title is not accepted!")
        else:   
            print("salary is not accepted!")

if __name__=='__main__':
    job=JobAssistant()
    job.get_user_preferences()
    job.validate_input()