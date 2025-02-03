from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time as t
import random

my_options=Options()
my_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=my_options)

def scrape_job_details(job_title1,job_location1):
    try:
        driver.get('https://in.indeed.com/?r=us')
        t.sleep(10)
        
        job_title=driver.find_element(By.NAME,'q')
        job_title.send_keys(job_title1)

        job_location=driver.find_element(By.NAME,'l')
        job_location.send_keys(job_location1)
        
        driver.find_element(By.XPATH,'//*[@id="jobsearch"]/div/div[2]/button').click()

        job_titles=driver.find_elements(By.CSS_SELECTOR,'a.jcs-JobTitle span')
        job_title_list=[]
        print()
        for title in job_titles:
            job_title_list.append(title.text)
        
        job_locations=driver.find_elements(By.CSS_SELECTOR,'div.company_location div div.css-1restlb')
        job_location_list=[]
        print()
        for location in job_locations:
            job_location_list.append(location.text)
        
        company_names=driver.find_elements(By.CSS_SELECTOR,'div.company_location div div.css-1afmp4o span.css-1h7lukg')
        company_name_list=[]
        print()
        for name in company_names:
            company_name_list.append(name.text)
        
        salaries=driver.find_elements(By.CSS_SELECTOR,'div.css-qspwa8 ul.css-keyg3o li.css-u74ql7 div.salary-snippet-container div.css-18z4q2i')
        emp_salary_list1=[]
        print()
        for salary in salaries:
            emp_salary_list1.append(salary.text)
        
        emp_salary_list=[]
        for i in emp_salary_list1:
            if "₹" or "," or " a year" or " a month" or "From " in i:
                i = i.replace("₹",'')
                i = i.replace(",",'')
                i = i.replace(" a year",'')
                i = i.replace(" a month",'')
                i = i.replace("From ",'')
                emp_salary_list.append(i)
        
        emp_list=[]
        for i in range(len(emp_salary_list)):
            emp_list.append({
                f"Job {i+1}": {
                    "Job title": job_title_list[i],
                    "Job location": job_location_list[i],
                    "Company Name": company_name_list[i],
                    "Salary": emp_salary_list[i]
                }
            })
        
        selected_job=random.choice(emp_list)
        
        print(selected_job['Job 10']['Salary'])
        
        driver.close()
        
    except ConnectionError:
        print("Internet is not available!")

