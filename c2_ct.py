import streamlit as st
import plotly.express as px
import pandas as pd
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="")
mycursor = mydb.cursor(buffered=True)
mycursor.execute('use capstone_2')#Selecting the SQL database

st.title("Phonepe Datavisualization")
#Creating about section of the app
About=st.sidebar.selectbox('About',['About','technology used'])
if About=='About':
    st.sidebar.write('The streamlit app is built to visualization of phonepe raw data in a chart format')
elif About=='technology used':
    st.sidebar.write('Python library  plotly, pandas, sql connector, streamlit are used to create this app')
#Creating a select box for the users to select the required data to visualise
data_type=st.sidebar.selectbox("Select Data Type", ["Transaction", "Users",'Users_brand',
                                                    'Map_Transaction','Map_users','top_transactions',
#This section contains the data of aggregated transactions                                                   'Top Transaction PinCode','Top Users Data'])
if data_type=='Transaction':
    st.header('phonepe Transaction data')
    chart_type = st.selectbox("Select Chart Type", ["Line Chart", "bar",'Sunburst'])
    if chart_type == "Line Chart":#This block of code contains the line chart creation
        mycursor.execute('SELECT Year ,sum(Amount) as Amount,SUM(Count)as count FROM t_1 GROUP BY Year')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dc_1=pd.DataFrame(r1,columns=columns)
        st.header("Line Chart")
        c1=px.line(Dc_1,x=Dc_1['Year'],y=Dc_1['Amount'])
        st.plotly_chart(c1)
#This block of code contains the bar chart code
    elif chart_type == "bar":
        st.header("bar chart")
        mycursor.execute('SELECT Year ,sum(Amount) as Amount,SUM(Count)as count FROM t_1 GROUP BY Year')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dc_1=pd.DataFrame(r1,columns=columns)
        c1=px.bar(Dc_1,x=Dc_1['Year'],y=Dc_1['Amount'])
        st.plotly_chart(c1)
#This block contains the sunburst chart code
    elif chart_type=='Sunburst':
        mycursor.execute('SELECT State,Year,Quater,Transaction,Count,Amount FROM t_1')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dc_a=pd.DataFrame(r1,columns=columns)
        st.header("Sunburst")
        c1=px.sunburst(Dc_a,path=["Year","Quater","Transaction","State"],values='Count',color='Amount')
        st.plotly_chart(c1)
#Creation of tables for the aggregated users data
elif data_type=='Users':
    st.header('phonepe users data')
    chart_type = st.selectbox("Select Chart Type", ['Bar-Regestered_users', 'Bar-App_open','All_data-Sunburst'])
    mycursor.execute('SELECT Year ,sum(Regestered_users) as Regestered_users,sum(AppOpens) as AppOpens FROM t_2 GROUP by Year')
    r1=mycursor.fetchall()
    columns = [i[0] for i in mycursor.description]
    
    Dcr_1=pd.DataFrame(r1,columns=columns)
#Code for bar chat of registered users    
    if chart_type=='Bar-Regestered_users':
        c1=px.bar(x=Dcr_1['Year'],y=Dcr_1['Regestered_users'],orientation='v', labels={'x':'Year', 'y':'total users'}, title='Regestered users')
        st.plotly_chart(c1)
#Code for bar chart of app open
    elif chart_type=='Bar-App_open':
        c1=px.bar(x=Dcr_1['Year'],y=Dcr_1['AppOpens'],orientation='v', labels={'x':'Year', 'y':'App_open'}, title='Application open')
        st.plotly_chart(c1)
#Code for Sunburst data of aggregated users
    elif chart_type == 'All_data-Sunburst':
        mycursor.execute('select State,Year,Quater,Regestered_users,AppOpens from t_2')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dcr_a=pd.DataFrame(r1,columns=columns)
        c1=px.sunburst(Dcr_a,path=['Year','Quater','State'],color='State',values='Regestered_users')
        st.plotly_chart(c1)
#Creating code for users brand data and its chart
elif data_type=='Users_brand':
    st.header('phonepe users brand data')
    chart_type = st.selectbox("Select Chart Type", ['Brand_details','All_data-Sunburst'])
    mycursor.execute('SELECT Year,Brand,sum(Count) as Count,Sum(Percentage) as Percentage FROM t_3 GROUP by Brand,Year order by Count Desc')
    r1=mycursor.fetchall()
    columns = [i[0] for i in mycursor.description]
    Dcb_1=pd.DataFrame(r1,columns=columns)#Creating a data frame for the chart
    if chart_type=='Brand_details':
        cb=px.bar(x=Dcb_1['Brand'],y=Dcb_1['Count'],orientation='v',barmode='group',labels={'x':'Brand', 'y':'Users'}, title='Brand_user_Data')
        st.plotly_chart(cb)
    elif chart_type=='All_data-Sunburst':
        mycursor.execute("select State,Year,Quater,Brand,Count,Percentage from t_3")
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dcb_a=pd.DataFrame(r1,columns=columns)
        Dcb_a.head()
        c1=px.sunburst(Dcb_a,path=['Year','Quater','Brand','State'],color='State',values='Count')
        st.plotly_chart(c1)
#Creating a Code for map transactions and creating a data frame for map visualisation
elif data_type=='Map_Transaction':
    st.header('phonepe Transaction Data Map Visualization')
    map_year = st.selectbox("Select Chart Type", [2018,2019,2020,2021,2022,2023])
    #Create visualising the map of India for each year
    if map_year==2018:
        mycursor.execute('SELECT State,Year,sum(Count) as Count,sum(Amount) as Amount  FROM tg_1 where 2018 GROUP by State')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dma_18=pd.DataFrame(r1,columns=columns)
        I_18 = px.choropleth(
        Dma_18,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Amount',
        color_continuous_scale='Cividis')
        I_18.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(I_18.to_dict())
    elif map_year==2019:
        mycursor.execute('SELECT State,Year,sum(Count) as Count,sum(Amount) as Amount  FROM tg_1 where Year=2019 GROUP by State')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dma_19=pd.DataFrame(r1,columns=columns)
        I_19 = px.choropleth(
        Dma_19,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Amount',
        color_continuous_scale='Viridis',
        hover_name="State")

        I_19.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(I_19.to_dict())
    elif map_year==2020:
        mycursor.execute('SELECT State,Year,sum(Count) as Count,sum(Amount) as Amount  FROM tg_1 where Year=2020 GROUP by State')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dma_20=pd.DataFrame(r1,columns=columns)
        I_20 = px.choropleth(
        Dma_20,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Amount',
        color_continuous_scale='Magma',
        hover_name="State")

        I_20.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(I_20.to_dict())
    elif map_year==2021:
        mycursor.execute('SELECT State,Year,sum(Count) as Count,sum(Amount) as Amount  FROM tg_1 where Year=2021 GROUP by State')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dma_21=pd.DataFrame(r1,columns=columns)
        I_21 = px.choropleth(
        Dma_21,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Amount',
        color_continuous_scale='Turbo',
        hover_name="State")

        I_21.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(I_21.to_dict())
    elif map_year==2022:
        mycursor.execute('SELECT State,Year,sum(Count) as Count,sum(Amount) as Amount  FROM tg_1 where Year=2022 GROUP by State')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dma_22=pd.DataFrame(r1,columns=columns)
        I_22 = px.choropleth(
        Dma_22,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Amount',
        color_continuous_scale='Inferno',
        hover_name="State")

        I_22.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(I_22.to_dict())
    elif map_year==2023:
        mycursor.execute('SELECT State,Year,sum(Count) as Count,sum(Amount) as Amount  FROM tg_1 where Year=2023 GROUP by State')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dma_23=pd.DataFrame(r1,columns=columns)
        I_23 = px.choropleth(
        Dma_23,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Amount',
        color_continuous_scale='Jet',
        hover_name="State")

        I_23.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(I_23.to_dict())
#Creating map data for users and its data frame
elif data_type=='Map_users':
    st.header('phonepe Users Data Map Visualization')
    map_year = st.selectbox("Select Chart Type", [2018,2019,2020,2021,2022,2023])
    #Creating map  of India for each year
    if map_year==2018:
        mycursor.execute('SELECT State ,sum(registered_users) as registered_users,sum(AppOpens) as AppOpens FROM tg_2 WHERE Year=2018 GROUP by State')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dmr_18=pd.DataFrame(r1,columns=columns)
       
        I_18 = px.choropleth(
            Dmr_18,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='registered_users',
            color_continuous_scale='Viridis',
            hover_name="State")

        I_18.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(I_18.to_dict())
    
    elif map_year==2019:
        mycursor.execute('SELECT State ,sum(registered_users) as registered_users,sum(AppOpens) as AppOpens FROM tg_2 WHERE Year=2019 GROUP by State')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dmr_19=pd.DataFrame(r1,columns=columns)
        
        I_19 = px.choropleth(
            Dmr_19,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='registered_users',
            color_continuous_scale='Inferno',
            hover_name="State")

        I_19.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(I_19.to_dict())
    elif map_year==2020:
        mycursor.execute('SELECT State ,sum(registered_users) as registered_users,sum(AppOpens) as AppOpens FROM tg_2 WHERE Year=2020 GROUP by State')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dmr_20=pd.DataFrame(r1,columns=columns)
        
        I_20 = px.choropleth(
            Dmr_20,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='registered_users',
            color_continuous_scale='Plasma',
            hover_name="State")

        I_20.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(I_20.to_dict())
    elif map_year==2021:
        mycursor.execute('SELECT State ,sum(registered_users) as registered_users,sum(AppOpens) as AppOpens FROM tg_2 WHERE Year=2021 GROUP by State')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dmr_21=pd.DataFrame(r1,columns=columns)
        
        I_21 = px.choropleth(
            Dmr_21,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='registered_users',
            color_continuous_scale='Magma',
            hover_name="State")

        I_21.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(I_21.to_dict())
    elif map_year==2022:
        mycursor.execute('SELECT State ,sum(registered_users) as registered_users,sum(AppOpens) as AppOpens FROM tg_2 WHERE Year=2022 GROUP by State')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dmr_22=pd.DataFrame(r1,columns=columns)
        
        I_22 = px.choropleth(
            Dmr_22,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='registered_users',
            color_continuous_scale='RdBu',
            hover_name="State")

        I_22.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(I_22.to_dict())
    elif map_year==2023:
        mycursor.execute('SELECT State ,sum(registered_users) as registered_users,sum(AppOpens) as AppOpens FROM tg_2 WHERE Year=2023 GROUP by State')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dmr_23=pd.DataFrame(r1,columns=columns)
        
        I_23 = px.choropleth(
            Dmr_23,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='registered_users',
            color_continuous_scale='RdBu',
            hover_name="State")

        I_23.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(I_23.to_dict())
#Creating code for top transactions of districts data
elif data_type=='top_transactions':
    st.header('phonepe Top Transaction data')
    chart_type = st.selectbox("Select Chart Type", ["bar_amount","bar_count",'all data Sunburst'])
    mycursor.execute('SELECT Year,sum(amount) as amount,sum(count) as count FROM t_4 GROUP by Year')
    r1=mycursor.fetchall()
    columns = [i[0] for i in mycursor.description]
    Dtt_1=pd.DataFrame(r1,columns=columns)
    if chart_type=="bar_amount":
        c1=px.bar(x=Dtt_1['Year'],y=Dtt_1['amount'],labels={'x':'Year', 'y':'amount'},orientation='v',title='top transaction data')
        st.plotly_chart(c1)
    elif chart_type=="bar_count":
        c1=px.bar(x=Dtt_1['Year'],y=Dtt_1['count'],labels={'x':'Year', 'y':'count'},orientation='v',title='top transaction data')
        st.plotly_chart(c1)
    elif chart_type=='all data Sunburst':
        mycursor.execute('SELECT Year,Quater,State,District,amount,count FROM t_4')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dtt_a=pd.DataFrame(r1,columns=columns)
        c1=px.sunburst(Dtt_a,path=['Year','Quater','State','District','amount'],color='State',values='count')
        st.plotly_chart(c1)
# Creating code for top transactions pin code data and its visualisation charts
elif data_type=='Top Transaction PinCode':
    st.header('phonepe Top Transaction Pincode data')
    chart_type = st.selectbox("Select Chart Type", ["bar_amount","line",'all data Sunburst'])
    mycursor.execute('SELECT Year,Quater,State,Pincode,sum(Count) as count,sum(Amount) as Amount from t_5 GROUP by Year')
    r1=mycursor.fetchall()
    columns = [i[0] for i in mycursor.description]
    Dtp_1=pd.DataFrame(r1,columns=columns)
    if chart_type=='all data Sunburst':
        mycursor.execute('SELECT Year,Quater,State,Pincode,Count,Amount from t_5')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dtp_a=pd.DataFrame(r1,columns=columns)
        c1=px.sunburst(Dtp_a,path=['Year','Quater','State','Pincode'],color='State',values='Amount')
        st.plotly_chart(c1)
    elif chart_type=='line':
        c1=px.line(Dtp_1,x=Dtp_1['Year'],y=Dtp_1['Amount'],labels={'x':'Year', 'y':'amount'},title='top transaction pincode Amount')
        st.plotly_chart(c1)
    elif chart_type=="bar_amount":
        c1=px.bar(x=Dtp_1['Year'],y=Dtp_1['Amount'],labels={'x':'Year', 'y':'amount'},orientation='v',title='top transaction Amount')
        st.plotly_chart(c1)
elif data_type=='Top Users Data':
    st.header('phonepe Top Transaction Pincode data')
    chart_type = st.selectbox("Select Chart Type", ["bar",'all data'])
    if chart_type=='bar':
        mycursor.execute('SELECT Year,State,District,max(registeredUsers) as registeredUsers  FROM t_6 GROUP by Year,District order by registeredUsers DESC limit 10')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dtu_u=pd.DataFrame(r1,columns=columns)
        st.header('phonepe Top 10 Registered Users District Data')
        c1=px.bar(x=Dtu_u['District'],y=Dtu_u['registeredUsers'],orientation='v',labels={'x':'Year', 'y':'amount'},title='top registered District')
        st.plotly_chart(c1)
        st.write(Dtu_u)
    elif chart_type== 'all data':
        mycursor.execute('SELECT Year,Quater,State,District,registeredUsers FROM t_6')
        r1=mycursor.fetchall()
        columns = [i[0] for i in mycursor.description]
        Dtu_a=pd.DataFrame(r1,columns=columns)
        c1=px.sunburst(Dtu_a,path=['Year','Quater','State','District',],color='State',values='registeredUsers')
        st.plotly_chart(c1)
#Creating a scroll bar for 10 different questions which can be selected by the users and the answers will be displayed
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
    c1=px.bar(x=Dq_1['State'],y=Dq_1['Amount'],orientation='v',labels={'x':'State', 'y':'amount'},title='top 10 State')
    st.plotly_chart(c1)
    st.write(Dq_1)
elif Q=='2.What are the top 10 maximum transaction amount in 2022 and which state has highest number?':
    mycursor.execute('SELECT  DISTINCT State,Year,MAX(Amount) as Amount FROM t_1 where Year=2022 GROUP BY  State ORDER by Amount DESC LIMIT 10')
    r1=mycursor.fetchall()
    columns = [i[0] for i in mycursor.description]
    Dq_2=pd.DataFrame(r1,columns=columns)
    c1=px.bar(x=Dq_2['State'],y=Dq_2['Amount'],orientation='v',labels={'x':'State', 'y':'amount'},title='top 10 State')
    st.plotly_chart(c1)
    st.write(Dq_2)
elif Q=='3.What are the bottom 10 stats  in terms of lowest transactions amount in the year 2022?':
    mycursor.execute('SELECT  DISTINCT State,Year,Min(Amount) as Amount FROM t_1 where Year=2022 GROUP BY  State ORDER by Amount ASC LIMIT 10')
    r1=mycursor.fetchall()
    columns = [i[0] for i in mycursor.description]
    Dq_3=pd.DataFrame(r1,columns=columns)
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