# Databall headshot badges

- `circle/<image_id>.png` — status circle badge (team colour + logo; COACH / LEGEND / MEDIA tags)
- `rect/<image_id>.png` — soccer jersey / manager-jacket bust (350x254)
- `databall_headshot_links.csv` — one row per person with both links
- `badges_lookup.csv` — Name → circle/jersey link (one row per name) for Google Sheets `IMPORTDATA`

Google Sheets: `=IMAGE("https://raw.githubusercontent.com/QuintLeale/databall-headshots/main/circle/bukayo-saka--soccer.png")`
