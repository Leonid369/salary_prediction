#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 01:12:46 2020

@author: saraswathishanmugamoorthy
"""

import pandas as pd
gs = pd.read_csv('glassdoor_jobs.csv')


# Removing rows that don't have salary estimates
gs = gs[gs['Salary Estimate'] != '-1']


#salary parsing
gs['hourly'] = gs['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
gs['employer_provided'] = gs['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)
salary = gs['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))
min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))
gs['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
gs['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
gs['avg_salary'] = (gs.min_salary+gs.max_salary)/2


#company name 
gs['company_txt'] = gs.apply(lambda x: x['Company Name'] if x['Rating']<1 else x['Company Name'][:-3], axis = 1)


#state field
gs['job_state'] = gs['Location'].apply(lambda x: x.split(',')[-1])
gs['same_state'] = gs.apply(lambda x: 1 if x.Location==x.Headquarters else 0, axis = 1)


#company age
gs['age'] = gs['Founded'].apply(lambda x: x if x<1 else 2020-x)

#parsing of job description (python etc)
gs['python_yn'] = gs['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
gs['R_yn'] = gs['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
gs['spark_yn'] = gs['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
gs['aws_yn'] = gs['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
gs['excel_yn'] = gs['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

gs_final = gs.drop(['Unnamed: 0'],axis=1)

gs_final.to_csv('cleaned_data.csv',index=False)