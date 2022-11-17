import pandas as pd
import numpy as np
import streamlit as st


st.title('Dashboard Exercise Using Georgia Covid-19 Data')

st.header('I. Some Commnly Used Commands')
st.text('Below shows some entry-level commands used in Python when loading a dataset')

st.subheader('Import Some Needed Packages')
code1 = '''import pandas as pd
import numpy as np
import streamlit as st'''
st.code(code1, language='python')

st.subheader('Load Dataset')
code2 = '''data = pd.read_csv('file_path.csv')'''
st.code(code2, language='python')

st.subheader('Show Some Basic Information of Dataset')
code3 = '''data.describe()'''
st.code(code3, language='python')

date_column = 'datestamp'
data_url = ('https://raw.githubusercontent.com/mengyao36/AHI_Microcourse_Visualization/main/Data/Georgia_COVID/Georgia_>

@st.cache
def load_data(nrows):
    data = pd.read_csv(data_url, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[date_column] = pd.to_datetime(data[date_column])
    return data

data = load_data(100)

st.header('II. Georgia Covid-19 Data - N = 100')
st.write(data)

st.subheader('Select Sub-dataset N = 30')
data_line = pd.DataFrame(data[:30], columns = ['c_cum', 'h_cum'])
st.write(data_line)

st.subheader('Use of Line Chart')
st.line_chart(data_line)

st.subheader('Use of Area Chart')
st.area_chart(data_line)

st.subheader('Use of Bar Chart')
st.bar_chart(data['county'])
