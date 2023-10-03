import streamlit as st
import mysql.connector as mycon
#establish connection
db = mycon.connect(
    host = "localhost", user="root", password="root",database='pydb'
)
db_curr = db.cursor()
#GUI
st.header("CRUD Operation")
tab1, tab2, tab3 = st.tabs (['Insert', 'Update', 'Delete'])
with tab1:
    no = st.text_input('Enter Product number: ')
    name = st.text_input("Enter Product Name: ")
    loc = st.text_input("Enter Location: ")

    if st.button("Submit"):
        sql = "insert into dmart (pro_no,pro_name,pro_loc) values (%s ,%s ,%s)"
        val = (no,name,loc)
        db_curr.execute(sql,val)
        db.commit()
        db_curr.execute('Select * from dmart')
        st.table(db_curr.fetchall())
with tab2:
    no = st.text_input(' Product number: ')
    name = st.text_input(" Product Name: ")
    loc = st.text_input(" Location: ")

    if st.button("Update"):
        sql = "UPDATE dmart SET pro_name = %s, pro_loc = %s WHERE pro_no = %s"
        val = (name, loc, no)
        db_curr.execute(sql,val)
        db.commit()
        db_curr.execute('Select * from dmart')
        st.table(db_curr.fetchall()) 
with tab3:
    db_curr.execute("Select *from dmart")
    st.table(db_curr.fetchall())
    no = st.text_input("Product no you want to Delete")
    if st.button("Delete"):
        sql = "DELETE FROM dmart WHERE pro_no = %s"
        val = (no,)
        db_curr.execute(sql,val)
        db.commit()
        db_curr.execute('Select * from dmart')
        st.table(db_curr.fetchall())