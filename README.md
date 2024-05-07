
# Project Title

The title of the project is phonepe data visualisation


## Python libraries 
It requires the following python library
import os
import json
import pandas as pd
from datetime import datetime
import plotly.express as px
from sqlalchemy import create_engine
import mysql.connector
import streamlit as st
In order to run the code And to create the user interface data visualisation using streamlit
## Data extraction
We used the following code !git clone https://github.com/PhonePe/pulse.git To create a phonepe pulse data copy from github For this we need to install Github Innova System
After creating the clone of that particular git hub file We should copy the path of that file and store it in a variable We use os.listdir("path variable') To create the path of the each file
We will stole the required date of while creating each file into a separate variable in form of list and at the end we will try to  Extract the data from the Json file in the folders state for each year's in that folder and store that data into a dictionary format
The stored data in the dictionary format is converted into a pandas data frame which will be used to clean the data in the future
## Data cleaning 
After creating the data frame we need to clean the data to the required format for example in the state column there are unwanted characters present in it we use
 eg Df1['State'] = Df1['State'].str.replace('-&-', ' & ') Following court like this to remove the unwanted characters in the data frame
 Certain columns like state data should be capitalised for the future use of data visualisation of the India map so we use the replace method function in pandas to clear the data.
 In certain data frame the values are filled as null for such data we used  Dropna()  function To clean that data
## Data storage
For each data frame we created we will try to create a replica of that particular data frame into an sql table for each and every data set once that is created using my sql we will try to insert that data using sql alchemy and my sql connector into the required table
## Data extraction
We used the following code !git clone https://github.com/PhonePe/pulse.git To create a phonepe pulse data copy from github For this we need to install Github Innova System
After creating the clone of that particular git hub file We should copy the path of that file and store it in a variable We use os.listdir("path variable') To create the path of the each file
We will stole the required date of while creating each file into a separate variable in form of list and at the end we will try to  Extract the data from the Json file in the folders state for each year's in that folder and store that data into a dictionary format
The stored data in the dictionary format is converted into a pandas data frame which will be used to clean the data in the future
## Data extraction
We used the following code !git clone https://github.com/PhonePe/pulse.git To create a phonepe pulse data copy from github For this we need to install Github Innova System
After creating the clone of that particular git hub file We should copy the path of that file and store it in a variable We use os.listdir("path variable') To create the path of the each file
We will stole the required date of while creating each file into a separate variable in form of list and at the end we will try to  Extract the data from the Json file in the folders state for each year's in that folder and store that data into a dictionary format
The stored data in the dictionary format is converted into a pandas data frame which will be used to clean the data in the future
## Data extraction from my sql
By using my SQL connector we will try to establish a connexion between my sql database we will write queries for each table to create a data frame for data visualisation using plotly
We will create a data frame for each and every graph and chart we need to visualise
We will write the query in pYthon code And extract the data from the Sql Se And extract the data from the Sql Server 
## Data visualisation 
We use streamlit and plotly For creating various chart and map And display that chart and map in your browser using streamlit.
## Roadmap
 Creating a github up clone

 Extraction of data from the Json file

 Converting the extractor data into a dictionary format

Converting the dictionary format variable data  into a pandas data frame one pandas data frame

Cleaning the data from the panda data frame and manipulation the data for the required format for the required format

Inserting the cleaned data into my sql server

Extracting the data for creating data visualisation charts for creating data visualisation charts

Creating a data frame from the extractor data

Creating various shots for data visualisation using ploty and streamlit





