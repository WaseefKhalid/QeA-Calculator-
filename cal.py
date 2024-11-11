import streamlit as st

# Set the title of the Streamlit app
st.title("Quaid-e-Azam Trophy Points Calculator")

# Inputs for match result
st.header("Match Result Points")
match_result = st.selectbox(
    "Select the match result:",
    ["Outright Win", "Drawn Game", "Tied Game", "Abandoned Game"]
)

# Points calculation based on match result
if match_result == "Outright Win":
    result_points = 16
elif match_result == "Drawn Game":
    result_points = 5
elif match_result == "Tied Game":
    result_points = 8
else:
    result_points = 5

st.write(f"Points for match result: {result_points}")

# Additional winning bonus points
st.header("Winning Bonus Points")
winning_bonus = st.selectbox(
    "Did the team win with any bonus points?",
    ["None", "Win after Follow-On", "Win with an Innings Margin", "Saved the Match after Follow-On"]
)

# Points for winning bonus
if winning_bonus == "Win after Follow-On":
    bonus_points = 2
elif winning_bonus == "Win with an Innings Margin":
    bonus_points = 1
elif winning_bonus == "Saved the Match after Follow-On":
    bonus_points = 1
else:
    bonus_points = 0

st.write(f"Bonus points for win: {bonus_points}")

# Batting points calculation
st.header("Batting Points (First Innings Only)")
batting_runs = st.number_input("Enter the total runs scored in the first innings:", min_value=0)
overs_played = st.number_input("Enter the overs played in the first innings:", min_value=0)

# Calculate batting points based on runs and overs
batting_points = 0
if overs_played <= 100:
    if batting_runs >= 400:
        batting_points = 5
    elif batting_runs >= 350:
        batting_points = 4
    elif batting_runs >= 300:
        batting_points = 3
    elif batting_runs >= 250:
        batting_points = 2
    elif batting_runs >= 200:
        batting_points = 1

st.write(f"Batting points: {batting_points}")

# Bowling points calculation
st.header("Bowling Points (First Innings Only)")
wickets_taken = st.number_input("Enter the number of wickets taken in the first innings:", min_value=0, max_value=10)
opponent_runs = st.number_input("Enter the runs scored by the opponent in the first innings:", min_value=0)
opponent_overs = st.number_input("Enter the overs bowled to the opponent:", min_value=0)

# Calculate bowling points based on wickets taken and opponent's runs
bowling_points = 0
if opponent_overs <= 100:
    if wickets_taken >= 8:
        bowling_points += 3
    elif wickets_taken >= 6:
        bowling_points += 2
    elif wickets_taken >= 3:
        bowling_points += 1

    if opponent_runs <= 200:
        bowling_points += 3
    elif opponent_runs <= 250:
        bowling_points += 2
    elif opponent_runs <= 300:
        bowling_points += 1

st.write(f"Bowling points: {bowling_points}")

# Calculate total points
total_points = result_points + bonus_points + batting_points + bowling_points
st.header(f"Total Points: {total_points}")
