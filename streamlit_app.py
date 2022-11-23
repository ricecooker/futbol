import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff

st.set_page_config(layout='wide')

@st.cache
def get_data():
    df = pd.read_csv('data/events.csv.gz')
    return df

st.write(f'Pandas: {pd.__version__}')
st.write(f'Streamlit: {st.__version__}')

df = get_data()


show_histogram = st.checkbox('Show histogram')
goal_time_df = df.query('is_goal == 1')[['time']]
fig = ff.create_distplot(
    [goal_time_df['time'].tolist()], 
    ['time'],
    curve_type='kde',
    show_hist=show_histogram,
    show_rug=False,
)
fig = (
    fig
    .add_vline(x=46, line_dash='dot', line_width=1, annotation_text='half')
    .add_vline(x=91, line_dash='dot', line_width=1, annotation_text='')
    .add_vrect(x0=91, x1=goal_time_df['time'].max(), line_width=0, fillcolor='#fdd', opacity=0.5)
)
fig = fig.update_layout(
    title='Distribution of Goals Scored by Time', 
    xaxis_title='minutes into match', 
    xaxis_dtick=10,
    yaxis_tickformat='.1%',
    showlegend=False,
)
st.plotly_chart(fig, use_container_width=True)

st.markdown('Source: https://www.kaggle.com/datasets/secareanualin/football-events?resource=download')
