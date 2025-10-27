[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-RandomForest-green)](https://scikit-learn.org/)
[![Data Analysis](https://img.shields.io/badge/DataAnalysis-Pandas-orange)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# IPL Cricket Analytics 🏏

## 📋 Table of Contents
- [What is this project?](#what-is-this-project)
- [What did I analyze?](#what-did-i-analyze)
- [Files in this project](#files-in-this-project)
- [How to run this?](#how-to-run-this)
- [What I learned](#what-i-learned)
- [Contact](#contact)

---

## What is this project?
This is a data analysis project about Indian Premier League (IPL) cricket.

## What did I analyze?
- IPL matches from 2007-2024
- Team performance
- Player statistics
- Match predictions using Machine Learning

## Files in this project
- `notebooks/01_data_exploration.ipynb` – Main analysis notebook
- `data/matches.csv` – Match data
- `data/deliveries.csv` – Ball-by-ball data
- `outputs/figures/` – All charts and visualizations

## 📊 Visualizations Created

Here are all the charts generated during the analysis:

### Team Analysis

**Top 10 Teams by Wins**
![Top 10 Teams by Wins](outputs/figures/01_top_teams_by_wins.png)

**Win Percentage by Team**
![Win Percentage](outputs/figures/02_win_percentage.png)

**Toss Impact on Match Outcomes**
![Toss Impact](outputs/figures/03_toss_impact.png)

**Toss Decisions: Bat vs Field**
![Toss Decisions](outputs/figures/04_toss_decisions.png)

**Top 10 Venues**
![Top Venues](outputs/figures/05_top_venues.png)

### Player Analysis

**Top 15 Batsmen by Total Runs**
![Top Batsmen by Runs](outputs/figures/06_top_batsmen_by_runs.png)

**Top 15 Bowlers by Total Wickets**
![Top Bowlers by Wickets](outputs/figures/07_top_bowlers_by_wickets.png)

**Centuries vs Fifties**
![Centuries vs Fifties](outputs/figures/08_centuries_vs_fifties.png)

**Average Runs per Match**
![Average Runs per Match](outputs/figures/09_average_runs_per_match.png)

**Best Economy Rate Bowlers**
![Best Economy Rate](outputs/figures/10_best_economy_rate.png)

### Machine Learning

**Confusion Matrix**
![Confusion Matrix](outputs/figures/11_confusion_matrix.png)

**Feature Importance for Match Outcome**
![Feature Importance](outputs/figures/12_feature_importance.png)

## 📌 Key Insights

- Mumbai Indians and Kolkata Knight Riders lead in total wins.
- Winning the toss increases match win probability (~52%).
- Top batsmen average 35+ runs per match, with 100+ IPL centuries recorded.
- Best bowling economy rates are around 6-7 runs per over.
- The Random Forest machine learning model achieved ~85% accuracy predicting IPL match winners.


## How to run this?
1. Install Python 3.11
2. Install libraries: `pip install -r requirements.txt`
3. Run Jupyter: `jupyter notebook`
4. Open `notebooks/01_data_exploration.ipynb`

## What I learned
- Data analysis with Pandas
- Creating visualizations with Matplotlib
- Machine Learning with Scikit-learn
- GitHub version control

## Contact
**Author:** Sai Tejeswar  
**GitHub:** [@saitej0912](https://github.com/saitej0912)  
**Email:** saitej0912@gmail.com  


