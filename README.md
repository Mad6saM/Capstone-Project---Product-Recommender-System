# Capstone-Project Product-Recommender-System based on Collaborative Filtering
A machine learning-based project that provides personalized product recommendations to users based on their browsing and purchase history. The system utilizes collaborative filtering and content-based filtering algorithms to analyze user behavior and generate relevant recommendations. This project aims to improve the overall shopping experience for users, increase sales for e-commerce businesses.

# Dataset

You can find the dataset here in the same repository in Dataset folder

# Approach
1) **Similarity based Collaborative filtering**

Objective - Provide personalized and relevant recommendations to users.

Outputs - Recommend top 3 products based on interactions of similar users.

Approach -

* Here, cust_id is of object, for our convenience we convert it to integer type.

+ We write a function to find similar users -
     - Find the similarity score of the desired user with each user in the interaction matrix using cosine_similarity and append to an empty list and sort it.
     - Extract the similar user and similarity scores from the sorted list
     - remove original user and its similarity score and return the rest.
       
+ We write a function to recommend users -
     - Call the previous similar users function to get the similar users for the desired user_id.
     - Find prod_ids with which the original user has interacted -> observed_interactions
     - For each similar user Find 'n' products with which the similar user has interacted with but not the actual user.
     - Return the specified number of products.
       
3) Model based Collaborative filtering
   
Objective -

Provide personalized recommendations to users based on their past behavior and preferences, while also addressing the challenges of sparsity and scalability that can arise in other collaborative filtering techniques.

Outputs -

Recommend top 5 products for a particular user.

**Approach** -

+ Taking the matrix of no.of items and converting it to a CSR(compressed sparse row) matrix. This is done to save memory and computational time, since only the non-zero values need to be stored.
+ Performing singular value decomposition (SVD) on the sparse or csr matrix. SVD is a matrix decomposition technique that can be used to reduce the dimensionality of a matrix. In this case, the SVD is used to reduce the dimensionality of the matrix of no.of items to 5 latent features.
+ Calculating the predicted no.of items for all users using SVD. The predicted ratings are calculated by multiplying the U matrix, the sigma matrix, and the Vt matrix.
+ Storing the predicted no.of items in a DataFrame. The DataFrame has the same columns as the original matrix of no.of items. The rows of the DataFrame correspond to the users. The values in the DataFrame are the no.of items for each user.
+ A function is written to recommend products based on the no.of items predictions made :
    - It gets the user's items purchased from the interactions_matrix.
    - It gets the user's predicted no.of items from the preds_matrix.
    - It creates a DataFrame with the user's actual and predicted no.of items.
    - It adds a column to the DataFrame with the product names.
    - It filters the DataFrame to only include products that the user has not bought.
    - It sorts the DataFrame by the predicted no.of items in descending order.
    - It prints the top num_recommendations products.

+ Evaluating the model :
    - Calculate the average no.of items for all the users by dividing the sum of all the products by the number of products. 2, Calculate the average items bought for all the predicted no.of items bought by dividing the sum of all the predicted no.of items bought by the number of products.
    - Create a DataFrame called rmse_df that contains the average no.of items bought and the average predicted no.of items.
    - Calculate the RMSE of the SVD model by taking the square root of the mean of the squared errors between the average actual no.of items bought and the average predicted no.of items.
      
The squared parameter in the mean_squared_error function determines whether to return the mean squared error (MSE) or the root mean squared error (RMSE). When squared is set to False, the function returns the RMSE, which is the square root of the MSE. In this case, you are calculating the RMSE, so you have set squared to False. This means that the errors are first squared, then averaged, and finally square-rooted to obtain the RMSE.

# Running the system

I have used streamlit platform to test the model. The app.py file in the Models folder can be used to access the same.

You will have to run using the below code:

!streamlit run app.py

You will receive the below output in which, you need to click on the 'your url is: https://every-steaks-hunt.loca.lt', which will redirect you to the platform.

- Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.

You can now view your Streamlit app in your browser.
     
     Network URL: http://172.28.0.12:8501
     External URL: http://34.122.1.9:8501

npx: installed 22 in 5.487s

your url is: https://every-steaks-hunt.loca.lt

**NOTE : The url keeps changing and won't look similar to the one mentioned above**
