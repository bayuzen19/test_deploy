import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#==== read dataset ===
df = pd.read_csv("data/CarPrice_Assignment.csv")

st.title("Car Price Prediction")
st.subheader("Explonatory Data Analytics")
st.markdown("---")
st.set_option('deprecation.showPyplotGlobalUse', False)

#==== Make Sidebar ====

page = st.sidebar.selectbox(
    "Select a Page",
    [
    "Homepage","Barplot","Scatterplot","Scatterplot six graph"
    ]
)


if page=="Homepage":
    st.header("Data Table Overview")
    st.balloons()
    st.dataframe(df.head(20))

elif page=="Barplot":
    feature_options = ['symboling', 'fueltype', 'aspiration',
                        'doornumber', 'carbody', 
                        'drivewheel', 'enginelocation', 
                        'enginetype', 'cylindernumber', 
                        'fuelsystem']
    page_barplot = st.selectbox("Choose scatterplot Feature with Price", feature_options)
    df_page_barplot = pd.pivot_table(df,index=page_barplot,values='price',aggfunc='mean').sort_values(by='price',ascending=True)
    df_page_barplot = df_page_barplot.reset_index()

    fig, ax = plt.subplots()
    ax = sns.barplot(data=df_page_barplot,x=page_barplot,y="price")
    for p in ax.patches:
        ax.annotate(np.round(p.get_height(),decimals=2), (p.get_x()+p.get_width()/2, p.get_height()), ha='center')
    st.write(f"## Price Comparison for Each {page_barplot}")
    st.pyplot(fig)

elif page == "Scatterplot":
    feature_options = ["wheelbase", "carlength"]
    page_scatter = st.selectbox("Choose scatterplot Feature with Price", feature_options)

    fig, ax = plt.subplots()
    st.write(f"## Correlation between {page_scatter} Base and Price")
    ax = sns.scatterplot(data=df,x=page_scatter, y='price')
    st.pyplot(fig)

    text = f"based on the {page_scatter} graph above, we can see that as {page_scatter} increases, so does the price."
    st.markdown(f"<div style='text-align:center;'><p>{text}</p></div>", unsafe_allow_html=True)

elif page=="Scatterplot six graph":
    fig = plt.figure(figsize=(16,8))
    plt.subplot(2,3,1)
    plt.xlabel("wheel base")
    plt.ylabel("price")
    plt.scatter(df['wheelbase'],df['price'])
    plt.title("Scatterplot WheelBase and Price")

    plt.subplot(2,3,2)
    plt.xlabel("car length")
    plt.ylabel("price")
    plt.scatter(df['carlength'],df['price'])
    plt.title("Scatterplot carlength and Price")

    plt.subplot(2,3,3)
    plt.xlabel("car width")
    plt.ylabel("price")
    plt.scatter(df['carwidth'],df['price'])
    plt.title("Scatterplot carwidth and Price")

    plt.subplot(2,3,4)
    plt.xlabel("curb weight")
    plt.ylabel("price")
    plt.scatter(df['curbweight'],df['price'])
    plt.title("Scatterplot curbweight and Price")

    plt.subplot(2,3,5)
    plt.xlabel("engine size")
    plt.ylabel("price")
    plt.scatter(df['enginesize'],df['price'])
    plt.title("Scatterplot enginesize and Price")

    plt.subplot(2,3,6)
    plt.xlabel("horse power")
    plt.ylabel("price")
    plt.scatter(df['horsepower'],df['price'])
    plt.title("Scatterplot horsepower and Price")

    st.pyplot(fig)

