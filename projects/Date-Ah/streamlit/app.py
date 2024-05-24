import streamlit as st
st.set_page_config(page_title = "Date-Ah!")
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from geopy.distance import geodesic
import googlemaps
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


gmaps = googlemaps.Client(key = 'AIzaSyCBbYlv82NZSUzXSxkk2FIrjNhd95t3Wmc' )



# --- Header ----

st.subheader('Thank you for using Date-Ah!\nA Restaraunt and Activity Recommender tailored to your needs')

st.write('Please let us know more about your needs to help us understand you better!')
# Function to get user profile
with st.expander('First, set up your user profile here!'):
    def new_user1():
        features = ['budget', 'cuisine', 'activity']
        user_profile = []

        for feature in features:
            importance = st.number_input(f"How important is {feature} to your date experience? (1 = high, 3 = low)", min_value=1, max_value=3, step=1)
            user_profile.append(importance)

        return user_profile

    wz1 = new_user1() 

with st.expander('Next, set up your cuisine profile here!'):
    #function to get user input for cuisine pref
    def new_user_profile_restaurant():

        cuisine_categories = ['Western', 'Chinese', 'Italian', 'Vietnamese', 'Japanese',
        'Singaporean', 'Mexican', 'Indian', 'Malaysian', 'Middle Eastern',
        'Indonesian', 'Spanish', 'Taiwanese', 'French',  'Other']
        
        # Initialize a dictionary to store user preferences
        user_profile = {}

        # Iterate over each cuisine category
        for cuisine in cuisine_categories:
            while True:
                preference = st.number_input(f"On a scale of 0 to 4, how much do you like {cuisine} food? (0 = dislike, 4 = love)", min_value=0, max_value=4, step=1)
                try:
                    preference = int(preference)
                    if preference in [0,1,2,3,4]:
                        user_profile[cuisine] = preference
                        break  # Exit the loop if a valid rating is entered
                    else:
                        print("Invalid rating! Please enter a number between 0 and 4.")
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
        user_profile = pd.Series(user_profile)
        return user_profile

    wz = new_user_profile_restaurant()

with st.expander('Next, set up your activity profile here!'):
    # function to get user input for activity 
    def new_user_profile_activity():
        
        activity_type = ['indoor','outdoor','animals','wet','enrichment','food','history','thrill','culture','nature','exercise','crafts','games']
        
        # Initialize a dictionary to store user preferences
        user_profile = {}

        # Iterate over each activity category
        for activity in activity_type:
            while True:
                preference = st.number_input(f"On a scale of 0 to 2, how much do you like {activity} activities? (0 = least interest, 2 = high interest)", min_value=0, max_value=2, step=1)
                try:
                    preference = int(preference)
                    if preference in [0, 1, 2]:
                        user_profile[activity] = preference
                        break  # Exit the loop if a valid rating is entered
                    else:
                        st.error("Invalid rating! Please enter a 0, 1, or 2.")
                except ValueError:
                    st.error("Invalid input! Please enter a valid number.")
        return user_profile

    wza = new_user_profile_activity()

with st.expander('Finally, input your location here!'):
    #Function to get coordinates based on postal code
    def get_co(postal_code):
        if not postal_code:
            return None
        try:
        # Use gmaps.geocode to get the geographical coordinates
            coordinates = gmaps.geocode(str(postal_code))
            if coordinates: 
            # Extract latitude and longitude
                longitude = coordinates[0]['geometry']['location']['lng']
                latitude = coordinates[0]['geometry']['location']['lat']
                return latitude, longitude
        except googlemaps.exceptions.ApiError as e:
            st.error('Error fetching coordinates. Please try again.')
     #function for user to input location 
    def new_user_postal():
        postalcode = st.text_input("What is your location(in postal code)?")
        return postalcode 
    postal = new_user_postal()


# Function to extract similar users to new user profile
def load_data():
    data = pd.read_csv('df_users.csv')
    data = data.rename_axis('user')
    data.drop(columns = 'user', inplace = True)
    return data
df_users = load_data()
#st.write(df_users.tail())



#  Function to extract similar users to new user profile
def extract_similar_users(new_user_vector, existing_users, threshold):
    
    # Create a DataFrame with the same structure as existing_users
    new_user_df = pd.DataFrame([new_user_vector], columns=existing_users.columns)
    existing_users = pd.concat([existing_users, new_user_df], ignore_index=True)


    similarities = cosine_similarity(new_user_df, existing_users)
    # Get similar users based on threshold (e.g., threshold=0.5)
    similar_users_indices = similarities[-1] > threshold
    similar_users = existing_users.index[similar_users_indices].tolist()

    return similar_users

similar_users = extract_similar_users(wz1, df_users, 0.95)
similar_users = similar_users[:-1]

#st.write(similar_users)





def load_data1():
    data = pd.read_csv('imdf_r.csv')
    return data
imdf_r = load_data1()
imdf_r.index += 1
imdf_r.drop(columns = ['user'],inplace = True)


def load_data2():
    data = pd.read_csv('imdf_a.csv')
    return data
imdf_a = load_data2()
imdf_a.index += 1
imdf_a.drop(columns = ['user'],inplace = True)


def get_highest_rated(interaction_matrix, similar_users):
    # Ensure that 'user' column is not included in the index
    interaction_matrix = interaction_matrix.reset_index(drop=True)

    # Select rows corresponding to similar users
    selected_rows = interaction_matrix.loc[similar_users]

    # Get column IDs with the 50 highest values in the selected rows
    top_columns = selected_rows.stack().nlargest(50).index.get_level_values(1).tolist()

    print("Top IDs with the 50 highest values:")
    print(top_columns)
    return top_columns

highest_restaurants = get_highest_rated(imdf_r, similar_users)
highest_activities = get_highest_rated(imdf_a, similar_users)

# st.write(highest_restaurants)
# st.write(highest_activities)




def load_data2():
    data = pd.read_csv('combined_restaurant.csv')
    return data
restaurants = load_data2()
restaurants.index += 1 
restaurants.drop(columns = 'Unnamed: 0', inplace= True)

def load_data3():
    data = pd.read_csv('combined_activity.csv')
    return data
activities = load_data3()
activities.index += 1
activities.drop(columns = 'Unnamed: 0', inplace= True)

# st.write(activities.loc[1])
# st.write(restaurants.loc[1])
# st.write(activities.index)

# st.write(highest_activities)


# Assuming "activities" DataFrame has an integer index
# Convert "highest_activities" to integers
highest_activities_int = [int(label) for label in highest_activities]

# Set the index of "activities" DataFrame to match "highest_activities"
activities.set_index('activity', inplace=True)

collaborative_restaurants = restaurants.iloc[highest_restaurants]

collaborative_activities = activities.iloc[highest_activities]
# Select rows from "activities" DataFrame using the updated index
# collaborative_activities = activities.loc[highest_activities_int]

# collaborative_restaurants = restaurants.loc[highest_restaurants]

# st.write(collaborative_restaurants)
# st.write(collaborative_activities)


# restaurant extractor function 
def restaurant_extractor(user):
    cuisine_categories = ['Western', 'Chinese', 'Other', 'Italian', 'Vietnamese', 'Japanese',
       'Singaporean', 'Mexican', 'Indian', 'Malaysian', 'Middle Eastern',
       'Indonesian', 'Spanish', 'Taiwanese', 'French']
    recommendations = []
    for idx, row in restaurants.iterrows():
        cuisine_vector = pd.Series(0, index = cuisine_categories)
        for cuisine in row['cuisine category'].split(', '):
            cuisine_vector[cuisine] = 1
        recommendation_score = np.dot(user.values, cuisine_vector.values)
        recommendations.append((row['name'], recommendation_score))
    
    recommendations_df = pd.DataFrame(recommendations, columns =['restaurant','recommendation_score'])
    non_zero_recommendations = recommendations_df[recommendations_df['recommendation_score']> 0]
    sorted_recommendations = non_zero_recommendations.sort_values(by='recommendation_score', ascending=False)
    top_50_recommendations = sorted_recommendations.head(50)

    print("\Top 50 Recommendations:")
    print(top_50_recommendations)

    return top_50_recommendations

content_restaurant = restaurant_extractor(wz)
# st.write(wz)
# st.write('content_restaurant:', content_restaurant)



def load_data4():
    data = pd.read_csv('combined_activity1.csv')
    return data
activity1 = load_data4()
# activities1.index += 1
# activities1.drop(columns = 'Unnamed: 0', inplace= True)

#st.write('typeuser:', type(wza))
# Function to extract Activities 
import pandas as pd

def activity_extractor(user):
    # Convert user to DataFrame if it's a dictionary
    if isinstance(user, dict):
        user = pd.Series(user)

    recommendations1 = []

    for idx, row in activity1.iterrows():
        # Initialize activity_vector based on the index of user
        activity_vector = pd.Series(0, index=user.index)
        types = row['type']
        if pd.notna(types):  # Check for missing values
            for type_ in types.split(', '):  # Split types by ', ' if multiple types
                if type_ in user.index:  # Check if type exists in user_profile index
                    activity_vector[type_] = 1  # Set 1 for each activity type present in the row

        recommendation_score1 = np.dot(user.values, activity_vector.values)
        recommendations1.append((row['activity'], recommendation_score1))

    recommendations_df1 = pd.DataFrame(recommendations1, columns=['activity', 'recommendation_score'])
    non_zero_recommendations1 = recommendations_df1[recommendations_df1['recommendation_score'] > 0]
    sorted_recommendations1 = non_zero_recommendations1.sort_values(by='recommendation_score', ascending=False)
    top_50_recommendations1 = sorted_recommendations1.head(50)

    print("\Top 50 Recommendations:")
    print(top_50_recommendations1)

    return top_50_recommendations1


content_activity = activity_extractor(wza)


# st.write(wza)
# st.write('content activity:', content_activity)




#Function to get overlapped restaurants
def overlap_r(content_df, collaborative_df, content_column, collaborative_column, original_data):
    # Find overlapped items
    overlapped = content_df.merge(collaborative_df, left_on=content_column, right_on=collaborative_column, how='inner')

    # If there are fewer than 20 overlapped items
    if len(overlapped) < 20:
        # Fill the remaining slots with items from one dataframe
        remaining_count = 20 - len(overlapped)
        if len(content_df) > remaining_count:
            overlapped = pd.concat([overlapped, content_df.head(remaining_count)])
        else:
            overlapped = pd.concat([overlapped, content_df])
    
    overlapped1 = original_data[original_data['name'].isin(overlapped['restaurant'])]
    

    return overlapped1

overlapped_restaurants = overlap_r(content_restaurant,collaborative_restaurants, 'restaurant', 'name',restaurants)
#st.write('overlapped restaurants:', overlapped_restaurants)

#Function to get overlapped activity
def overlap_a(content_df, collaborative_df, content_column, collaborative_column):
    overlapped = content_df.merge(collaborative_df, left_on=content_column, right_on=collaborative_column, how='inner')

    if len(overlapped) < 20:
        remaining_count = 20 - len(overlapped)
        remaining_items = content_df[~content_df[content_column].isin(overlapped[content_column])].head(remaining_count)
        overlapped = pd.concat([overlapped, remaining_items])

    overlapped1 = activity1[activity1['activity'].isin(overlapped['activity'])]
    return overlapped1.head(20)

overlapped_activities = overlap_a(content_activity,collaborative_activities,'activity','activity')
# st.write('overlapped activities:', overlapped_activities)


# st.write(postal)



coordinates = get_co(postal)

#st.write('coordinates:', coordinates)


# function to calculate distance between two points based on coordinates
def calc_dist(lat1, lon1, lat2, lon2):
    
    # Calculate the distance between the two points
    distance = geodesic((lat1, lon1), (lat2, lon2)).kilometers
    return distance

#function to get final recommend items
def rec(postal, userprofile, usera):
    # Calculate distance to location for each item
    overlapped_restaurants['distance'] = overlapped_restaurants.apply(lambda row: 200 if row['latitude'] == 'not available' or row['longitude'] == 'not available' else calc_dist(postal[0], postal[1], row['latitude'], row['longitude']), axis=1)
    overlapped_activities['distance'] = overlapped_activities.apply(lambda row: 200 if row['latitude'] == 'not available' or row['longitude'] == 'not available' else calc_dist(postal[0], postal[1], row['latitude'], row['longitude']), axis=1)


    #overlapped_restaurants['distance'] = overlapped_restaurants.apply(lambda row: 200 if row['latitude'] == 'not available' or row['longitude'] == 'not available' else calc_dist(postal[0], postal[1], row['latitude'], row['longitude']), axis=1)
    #overlapped_activities['distance'] = overlapped_activities.apply(lambda row: 200 if row['latitude'] == 'not available' or row['longitude'] == 'not available' else calc_dist(postal[0], postal[1], row['latitude'], row['longitude']), axis=1)

    # Calculate activity score
    def calculate_score(row):
        score = 0
        for activity, weight in usera.items():
            if weight != 0 and activity in row['type']:
                score += weight
        return score

    overlapped_activities['activity_score'] = overlapped_activities.apply(calculate_score, axis=1)

    # Initialize StandardScaler
    ss = StandardScaler()

    # Fit and transform the 'price' column for restaurants
    overlapped_restaurants['price'] = pd.to_numeric(overlapped_restaurants['price'], errors='coerce')
    overlapped_restaurants['price'] = overlapped_restaurants['price'].replace(0, np.nan)  # Replace 0 values with NaN
    overlapped_restaurants['normalized_price'] = ss.fit_transform(overlapped_restaurants[['price']])

    # Fit and transform the 'rating' column for restaurants
    overlapped_restaurants['normalized_rating'] = ss.fit_transform(overlapped_restaurants[['rating']])

    # Fit and transform the 'distance' column for restaurants
    overlapped_restaurants['normalized_distance'] = ss.fit_transform(overlapped_restaurants[['distance']])

    # Define weights for user preferences
    profile_to_weight = {3: 0.2, 2: 0.3, 1: 0.4}
    budget_weight = profile_to_weight.get(userprofile[0], 0)
    food_weight = profile_to_weight.get(userprofile[1], 0)
    distance_weight = 1 - budget_weight - food_weight
    
    # Calculate overall score for restaurants
    overlapped_restaurants['overall_score'] = (
        distance_weight * 1 / overlapped_restaurants['distance'] +
        food_weight * overlapped_restaurants['rating'] +
        budget_weight * (1 / overlapped_restaurants['price'])
    )

    # Define weights for user activities
    activity_to_weight = {1: 0.5, 2: 0.3, 3: 0.1}
    activity_weight = activity_to_weight.get(userprofile[2], 0)
    distance_r_weight = 1 - activity_weight

    # Calculate overall score for activities
    overlapped_activities['overall_score'] = (
        distance_r_weight * 1 / overlapped_activities['distance'] +
        activity_weight * overlapped_activities['activity_score']
    )

    # Sort restaurants and activities by overall score
    sorted_restaurants = overlapped_restaurants.sort_values(by='overall_score', ascending=False)
    sorted_activities = overlapped_activities.sort_values(by='overall_score', ascending=False)

    # Print top 5 restaurants and activities
    print("Top 5 restaurants:")
    print(sorted_restaurants[['name', 'price', 'distance']].head(5))
    print('Top 5 activities:')
    print(sorted_activities[['activity', 'type', 'distance']].head(5))

    return sorted_restaurants, sorted_activities

#ecommended_r, recommended_a = rec(coordinates, wz1, wza)

# Assuming 'coordinates' contains the extracted coordinates from the postal code
user_has_location = coordinates is not None

if user_has_location:
    recommended_r, recommended_a = rec(coordinates, wz1, wza)
    
    st.write('Recommended Restaurants:', recommended_r[['name','cuisine category', 'price', 'distance','location']].head())
    st.write('Recommended Activities:', recommended_a[['activity','distance','type','location']].head())
    recommended_r['latitude'] = recommended_r['latitude'].replace('not available', np.nan)
    recommended_r['longitude'] = recommended_r['longitude'].replace('not available', np.nan)
    recommended_r['latitude'] = recommended_r['latitude'].astype(float)
    recommended_r['longitude'] = recommended_r['longitude'].astype(float)
    recommended_a['latitude'] = recommended_a['latitude'].replace('not available', np.nan)
    recommended_a['longitude'] = recommended_a['longitude'].replace('not available', np.nan)
    recommended_a['latitude'] = recommended_a['latitude'].astype(float)
    recommended_a['longitude'] = recommended_a['longitude'].astype(float)
    recommended_locations = recommended_r.dropna(subset=['latitude', 'longitude'])
    recommended_locations1 = recommended_a.dropna(subset=['latitude', 'longitude'])

    st.write("Here are the Restaurants' and Activities' location on the map")
    st.write('Recommended restaurants locations:')
    st.map(recommended_locations[['latitude', 'longitude']].head())

    st.write('Recommended activities locations:')
    st.map(recommended_locations1[['latitude', 'longitude']].head())

else:
    st.write('Please input your location to get recommendations.')















