# -*- coding: <UTF-8> -*-
import cloudscraper
import pandas as pd
from bs4 import BeautifulSoup
from scrapeWebsite import getInsertBattingString
from scrapeWebsite import getInsertPitchingString

from scanTables import getPitchingDF

def main():
    urlFrame = "https://www.baseball-reference.com/teams/"
    teamCodes = ['PHI', 'NYM', 'MIA', 'ATL', 'WSN', 'CHC', 'MIL', 'STL', 'CIN', 'PIT', 'LAD', 'SDP', 'SFG', 'ARI', 'COL', 'TOR', 'NYY', 'BOS', 'TBR', 'BAL', 'DET', 'MIN', 'CLE', 'KCR', 'CHW', 'HOU', 'SEA', 'TEX', 'LAA', 'ATH']
    # teamCodes = ['LAA']
    for team in teamCodes:
        # stmt=getInsertBattingString(urlFrame, team, '2025')
        stmt=getInsertPitchingString(urlFrame, team, '2025')
        with open('insertStatements.sql', 'a', encoding="utf-8") as f:
            f.write(stmt)


if __name__ == "__main__":
    main()