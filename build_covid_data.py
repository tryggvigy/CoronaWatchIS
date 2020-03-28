from pathlib import Path
import requests

BASE_URL = "https://docs.google.com/spreadsheets/d/1xgDhtejTtcyy6EN5dbDp5W3TeJhKFRRgm6Xk0s0YFeA/export?format=csv"
SMIT_SHEET = f"{BASE_URL}&gid=0"
SPITALI_SHEET = f"{BASE_URL}&gid=1167203444"
ALDUR_SHEET = f"{BASE_URL}&gid=2147090221"

def build_data():
    print("Downloading")
    cases_resp=requests.get(url=SMIT_SHEET)
    hospital_resp=requests.get(url=SPITALI_SHEET)
    age_response=requests.get(url=ALDUR_SHEET)

    # create data folder
    Path('data').mkdir(parents=True, exist_ok=True)

    print("Updating Datasets")

    open(str(Path('data', 'covid_in_is.cvs')), "wb").write(cases_resp.content)
    open(str(Path('data', 'covid_in_is_hosp.cvs')), "wb").write(hospital_resp.content)
    open(str(Path('data', 'covid_in_is_age.cvs')), "wb").write(age_response.content)

    print("Success")

if __name__ == '__main__':
    build_data()
