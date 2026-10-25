# Databall headshot badges

- `circle/<image_id>.png` — status circle badge (team colour + logo; COACH / LEGEND / MEDIA tags)
- `rect/<image_id>.png` — soccer jersey / manager-jacket bust (350x254)
- `databall_headshot_links.csv` — one row per person with both links
- `badges_lookup.csv` — Name → circle/jersey link (one row per name) for Google Sheets `IMPORTDATA`

Google Sheets: `=IMAGE("https://raw.githubusercontent.com/QuintLeale/databall-headshots/main/circle/bukayo-saka--soccer.png")`

## Master lookups (Oct 2026)

- `people_images_master.csv`: one row per person (27,093). `Databall_ID` is the file name in `circle/` and `rect/`.
  IDs to separate people who share a name: `Wiki_Title`, `Wikidata_QID`, `ESPN_ID`, `FotMob_ID`, `Birth_Date`, `Match_Key` (Name | Sport | League), `Match_Key_Birth` (Name | Sport | Birth year), `Same_Name_Count`, `Other_Names`.
  Images: `IMG_Circle`, `IMG_Jersey`, `IMG_Original` (photo the badge was built from), `IMG_Best_Master`, `IMG_ESPN`, `IMG_Official`, `IMG_Fox`, `IMG_School`, `IMG_Wiki`, `IMG_Other`, `IMG_Prev`.
  Fallbacks: `IMG_Team_Logo`, `IMG_League_Logo`, `IMG_Flag`, `IMG_Agency_Logo`, `IMG_Sport_Badge`.
- `entity_images_master.csv`: teams, leagues/conferences, agencies, media, venues, brands, awards, events, flags, metros, sports, trophies (6,981 rows).
- `entity/sport`, `entity/metro`, `entity/venue`: hosted PNG badges (the originals were inline SVG, which Sheets can't show).
