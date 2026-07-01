import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)
data = response.json()

print(data.keys())


nav_df = pd.DataFrame(data["data"])

print(nav_df.head())

nav_df.to_csv(
    "data/raw/HDFC_Top100_live.csv",
    index=False
)


funds = {
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_Large_Cap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

import requests
import pandas as pd

for name, code in funds.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data["data"])

    df.to_csv(
        f"data/raw/{name}.csv",
        index=False
    )

    print(f"{name} downloaded.")

    