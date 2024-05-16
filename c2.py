import os
import json
import pandas as pd
import streamlit as st
from datetime import datetime
from sqlalchemy import create_engine
import mysql.connector
import plotly.express as px

mydb = mysql.connector.connect(host="localhost", user="root", password="")
mycursor = mydb.cursor(buffered=True)
mycursor.execute('use capstone_2')

username = 'root'
password = ''
host = 'localhost'
database_name = 'capstone_2'
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{database_name}')


def home():
    st.image(r"C:\Users\kesav\Guvi\phonepe\logo.png")
    st.title('Project done by KESAVAPRASAD')


def about():
    st.title("history of phonepe")
    st.image(r"C:\Users\kesav\Guvi\phonepe\h1.webp")
    st.image(r"C:\Users\kesav\Guvi\phonepe\h2.webp")
    st.image(r"C:\Users\kesav\Guvi\phonepe\h3.webp")
    st.title('Business model')
    st.image(r"C:\Users\kesav\Guvi\phonepe\bm1.webp")
    st.image(r"C:\Users\kesav\Guvi\phonepe\bm2.webp")


def visualization_of_data():
    st.title('Phonepe  data visualisation')

    def user_transaction():
        Df1 = pd.read_sql_query('SELECT State,Year,Quater,Transaction,Count,Amount FROM t_1', engine)
        mydb.close()

        def table():
        # Define your SQL query
            query = "SELECT State, Year, Quater, Transaction,Count, Amount FROM t_1 WHERE Year = %s AND Quater = %s AND State = %s"
            col1, col2, col3 = st.columns(3)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            with col3:
                state = st.selectbox("select the state:", Df1['State'].unique(),index=0)
            year = str(year)
            quater = int(quater)
            state = str(state)
            # Execute the query and create a DataFrame
            df = pd.read_sql_query(query, engine, params=(year, quater, state))
            df['Year']=df['Year'].astype(str)
            st.write(df)
        def bar():
            query = "SELECT State, Year, Quater, Transaction,Count, Amount FROM t_1 WHERE Year = %s AND Quater = %s AND State = %s"
            col1, col2, col3 = st.columns(3)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            with col3:
                state = st.selectbox("select the state:", Df1['State'].unique(),index=0)
            year = str(year)
            quater = int(quater)
            state = str(state)
            # Execute the query and create a DataFrame
            df = pd.read_sql_query(query, engine, params=(year, quater, state))
            df['Year']=df['Year'].astype(str)
            st.title("Bar Chart for transaction")
            y1=st.selectbox("select y axis:",['Amount','Count'])
            # Create bar chart
            fig = px.bar(df, x='Transaction', y=y1, title='Transactions of the state:'+ state)
            # Display the chart
            st.plotly_chart(fig)
        def bar_state():
            st.title("Bar Chart for state")
            col1, col2 = st.columns(2)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            year = str(year)
            quater = int(quater)
            # Execute the query and create a DataFrame
            query = "SELECT State, Year, Quater, Transaction,Count, Amount FROM t_1 WHERE Year = %s AND Quater = %s"
            df = pd.read_sql_query(query, engine, params=(year, quater))
            y1=st.selectbox("select y axis:",['Amount','Count'])
            # Create bar chart
            fig = px.bar(df, x='State', y=y1, title='Transactions of  all state:')
            # Display the chart
            st.plotly_chart(fig)
        def sunburst():
            st.title("sunburst for state")
           
            state = st.selectbox("select the State:", Df1['State'].unique(),index=0)
            state=str(state)
            
            # Execute the query and create a DataFrame
            query = "SELECT State, Year, Quater, Transaction,Count, Amount FROM t_1 WHERE State = %s "
            df = pd.read_sql_query(query, engine, params=(state,))
            #y1=st.selectbox("select y axis:",['Amount','Count'])
            # Create bar chart
            fig = px.sunburst(df,path=["Year","Quater","Transaction"],values='Count',color='Amount')
            # Display the chart
            st.plotly_chart(fig)
            
           

        page = ["table","bar",'bar_state','sunburst']
        selected_page = st.sidebar.selectbox('Select a content:', page)
        page_details = {
            'table':table,
            'bar': bar,
            'bar_state':bar_state,
            'sunburst':sunburst
        }
        page_details[selected_page]()
    def user_registration():
        Df1 = pd.read_sql_query('SELECT State,Year,Quater,Regestered_users,AppOpens FROM t_2', engine)
        mydb.close()

        def table():
        # Define your SQL query
            query = "SELECT State, Year, Quater, Regestered_users,AppOpens FROM t_2 WHERE Year = %s AND Quater = %s AND State = %s"
            col1, col2, col3 = st.columns(3)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            with col3:
                state = st.selectbox("select the state:", Df1['State'].unique(),index=0)
            year = str(year)
            quater = int(quater)
            state = str(state)
            # Execute the query and create a DataFrame
            df = pd.read_sql_query(query, engine, params=(year, quater, state))
            df['Year']=df['Year'].astype(str)
            st.write(df)

        def bar_user():
            st.title("Bar Chart for state")
            col1, col2 = st.columns(2)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            year = str(year)
            quater = int(quater)
            # Execute the query and create a DataFrame
            query = "SELECT State, Year, Quater, Regestered_users,AppOpens FROM t_2 WHERE Year = %s AND Quater = %s"
            df = pd.read_sql_query(query, engine, params=(year, quater))
            y1=st.selectbox("select y axis:",['Regestered_users','AppOpens'])
            # Create bar chart
            fig = px.bar(df, x='State', y=y1, title='Registration of  all state:')
            # Display the chart
            st.plotly_chart(fig)
           

        page = ["table",'bar_user']
        selected_page = st.sidebar.selectbox('Select a content:', page)
        page_details = {
            'table':table,
            'bar_user':bar_user
        }
        page_details[selected_page]()
    def users_brand():
        Df1 = pd.read_sql_query('SELECT State,Year,Quater,Brand,Count,Percentage FROM t_3', engine)
        mydb.close()

        def table():
        # Define your SQL query
            query = "SELECT State, Year, Quater,Brand,Count,Percentage FROM t_3 WHERE Year = %s AND Quater = %s AND State = %s"
            col1, col2, col3 = st.columns(3)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            with col3:
                state = st.selectbox("select the state:", Df1['State'].unique(),index=0)
            year = str(year)
            quater = int(quater)
            state = str(state)
            # Execute the query and create a DataFrame
            df = pd.read_sql_query(query, engine, params=(year, quater, state))
            df['Year']=df['Year'].astype(str)
            st.write(df)
        def bar():
            query = "SELECT State, Year, Quater,Brand,Count,Percentage FROM t_3 WHERE Year = %s AND Quater = %s AND State = %s"
            col1, col2, col3 = st.columns(3)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            with col3:
                state = st.selectbox("select the state:", Df1['State'].unique(),index=0)
            year = str(year)
            quater = int(quater)
            state = str(state)
            # Execute the query and create a DataFrame
            df = pd.read_sql_query(query, engine, params=(year, quater, state))
            df['Year']=df['Year'].astype(str)
            st.title("Bar Chart for transaction")
            y1=st.selectbox("select y axis:",['Count','Percentage'])
            # Create bar chart
            fig = px.bar(df, x='Brand', y=y1, title='Transactions of the Brand of:'+ state)
            # Display the chart
            st.plotly_chart(fig)
        def users_brand_general():
            st.title("Bar Chart for state")
            col1, col2 = st.columns(2)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            year = str(year)
            quater = int(quater)
            # Execute the query and create a DataFrame
            query = "SELECT State, Year, Quater,Brand,Count,Percentage FROM t_3 WHERE Year = %s AND Quater = %s"
            df = pd.read_sql_query(query, engine, params=(year, quater))
            y1=st.selectbox("select y axis:",['Count','Percentage'])
            # Create bar chart
            fig = px.bar(df, x='Brand', y=y1, title='Transactions of  all Brand:')
            # Display the chart
            st.plotly_chart(fig)
        def sunburst():
            st.title("sunburst for state")
           
            state = st.selectbox("select the State:", Df1['State'].unique(),index=0)
            state=str(state)
            
            # Execute the query and create a DataFrame
            query = "SELECT State, Year, Quater,Brand,Count,Percentage FROM t_3 WHERE State = %s "
            df = pd.read_sql_query(query, engine, params=(state,))
            #y1=st.selectbox("select y axis:",['Count','Percentage'])
            # Create bar chart
            fig = px.sunburst(df,path=["Year","Quater","Brand"],values='Count',color='Percentage')
            # Display the chart
            st.plotly_chart(fig)
            
           

        page = ["table","bar",'users_brand_general','sunburst']
        selected_page = st.sidebar.selectbox('Select a content:', page)
        page_details = {
            'table':table,
            'bar': bar,
            'users_brand_general':users_brand_general,
            'sunburst':sunburst
        }
        page_details[selected_page]()
    def map_transaction():

        def map_transaction_amount():
            Df1 = pd.read_sql_query('SELECT State,Year,Quater,Count,Amount FROM tg_1' , engine)
            mydb.close()
            col1, col2 = st.columns(2)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(), index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(), index=0)
            
            year = str(year)
            quater = int(quater)
            
            # Execute the SQL query with parameters
            d1 = pd.read_sql_query('SELECT State,Year,sum(Count) as Count,sum(Amount) as Amount FROM tg_1 WHERE Year=%s AND Quater=%s GROUP BY State', engine, params=(year, quater))

            fig = px.choropleth(
                d1,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='State',
                color='Amount',
                color_continuous_scale='Cividis'
            )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig.to_dict())
            st.write(d1)
    
        def map_transaction_Count():
            Df1 = pd.read_sql_query('SELECT State,Year,Quater,Count,Amount FROM tg_1' , engine)
            mydb.close()
            col1, col2 = st.columns(2)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(), index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(), index=0)
            
            year = str(year)
            quater = int(quater)
            
            # Execute the SQL query with parameters
            d1 = pd.read_sql_query('SELECT State,Year,sum(Count) as Count,sum(Amount) as Amount FROM tg_1 WHERE Year=%s AND Quater=%s GROUP BY State', engine, params=(year, quater))

            fig = px.choropleth(
                d1,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='State',
                color='Count',
                color_continuous_scale='Cividis'
            )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig.to_dict())
            st.write(d1)

        
        page = ['map_transaction_amount','map_transaction_Count']
        selected_page = st.sidebar.selectbox('Select a type of data:', page)
        page_details = {
            'map_transaction_amount':map_transaction_amount,
            'map_transaction_Count':map_transaction_Count
            }
        page_details[selected_page]()

    def map_users():
        Df1 = pd.read_sql_query('SELECT State,Year,Quater,District,registered_users,AppOpens FROM tg_2' , engine)
        mydb.close()

        def map_registered_users():
            
            col1, col2 = st.columns(2)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(), index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(), index=0)
            
            year = str(year)
            quater = int(quater)
            
            # Execute the SQL query with parameters
            d1 = pd.read_sql_query('SELECT State,Year,Quater,District,sum(registered_users) as registered_users FROM tg_2 WHERE Year=%s AND Quater=%s GROUP BY State', engine, params=(year, quater))

            fig = px.choropleth(
                d1,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='State',
                color='registered_users',
                color_continuous_scale='Cividis'
            )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig.to_dict())
            st.write(d1)
    
        def map_users_appopen():
            col1, col2 = st.columns(2)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(), index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(), index=0)
            
            year = str(year)
            quater = int(quater)
            
            # Execute the SQL query with parameters
            d1 = pd.read_sql_query('SELECT State,Year,Quater,District,sum(AppOpens) as AppOpens FROM tg_2 WHERE Year=%s AND Quater=%s GROUP BY State', engine, params=(year, quater))

            fig = px.choropleth(
                d1,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='State',
                color='AppOpens',
                color_continuous_scale='Cividis'
            )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig.to_dict())
            st.write(d1)

        
        page = ['map_registered_users','map_users_appopen']
        selected_page = st.sidebar.selectbox('Select a type of data:', page)
        page_details = {
            'map_registered_users':map_registered_users,
            'map_users_appopen':map_users_appopen
            }
        page_details[selected_page]()
    def user_district_transaction():
        Df1 = pd.read_sql_query('SELECT State,Year,Quater,District,count,amount FROM t_4', engine)
        mydb.close()

        def table():
        # Define your SQL query
            query = "SELECT State, Year, Quater,District,count,amount FROM t_4 WHERE Year = %s AND Quater = %s AND State = %s"
            col1, col2, col3 = st.columns(3)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            with col3:
                state = st.selectbox("select the state:", Df1['State'].unique(),index=0)
            year = str(year)
            quater = int(quater)
            state = str(state)
            # Execute the query and create a DataFrame
            df = pd.read_sql_query(query, engine, params=(year, quater, state))
            df['Year']=df['Year'].astype(str)
            st.write(df)
        def bar():
            query = "SELECT State, Year, Quater,District,count,amount FROM t_4 WHERE Year = %s AND Quater = %s AND State = %s"
            col1, col2, col3 = st.columns(3)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            with col3:
                state = st.selectbox("select the state:", Df1['State'].unique(),index=0)
            year = str(year)
            quater = int(quater)
            state = str(state)
            # Execute the query and create a DataFrame
            df = pd.read_sql_query(query, engine, params=(year, quater, state))
            df['Year']=df['Year'].astype(str)
            st.title("Bar Chart for transaction")
            y1=st.selectbox("select y axis:",['amount','count'])
            # Create bar chart
            fig = px.bar(df, x='District', y=y1, title='Transactions of District of:'+ state)
            # Display the chart
            st.plotly_chart(fig)
        def bar_state():
            st.title("Bar Chart for state")
            col1, col2 = st.columns(2)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            year = str(year)
            quater = int(quater)
            # Execute the query and create a DataFrame
            query = "SELECT State, Year, Quater,District,count,amount FROM t_4 WHERE Year = %s AND Quater = %s"
            df = pd.read_sql_query(query, engine, params=(year, quater))
            y1=st.selectbox("select y axis:",['amount','count'])
            # Create bar chart
            fig = px.bar(df, x='State', y=y1, title='Transactions of  all state:')
            # Display the chart
            st.plotly_chart(fig)
        def sunburst():
            st.title("sunburst for state")
           
            state = st.selectbox("select the State:", Df1['State'].unique(),index=0)
            state=str(state)
            
            # Execute the query and create a DataFrame
            query = "SELECT State, Year, Quater,District,count,amount FROM t_4 WHERE State = %s "
            df = pd.read_sql_query(query, engine, params=(state,))
            
            # Create sunburst chart
            fig = px.sunburst(df,path=["Year","Quater","District"],values='count',color='amount')
            # Display the chart
            st.plotly_chart(fig)
            
           

        page = ["table","bar",'bar_state','sunburst']
        selected_page = st.sidebar.selectbox('Select a content:', page)
        page_details = {
            'table':table,
            'bar': bar,
            'bar_state':bar_state,
            'sunburst':sunburst
        }
        page_details[selected_page]()

    def user_pincode_transaction():
        Df1 = pd.read_sql_query('SELECT State,Year,Quater,Pincode,Count,Amount FROM t_5', engine)
        mydb.close()

        def table():
        # Define your SQL query
            query = "SELECT State, Year, Quater,Pincode,Count,Amount FROM t_5 WHERE Year = %s AND Quater = %s AND State = %s"
            col1, col2, col3 = st.columns(3)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            with col3:
                state = st.selectbox("select the state:", Df1['State'].unique(),index=0)
            year = str(year)
            quater = int(quater)
            state = str(state)
            # Execute the query and create a DataFrame
            df = pd.read_sql_query(query, engine, params=(year, quater, state))
            df['Year']=df['Year'].astype(str)
            df['Pincode']=df['Pincode'].astype(str)
            st.write(df)
        def Scatter():
            query = "SELECT State, Year, Quater,Pincode,Count,Amount FROM t_5 WHERE Year = %s AND Quater = %s AND State = %s "
            col1, col2, col3 = st.columns(3)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            with col3:
                state = st.selectbox("select the state:", Df1['State'].unique(),index=0)
            year = str(year)
            quater = int(quater)
            state = str(state)
            # Execute the query and create a DataFrame
            df = pd.read_sql_query(query, engine, params=(year, quater, state))
            df['Year']=df['Year'].astype(str)
            df['Pincode']=df['Pincode'].astype(str)
            
            y1=st.selectbox("select y axis:",['Amount','Count'])
            st.title("Scatter Chart for transaction:"+y1)
            # Create bar chart
            fig = px.scatter(df, x='Pincode', y=y1, title='Transactions of Pincode of:'+ state)
            # Display the chart
            st.plotly_chart(fig)
            st.write(df)
        def bar_state():
            st.title("Bar Chart for state")
            col1, col2 = st.columns(2)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            year = str(year)
            quater = int(quater)
            # Execute the query and create a DataFrame
            query = "SELECT State, Year, Quater,Pincode,Count,Amount FROM t_5 WHERE Year = %s AND Quater = %s"
            df = pd.read_sql_query(query, engine, params=(year, quater))
            y1=st.selectbox("select y axis:",['Amount','Count'])
            st.title("Bar Chart for transaction:"+y1)
            # Create bar chart
            fig = px.bar(df, x='State', y=y1, title='Transactions of  all state:')
            # Display the chart
            st.plotly_chart(fig)
        def sunburst():
            
            state = st.selectbox("select the State:", Df1['State'].unique(),index=0)
            state=str(state)
            st.title("sunburst for state:"+state)
            
            # Execute the query and create a DataFrame
            query = "SELECT State, Year, Quater,Pincode,Count,Amount FROM t_5 WHERE State = %s "
            df = pd.read_sql_query(query, engine, params=(state,))
            
            # Create sunburst chart
            fig = px.sunburst(df,path=["Year","Quater","Pincode"],values='Count',color='Amount')
            # Display the chart
            st.plotly_chart(fig)
            
           

        page = ["table","Scatter",'bar_state','sunburst']
        selected_page = st.sidebar.selectbox('Select a content:', page)
        page_details = {
            'table':table,
            'Scatter': Scatter,
            'bar_state':bar_state,
            'sunburst':sunburst
        }
        page_details[selected_page]()
    def user_district_registration():
        Df1 = pd.read_sql_query('SELECT State,Year,Quater,District,registeredUsers FROM t_6', engine)
        mydb.close()

        def table():
        # Define your SQL query
            query = "SELECT State, Year, Quater,District,registeredUsers FROM t_6 WHERE Year = %s AND Quater = %s AND State = %s"
            col1, col2, col3 = st.columns(3)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            with col3:
                state = st.selectbox("select the state:", Df1['State'].unique(),index=0)
            year = str(year)
            quater = int(quater)
            state = str(state)
            # Execute the query and create a DataFrame
            df = pd.read_sql_query(query, engine, params=(year, quater, state))
            df['Year']=df['Year'].astype(str)
            st.write(df)

        def bar_user():
            st.title("Bar Chart for state")
            col1, col2,col3 = st.columns(3)

            # Example user-provided values
            with col1:
                year = st.selectbox("select the year:", Df1['Year'].unique(),index=0)
            with col2:
                quater = st.selectbox("select the quarter:", Df1['Quater'].unique(),index=0)
            with col3:
                state = st.selectbox("select the state:", Df1['State'].unique(),index=0)
            
            year = str(year)
            quater = int(quater)
            state = str(state)
            # Execute the query and create a DataFrame
            query = "SELECT State, Year, Quater,District,registeredUsers FROM t_6 WHERE Year = %s AND Quater = %s AND State=%s"
            df = pd.read_sql_query(query, engine, params=(year, quater,state))
            # Create bar chart
            fig = px.bar(df, x='District', y='registeredUsers', title='Registration of  all District in:'+ state)
            # Display the chart
            st.plotly_chart(fig)

        page = ['table','bar_user']
        selected_page = st.sidebar.selectbox('Select a content:', page)
        page_details = {
            'table':table,
            'bar_user':bar_user

        }
        page_details[selected_page]()
    
    page = ['user_transaction','user_registration','users_brand','map_transaction','map_users',
            'user_district_transaction','user_pincode_transaction','user_district_registration']
    selected_page = st.sidebar.selectbox('Select a type of data:', page)
    page_details = {
            'user_transaction': user_transaction,
            'user_registration':user_registration,
            'users_brand':users_brand,
            'map_transaction':map_transaction,
            'map_users':map_users,
            'user_district_transaction':user_district_transaction,
            'user_pincode_transaction':user_pincode_transaction,
            'user_district_registration':user_district_registration
            }

    page_details[selected_page]()

#Creating a scroll bar for 10 different questions which can be selected by the users and the answers will be displayed
def Question():   
    st.sidebar.title("Questions")
    Q=st.sidebar.selectbox('select',['1.What are the top 10 maximum transaction amount in 2023 and which state has highest number?',
                                    '2.What are the top 10 maximum transaction amount in 2022 and which state has highest number?',
                                    '3.What are the bottom 10 stats  in terms of lowest transactions amount in the year 2022?',
                                    '4.What are the top 10 states which has highest registered users in the year 2021?',
                                    '5.Which brand phone has the highest users in the year 2022?',
                                    '6.What are the top 10 states of registered users the year 2020?',
                                    '7.What is the data of registered users for the year 2022 quarter 1?',
                                    '8.What are the top 10 districts in terms of transaction for the year 2021 and quarter 4?',
                                    '9.What are the bottom 10 districts which has the lowest transaction amount in the year 2021 and quarter 2?',
                                    '10.Which district has their lowest registered users in the year 2022 quarter 1?'])
    if Q=='1.What are the top 10 maximum transaction amount in 2023 and which state has highest number?':
        mycursor.execute('SELECT  DISTINCT State,Year,MAX(Amount) as Amount FROM t_1 where Year=2023 GROUP BY  State ORDER by Amount DESC LIMIT 10')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dq_1=pd.DataFrame(r1,columns=columns)
        Dq_1['Year'] = Dq_1['Year'].astype(str)
        c1=px.bar(x=Dq_1['State'],y=Dq_1['Amount'],orientation='v',labels={'x':'State', 'y':'amount'},title='top 10 State')
        st.plotly_chart(c1)
        st.write(Dq_1)
    elif Q=='2.What are the top 10 maximum transaction amount in 2022 and which state has highest number?':
        mycursor.execute('SELECT  DISTINCT State,Year,MAX(Amount) as Amount FROM t_1 where Year=2022 GROUP BY  State ORDER by Amount DESC LIMIT 10')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dq_2=pd.DataFrame(r1,columns=columns)
        Dq_2['Year'] = Dq_2['Year'].astype(str)
        c1=px.bar(x=Dq_2['State'],y=Dq_2['Amount'],orientation='v',labels={'x':'State', 'y':'amount'},title='top 10 State')
        st.plotly_chart(c1)
        st.write(Dq_2)
    elif Q=='3.What are the bottom 10 stats  in terms of lowest transactions amount in the year 2022?':
        mycursor.execute('SELECT  DISTINCT State,Year,Min(Amount) as Amount FROM t_1 where Year=2022 GROUP BY  State ORDER by Amount ASC LIMIT 10')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dq_3=pd.DataFrame(r1,columns=columns)
        Dq_3['Year'] = Dq_3['Year'].astype(str)
        c1=px.bar(x=Dq_3['State'],y=Dq_3['Amount'],orientation='v',labels={'x':'State', 'y':'amount'},title='bottom 10 State')
        st.plotly_chart(c1)
        st.write(Dq_3)
    elif Q=='4.What are the top 10 states which has highest registered users in the year 2021?':
        mycursor.execute('SELECT State, MAX(Regestered_users) as Regestered_users FROM t_2 WHERE Year = 2021 GROUP BY State ORDER BY Regestered_users DESC LIMIT 10')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dq_4=pd.DataFrame(r1,columns=columns)
        c1=px.bar(x=Dq_4['State'],y=Dq_4['Regestered_users'],orientation='v',labels={'x':'State', 'y':'Regestered_users'},title='top 10 State registered users')
        st.plotly_chart(c1)
        st.write(Dq_4)
    elif Q =='5.Which brand phone has the highest users in the year 2022?':
        mycursor.execute('SELECT Brand,max(Count) as Count FROM t_3 WHERE Year=2022 GROUP by Brand ORDER by Count DESC limit 10')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dq_5=pd.DataFrame(r1,columns=columns)

        c1=px.bar(x=Dq_5['Brand'],y=Dq_5['Count'],orientation='v',labels={'x':'Brand', 'y':'Count'},title='top 10 used brand')
        st.plotly_chart(c1)
        st.write(Dq_5)
    elif Q=='6.What are the top 10 states of registered users the year 2020?':
        mycursor.execute('SELECT State,max(registered_users) as registered_users FROM tg_2 WHERE Year=2020 GROUP by State ORDER by registered_users DESC LIMIT 10')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dq_6=pd.DataFrame(r1,columns=columns)
        
        c1= px.choropleth(
                    Dq_6,
                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',
                    locations='State',
                    color='registered_users',
                    color_continuous_scale='Viridis',
                    )
        st.plotly_chart(c1)
        st.write(Dq_6)
    elif Q=='7.What is the data of registered users for the year 2022 quarter 1?':
        mycursor.execute('SELECT State, SUM(registered_users) as registered_users FROM tg_2 WHERE Year=2022 AND Quater=1 GROUP BY State ORDER BY State')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dq_7=pd.DataFrame(r1,columns=columns)
        
        c1= px.choropleth(
                    Dq_7,
                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',
                    locations='State',
                    color='registered_users',
                    color_continuous_scale='Viridis',
                    )
        st.plotly_chart(c1)
        st.write(Dq_7)

    elif Q=='8.What are the top 10 districts in terms of transaction for the year 2021 and quarter 4?':
        mycursor.execute('SELECT State, District, MAX(amount) as amount FROM t_4 WHERE Year = 2021 AND Quater = 4 GROUP BY State ORDER BY amount DESC LIMIT 10;')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dq_8=pd.DataFrame(r1,columns=columns)
        
        c1=px.bar(x=Dq_8['District'],y=Dq_8['amount'],orientation='v',labels={'x':'District', 'y':'amount'},title='top 10 district transactions')
        st.plotly_chart(c1)
        st.write(Dq_8)
    elif Q=='9.What are the bottom 10 districts which has the lowest transaction amount in the year 2021 and quarter 2?':
        mycursor.execute('SELECT State, District, min(amount) as amount FROM t_4 WHERE Year = 2021 AND Quater = 2 GROUP BY State ORDER BY amount  LIMIT 10')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dq_9=pd.DataFrame(r1,columns=columns)
        
        c1=px.bar(x=Dq_9['District'],y=Dq_9['amount'],orientation='v',labels={'x':'District', 'y':'amount'},
                title='top 10 district transactions')
        st.plotly_chart(c1)
        st.write(Dq_9)
    elif Q=='10.Which district has their lowest registered users in the year 2022 quarter 1?':
        mycursor.execute('SELECT State,District,min(registeredUsers) as registeredUsers \
                        FROM t_6 WHERE Year=2022 AND Quater=1 GROUP by District ORDER by registeredUsers ASC LIMIT 10')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dq_10=pd.DataFrame(r1,columns=columns)
        
        c1=px.bar(x=Dq_10['District'],y=Dq_10['registeredUsers'],orientation='v',\
                labels={'x':'District', 'y':'registeredUsers'},title='bottom  10 district registeredUsers')
        st.plotly_chart(c1)
        st.write(Dq_10)










page = ['home', 'about', 'visualization_of_data','Question']
selected_page = st.sidebar.selectbox('Select a page:', page)
page_details = {
    'home': home,
    'about': about,
    'visualization_of_data': visualization_of_data,
    'Question':Question

}

page_details[selected_page]()
