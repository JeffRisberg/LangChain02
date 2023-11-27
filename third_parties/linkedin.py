import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    # api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    api_endpoint = "https://gist.githubusercontent.com/JeffRisberg/c978d2f02777207b29ff8a824dbd6533/raw"
    # header_dict = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
    header_dict = {}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dict
    )

    print(response)
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
           and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
