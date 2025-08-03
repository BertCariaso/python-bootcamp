country_codes={
    "PH":"Philippines",
    "US": "United States",
    "SG" : "Singapore",
    "AU": "Australia"
}

country_code=input("Enter country code: ")
"""print(country_codes[country_code])"""

print(country_codes.get(country_code,"unknown"))







