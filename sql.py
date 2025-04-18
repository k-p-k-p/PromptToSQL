from dotenv import load_dotenv
load_dotenv() ##load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
##genai api key configure
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load google gemini model
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

##function to retrierve query from the database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    try:
        cur.execute(sql)
    except sqlite3.Error as e:
        print(f"Error executing SQL: {e}")
    rows=cur.fetchall()
    print(f"Number of rows fetched: {len(rows)}")  # New print statement
    conn.close()
    return rows

##define your prompt
prompt=[
    """You are an expert in converting english questions into sql  code!
The sql database has the name student and the following columns->
name,class,section,marks\nFor example:\n
Example 1:\n
How many records are in the student table?\n
The sql query for the above example question 1 will be like:Select count(*) from student;\n
Example 2:
Tell me all the names of students studying in Data Science.
The sql query for the  above order is:
select name from student where class="data science";
also the sql code should not have ``` in the beginning or end and sql word in output
"""
]

##streamlit app
st.set_page_config(page_title="I can retrieve any sql query")
st.header("Gemini App to retrieve SQL Query")

question=st.text_input("Input :",key="input")
submit=st.button("Ask the Question")

##if subit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Response is:")
    for row in response:
        print(row)
        st.header(row)
    

   