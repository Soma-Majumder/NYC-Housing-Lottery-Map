# NYC Housing Lottery Map

An interactive map of every building advertised in an affordable housing lottery on NYC Housing Connect since July 2020: 2,142 buildings in 1,754 lotteries across all five boroughs.

## What it does

- Colors each borough with its own pastel fill and each pin by lottery status: accepting applications, reviewing applicants, all units filled, or closed.
- Lets you filter by status, borough and senior housing, and search by name or street.
- Shows a building's details when you click its pin: units, application deadline, construction type, and units by income tier.
- Lists every lottery currently open, sorted by deadline, with steps for applying on Housing Connect.

## Run it

Open `index.html` in a browser. It is a single self-contained file with no server and no API keys.

To publish it on GitHub Pages, go to Settings → Pages and set the source to the `main` branch.

## Rebuild after editing data

```
python3 build.py
```

This regenerates `index.html` from `template.html` and the files in `data/`. The file formats are described at the top of `build.py`.

## Data

The data comes from NYC Open Data, published by HPD and pulled October 19, 2026:

- [Advertised Lotteries on Housing Connect By Building](https://data.cityofnewyork.us/d/nibs-na6y)
- [Advertised Lotteries on Housing Connect by Lottery](https://data.cityofnewyork.us/d/vy5i-a666)

The datasets leave out re-rental "mini lotteries" and Mitchell-Lama waiting lists. Check deadlines on [Housing Connect](https://housingconnect.nyc.gov/PublicWeb/) before applying.
