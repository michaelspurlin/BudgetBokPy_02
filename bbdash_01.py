import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode # better tables in Streamlit


# df = pd.DataFrame(px.data.gapminder())
#  clist = df['country'].unique()
#country = st.sidebar.selectbox("Select a country:", clist)

df = pd.read_csv('Rock_City_FY2022_Budget_Data.csv')




deptlist = df['dept_name'].unique()


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

#creating columns
col1, col2 = st.columns((1,1))
with col1:
     choice = st.radio(
    "Would you like to view by department name or by fund?",
    ('By department', 'By fund'))

if choice == 'By department':
    df_1 = df_dept_sum
    st.header("By Department")
else:
    df_1 = df_fund_sum
    st.header("By Fund")
with col2:

     view = st.radio(
         "Would you like the table view or the chart view?",
         ('table', 'chart'))


# create choice (dept or fund or chart) radio buttons


#create View (table or chart) radio buttons
if view == 'table':
    st.write('You selected the table view.')
    st.dataframe(df_1, height=700)
else:
    st.write("You selected the chart view.")
    fig = px.bar(df_1, x="amount", orientation='h')
    st.write(fig)


department = st.sidebar.selectbox("Select a department:", deptlist, index=0)

# #creating a better table view of the data set using aggrid
# #put df into Agrid format
# #AgGrid(df)
# gb = GridOptionsBuilder.from_dataframe(df)
# gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
# gb.configure_side_bar() #Add a sidebar
# gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
# gridOptions = gb.build()
#
# grid_response = AgGrid(
#     df,
#     gridOptions=gridOptions,
#     data_return_mode='AS_INPUT',
#     update_mode='MODEL_CHANGED',
#     fit_columns_on_grid_load=False,
#     theme='blue', #Add theme color to the table
#     enable_enterprise_modules=True,
#     height=350,
#     width='100%',
#     reload_data=True
# )
#
# data = grid_response['data']
# selected = grid_response['selected_rows']
# df2 = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df2