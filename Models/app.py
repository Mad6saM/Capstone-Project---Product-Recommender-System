import streamlit as st
import pickle
import requests

prod_ids=pickle.load(open('Cust_list,pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

def recommendations(user_index, num_of_products, interactions_matrix):
    
    most_similar_users = similar_users(user_index, interactions_matrix)[0]
    
    prod_ids = set(list(interactions_matrix.columns[np.where(interactions_matrix.loc[user_index] > 0)]))
    recommendations = []
    similar_user=1
    observed_interactions = prod_ids.copy()
    for similar_user in most_similar_users:
        if len(recommendations) < num_of_products:
            
            similar_user_prod_ids = set(list(interactions_matrix.columns[np.where(interactions_matrix.loc[similar_user] > 0)]))
            recommendations.extend(list(similar_user_prod_ids.difference(observed_interactions)))
            observed_interactions = observed_interactions.union(similar_user_prod_ids)
        else:
            break
    
    return recommendations[:num_of_products]

st.header("Product Recommender System")
Product_list=prod_ids
selected_product=st.selectbox("Type or select a customer from the dropdown",prod_ids,index=None)

if st.button("Show Recommendations"):
    user_index = 'Any'
    interactions_matrix = 'Any'

    similar_user_prod_ids = recommendations(user_index, num_of_products=5, interactions_matrix=interactions_matrix)
    st.write("Recommended Products:", similar_user_prod_ids)
