import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode # better tables in Streamlit


# df = pd.DataFrame(px.data.gapminder())
#  clist = df['country'].unique()
#country = st.sidebar.selectbox("Select a country:", clist)

df = pd.read_csv('Rock_City_FY2022_Budget_Data.csv')




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

#creating a batter table view of the data set using aggrid
#put df into Agrid format
#AgGrid(df)
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar() #Add a sidebar
gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gridOptions = gb.build()

grid_response = AgGrid(
    df,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT',
    update_mode='MODEL_CHANGED',
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350,
    width='100%',
    reload_data=True
)

data = grid_response['data']
selected = grid_response['selected_rows']
df2 = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df2