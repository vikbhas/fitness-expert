import openai

# Function to get user details
def get_user_details():
    user_details = {}

    # Personal Information
    user_details['age'] = int(input("Enter your age: "))
    user_details['gender'] = input("Enter your gender (Male/Female): ")
    user_details['height'] = float(input("Enter your height in cm: "))
    user_details['current_weight'] = float(input("Enter your current weight in kg: "))
    user_details['target_weight'] = float(input("Enter your target weight in kg: "))

    # Activity Level
    user_details['activity_level'] = input("Describe your typical daily activity (sedentary, light activity, moderate activity, very active): ")
    user_details['exercise_routine'] = input("Do you currently exercise? If yes, describe the type of exercise and how often: ")
    user_details['physical_limitations'] = input("Do you have any physical limitations or injuries? (yes/no): ")
    user_details['physical_limitations_details'] = input("If yes, please describe: ") if user_details['physical_limitations'].lower() == 'yes' else "None"

    # Dietary Habits
    user_details['diet'] = input("Describe your typical daily meals and snacks: ")
    user_details['dietary_restrictions'] = input("Do you have any dietary restrictions or preferences? (e.g., vegetarian, vegan, gluten-free, lactose intolerant): ")
    user_details['water_intake'] = float(input("How much water do you drink daily in liters? "))
    user_details['beverage_consumption'] = input("Do you consume alcohol, caffeine, or sugary drinks? If yes, how much?: ")

    # Goals and Preferences
    user_details['fitness_goal'] = input("What are your primary fitness goals? (e.g., weight loss, muscle gain, improve endurance, overall fitness): ")
    user_details['exercise_preferences'] = input("Do you prefer certain types of exercise? (e.g., cardio, strength training, yoga, sports): ")
    user_details['exercise_commitment'] = int(input("How many days per week can you commit to exercising? "))
    user_details['exercise_duration'] = int(input("How long can you exercise each day (in minutes)? "))

    return user_details


# Function to call OpenAI API and get recommendations
def get_recommendations(user_details):
    openai.api_key = 'your_openai_api_key_here'  # Replace with your actual OpenAI API key

    prompt = f"""
    The user has provided the following details:
    Age: {user_details['age']}
    Gender: {user_details['gender']}
    Height: {user_details['height']} cm
    Current Weight: {user_details['current_weight']} kg
    Target Weight: {user_details['target_weight']} kg
    Activity Level: {user_details['activity_level']}
    Exercise Routine: {user_details['exercise_routine']}
    Physical Limitations: {user_details['physical_limitations_details']}
    Typical Diet: {user_details['diet']}
    Dietary Restrictions: {user_details['dietary_restrictions']}
    Water Intake: {user_details['water_intake']} liters
    Beverage Consumption: {user_details['beverage_consumption']}
    Fitness Goal: {user_details['fitness_goal']}
    Exercise Preferences: {user_details['exercise_preferences']}
    Exercise Commitment: {user_details['exercise_commitment']} days per week
    Exercise Duration: {user_details['exercise_duration']} minutes per day

    Based on these details, please provide a personalized workout schedule and diet plan to help the user achieve their fitness goals.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a fitness expert."},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content']


if __name__ == "__main__":
    user_details = get_user_details()
    recommendations = get_recommendations(user_details)
    print("\nPersonalized Fitness Recommendations:\n")
    print(recommendations)
