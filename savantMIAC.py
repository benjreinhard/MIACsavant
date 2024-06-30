import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV files
hitters = pd.read_csv('/Users/benjaminreinhard/Desktop/hitters.csv')
pitchers = pd.read_csv('/Users/benjaminreinhard/Desktop/pitchers.csv')
team_sheet = pd.read_csv('/Users/benjaminreinhard/Desktop/team.csv')

# Function to calculate percentiles
def calculate_percentiles(data, columns, lower_better=None):
    if lower_better is None:
        lower_better = []
    percentiles = data[columns].rank(pct=True) * 100
    for col in lower_better:
        percentiles[col] = 100 - percentiles[col]
    return percentiles

# Calculate percentiles for hitters and pitchers
hitter_columns = hitters.columns[2:]  # Adjust if necessary
pitcher_columns = pitchers.columns[2:]  # Adjust if necessary
hitters_percentiles = calculate_percentiles(hitters, hitter_columns, lower_better=['Kp', 'KdBB', 'SM'])
pitchers_percentiles = calculate_percentiles(pitchers, pitcher_columns, lower_better=['ERA', 'RA9', 'FIP', 'SIERA', 'BBp', 'HRp', 'WHIP', 'BAVG', 'wOBAAG', 'SLGAG'])

# Function to create percentile bars
def create_percentile_bar(percentiles, actual_values, title):
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.barh(percentiles.index, percentiles, color='gray', alpha=0.3)
    for bar, value, actual in zip(bars, percentiles, actual_values):
        ax.text(value, bar.get_y() + bar.get_height()/2, f'{value:.0f}', va='center', ha='left', color='black')
        ax.text(100, bar.get_y() + bar.get_height()/2, actual, va='center', ha='left', color='black')
    ax.set_xlim(0, 100)
    ax.set_title(title)
    ax.set_xlabel('Percentile')
    return fig

# Streamlit app
st.title('Baseball Performance Dashboard')

tabs = st.tabs(["Hitter", "Pitcher", "Team"])

with tabs[0]:
    st.header("Hitter Statistics")
<<<<<<< HEAD
    selected_team = st.selectbox("Select Team", hitters['Team'].unique())
    team_hitters = hitters[hitters['Team'] == selected_team]
    selected_player = st.selectbox("Select Player", team_hitters['Player'])
    player_stats = team_hitters[team_hitters['Player'] == selected_player].iloc[0, 2:]
    player_percentiles = hitters_percentiles.loc[team_hitters.index[team_hitters['Player'] == selected_player]].iloc[0]
    fig = create_percentile_bar(player_percentiles, player_stats, f"{selected_player} - {selected_team} Hitter Statistics")
=======
    hitter_percentiles_display = hitters_percentiles.mean()
    fig = create_percentile_bar(hitter_percentiles_display, hitters.iloc[0, 2:], "Overall MIAC Hitter Statistics")
>>>>>>> cadf2841f0d0826b55ad384aaed26ce8e8d04dcd
    st.pyplot(fig)

with tabs[1]:
    st.header("Pitcher Statistics")
<<<<<<< HEAD
    selected_team = st.selectbox("Select Team", pitchers['Team'].unique())
    team_pitchers = pitchers[pitchers['Team'] == selected_team]
    selected_player = st.selectbox("Select Player", team_pitchers['Player'])
    player_stats = team_pitchers[team_pitchers['Player'] == selected_player].iloc[0, 2:]
    player_percentiles = pitchers_percentiles.loc[team_pitchers.index[team_pitchers['Player'] == selected_player]].iloc[0]
    fig = create_percentile_bar(player_percentiles, player_stats, f"{selected_player} - {selected_team} Pitcher Statistics")
=======
    pitcher_percentiles_display = pitchers_percentiles.mean()
    fig = create_percentile_bar(pitcher_percentiles_display, pitchers.iloc[0, 2:], "Overall MIAC Pitcher Statistics")
>>>>>>> cadf2841f0d0826b55ad384aaed26ce8e8d04dcd
    st.pyplot(fig)

with tabs[2]:
    st.header("Team Statistics")
<<<<<<< HEAD
    selected_team = st.selectbox("Select Team", team_sheet['Team'].unique())
    team_stats = team_sheet[team_sheet['Team'] == selected_team].iloc[0, 1:]
    team_percentiles = calculate_percentiles(team_sheet, team_stats.index).loc[team_sheet.index[team_sheet['Team'] == selected_team]].iloc[0]
    fig = create_percentile_bar(team_percentiles, team_stats, f"{selected_team} Team Statistics")
    st.pyplot(fig)
=======
    st.dataframe(team_sheet)
>>>>>>> cadf2841f0d0826b55ad384aaed26ce8e8d04dcd

# Run the app with `streamlit run app.py` (make sure to adjust the file path as needed)
