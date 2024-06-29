import streamlit as st
import pickle
import pandas as pd
def rec(movie):
    movie_index=movies[movies['title']==movie].index[0]
    dis=similarity[movie_index]
    movies_list=sorted(list(enumerate(dis)),reverse=True,key=lambda x:x[1])[1:10]
    recc_mov=[]
    for i in movies_list:
      recc_mov.append(movies.iloc[i[0]].title)
    return recc_mov

movies_list = pickle.load(open('moviess.pkl','rb'))
movies=pd.DataFrame(movies_list)
similarity=pickle.load(open('simi.pkl','rb'))
st.title("Movie reco system📽️🍿")
option=st.selectbox(
"",
movies['title'].values)

if st.button("recommend"):
    st.write("boom 💥💥💥:")
    recomd=rec(option)
    for i in recomd:
        st.write(i)
