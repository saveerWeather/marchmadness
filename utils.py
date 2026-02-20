import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent / 'data'

def load_data():
    DATA = {}
    DATA['m_teams'] = pd.read_csv(DATA_DIR / 'MTeams.csv')
    DATA['w_teams'] = pd.read_csv(DATA_DIR / 'WTeams.csv')
    DATA['m_regular'] = pd.read_csv(DATA_DIR / 'MRegularSeasonCompactResults.csv')
    DATA['w_regular'] = pd.read_csv(DATA_DIR / 'WRegularSeasonCompactResults.csv')
    DATA['m_tourney'] = pd.read_csv(DATA_DIR / 'MNCAATourneyCompactResults.csv')
    DATA['w_tourney'] = pd.read_csv(DATA_DIR / 'WNCAATourneyCompactResults.csv')
    DATA['m_seeds'] = pd.read_csv(DATA_DIR / 'MNCAATourneySeeds.csv')
    DATA['w_seeds'] = pd.read_csv(DATA_DIR / 'WNCAATourneySeeds.csv')
    DATA['sample_sub'] = pd.read_csv(DATA_DIR / 'SampleSubmissionStage1.csv')
    return DATA
