import streamlit as st

# maths times table creator

#variables
totalrows=20 # max number to times with the table e.g 2 times tablr up to 20 x 2
tables=(3,7,9,13) # times tables you want to create

st.title('times tables')
# loop each of tye times tables
for table in tables:
    heading=("%d times table" % (table))
    seperator= "-" * len(heading)
    #st.text("%d times table" % (table))
    #("\n\n")
    st.text(seperator)
    st.text(heading)
    st.text(seperator)
    # print out rows forbthis times table
    for n in range(1, totalrows+1):
      answer=table * n
      st.text("%d x %d = %d" % (table,n,answer))
      #st.text("answer")
