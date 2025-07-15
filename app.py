import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies_df[movies_df['title']== movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True,key= lambda x:x[1])[1:6]
    recommended_movies =[]
    for i in movies_list :
        movie_id = i[0]
        #fetch poster from API

        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies

    # for i in movies_list:
    #     print(new_df.iloc[i[0]].title)
movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values
# print(movies_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie recommender System')

selected_movie_name = st.selectbox(
    'how would you like?',movies_df['title'].values
)

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    st.write(selected_movie_name)
    for movie in recommendation:
        st.write(movie)