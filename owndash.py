import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Define the file paths
hitters_file_path = '/Users/benjaminreinhard/Desktop/AppleSox Stream Lit App - hitters.csv'
pitchers_file_path = '/Users/benjaminreinhard/Desktop/AppleSox Stream Lit App - Pitchers.csv'

# Load the CSV files
hitters_df = pd.read_csv(hitters_file_path)
pitchers_df = pd.read_csv(pitchers_file_path)

# Define the statistics for each type of player based on the provided CSV files
hitters_stats = {
    'higher_is_better': ['wOBA', 'Avg. EV', '90th Perc. EV'],
    'lower_is_better': ['K%', 'BB%', 'Chase %', 'Whiff %']
}

pitchers_stats = {
    'higher_is_better': ['GB%', 'Strike%', 'Avg. Velo', '90th Perc. Velo', 'K%'],
    'lower_is_better': ['wOBA', 'BB%']
}

def display_leaderboard(df, stat, higher_is_better=True):
    if higher_is_better:
        leaderboard = df.nlargest(5, stat)
    else:
        leaderboard = df.nsmallest(5, stat)
    return leaderboard[[df.columns[0], stat]]

# Streamlit app
st.title("Baseball Leaderboard Dashboard")

tab1, tab2, tab3 = st.tabs(["Leaderboards", "Team Stats", "Player Stats"])

with tab1:
    st.header("Hitters Leaderboard")
    for stat in hitters_stats['higher_is_better']:
        st.subheader(f"Top 5 for {stat}")
        st.dataframe(display_leaderboard(hitters_df, stat, higher_is_better=True))

    for stat in hitters_stats['lower_is_better']:
        st.subheader(f"Top 5 for {stat}")
        st.dataframe(display_leaderboard(hitters_df, stat, higher_is_better=False))

    st.header("Pitchers Leaderboard")
    for stat in pitchers_stats['higher_is_better']:
        st.subheader(f"Top 5 for {stat}")
        st.dataframe(display_leaderboard(pitchers_df, stat, higher_is_better=True))

    for stat in pitchers_stats['lower_is_better']:
        st.subheader(f"Top 5 for {stat}")
        st.dataframe(display_leaderboard(pitchers_df, stat, higher_is_better=False))

with tab2:
    st.header("Team Stats")
    st.write("Hitters Team Stats")
    st.dataframe(hitters_df.groupby(hitters_df.columns[0]).mean())

    st.write("Pitchers Team Stats")
    st.dataframe(pitchers_df.groupby(pitchers_df.columns[0]).mean())

with tab3:
    st.header("Player Stats")
    player_type = st.selectbox("Select Player Type", ["Hitter", "Pitcher"])
    if player_type == "Hitter":
        player_name = st.selectbox("Select Player", hitters_df[hitters_df.columns[0]].unique())
        player_stats = hitters_df[hitters_df[hitters_df.columns[0]] == player_name]
        st.subheader(f"Stats for {player_name}")
        st.dataframe(player_stats)
        
        # Plotting the rolling wOBA
        dates = ['5/31', '6/15', 'wOBA']
        player_wOBA = [player_stats['5/31'].values[0], player_stats['6/15'].values[0], player_stats['wOBA'].values[0]]
        team_stats = hitters_df[hitters_df[hitters_df.columns[0]] == 'Team']
        team_wOBA = [team_stats['5/31'].values[0], team_stats['6/15'].values[0], team_stats['wOBA'].values[0]]

        fig, ax = plt.subplots()
        ax.plot(dates, player_wOBA, marker='o', label=player_name)
        ax.plot(dates, team_wOBA, linestyle='--', label='Team Average')
        ax.set_xlabel('Date')
        ax.set_ylabel('wOBA')
        ax.set_title('Rolling wOBA')
        ax.legend()
        st.pyplot(fig)
        
        st.write("Comparison with Team Averages")
        st.dataframe(team_stats)
    else:
        player_name = st.selectbox("Select Player", pitchers_df[pitchers_df.columns[0]].unique())
        player_stats = pitchers_df[pitchers_df[pitchers_df.columns[0]] == player_name]
        st.subheader(f"Stats for {player_name}")
        st.dataframe(player_stats)
        st.write("Comparison with Team Averages")
        team_stats = pitchers_df[pitchers_df[pitchers_df.columns[0]] == 'Team']
        st.dataframe(team_stats)
