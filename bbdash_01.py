import streamlit as st
import pandas as pd
import plotly.express as px

# df = pd.DataFrame(px.data.gapminder())
#  clist = df['country'].unique()
#country = st.sidebar.selectbox("Select a country:", clist)

df = pd.read_csv('Rock_City_FY2022_Budget_Data.csv')

#format amount


deptlist = df['dept_name'].unique()
#epartment = st.selectbox("Select a department:", deptlist, index=0)

#create by department list
#df_group_dept = df.groupby(deptlist)
# df_group_dept = df.sort_values(by=['amount'], ascending=False )
df_dept = df[['dept_name', 'amount']]
df_dept_sum = df_dept.groupby(['dept_name']).sum(['amount'])
df_dept_sum = df_dept_sum.sort_values(by='amount', ascending=False)



#Create by fund list
df_fund = df[['fund_name', 'amount']]
df_fund_sum = df_fund.groupby(['fund_name']).sum(['amount'])
df_fund_sum = df_fund_sum.sort_values(by='amount', ascending=False)

#creatte for by fund
#format inot currency
#show all the rows


#create the choice picklist
# Using object notation

choice = st.sidebar.selectbox("Select your view:", ("By department", "By fund"), index=0)

#selecting
if (choice == "By department"):
    # display the data for the department choice
    st.header("By Department")

    st.write("You selected department!!")
    st.dataframe(df_dept_sum, height = 700)  #need dataframe to stet height or width
    # Bart chart by all dpeartments- need plotly
    fig = px.bar(df_dept_sum, x="amount", orientation='h')
    st.write(fig)


else:
    st.header("By Fund")

    st.write("You selected fund!!")
    st.dataframe(df_fund_sum, height = 400)
    fig = px.bar(df_fund_sum, x="amount", orientation='h')
    st.write(fig)

#bar chart by one department



#group the data by dept
#df_group_dept = df.groupby(['dept_name']).sum()




#
#

# st.write(df_group_dept.columns)
#


# second version I am commiting