import pandas as pd

domestic_airports = [
    {
        "airport_code": "DEL",
        "airport_name": "Indira Gandhi International Airport",
        "city": "New Delhi",
        "state": "Delhi",
        "country": "India",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 14534,
        "elevation_ft": 777
    },
    {
        "airport_code": "BOM",
        "airport_name": "Chhatrapati Shivaji Maharaj International Airport",
        "city": "Mumbai",
        "state": "Maharashtra",
        "country": "India",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 11499,
        "elevation_ft": 39
    },
    {
        "airport_code": "BLR",
        "airport_name": "Kempegowda International Airport",
        "city": "Bengaluru",
        "state": "Karnataka",
        "country": "India",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 13123,
        "elevation_ft": 3000
    },
    {
        "airport_code": "HYD",
        "airport_name": "Rajiv Gandhi International Airport",
        "city": "Hyderabad",
        "state": "Telangana",
        "country": "India",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 13976,
        "elevation_ft": 2024
    },
    {
        "airport_code": "MAA",
        "airport_name": "Chennai International Airport",
        "city": "Chennai",
        "state": "Tamil Nadu",
        "country": "India",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 12467,
        "elevation_ft": 52
    },
    {
        "airport_code": "CCU",
        "airport_name": "Netaji Subhas Chandra Bose International Airport",
        "city": "Kolkata",
        "state": "West Bengal",
        "country": "India",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 11900,
        "elevation_ft": 16
    },
    {
        "airport_code": "COK",
        "airport_name": "Cochin International Airport",
        "city": "Kochi",
        "state": "Kerala",
        "country": "India",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 11155,
        "elevation_ft": 30
    },
    {
        "airport_code": "GOI",
        "airport_name": "Dabolim Airport",
        "city": "Goa",
        "state": "Goa",
        "country": "India",
        "airport_type": "DOMESTIC",
        "runway_length_ft": 11345,
        "elevation_ft": 150
    },
    {
        "airport_code": "GOX",
        "airport_name": "Manohar International Airport",
        "city": "Goa",
        "state": "Goa",
        "country": "India",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 12300,
        "elevation_ft": 187
    },
    {
        "airport_code": "AMD",
        "airport_name": "Sardar Vallabhbhai Patel International Airport",
        "city": "Ahmedabad",
        "state": "Gujarat",
        "country": "India",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 11781,
        "elevation_ft": 189
    },
    {
        "airport_code": "PNQ",
        "airport_name": "Pune Airport",
        "city": "Pune",
        "state": "Maharashtra",
        "country": "India",
        "airport_type": "DOMESTIC",
        "runway_length_ft": 8330,
        "elevation_ft": 1942
    },
    {
        "airport_code": "LKO",
        "airport_name": "Chaudhary Charan Singh International Airport",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "country": "India",
        "airport_type": "DOMESTIC",
        "runway_length_ft": 9000,
        "elevation_ft": 404
    },
    {
        "airport_code": "TRV",
        "airport_name": "Trivandrum International Airport",
        "city": "Thiruvananthapuram",
        "state": "Kerala",
        "country": "India",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 11178,
        "elevation_ft": 14
    },
    {
        "airport_code": "IXC",
        "airport_name": "Chandigarh International Airport",
        "city": "Chandigarh",
        "state": "Chandigarh",
        "country": "India",
        "airport_type": "DOMESTIC",
        "runway_length_ft": 10000,
        "elevation_ft": 1012
    },
    {
        "airport_code": "IXM",
        "airport_name": "Madurai Airport",
        "city": "Madurai",
        "state": "Tamil Nadu",
        "country": "India",
        "airport_type": "DOMESTIC",
        "runway_length_ft": 7500,
        "elevation_ft": 459
    },
    {
        "airport_code": "VGA",
        "airport_name": "Vijayawada International Airport",
        "city": "Vijayawada",
        "state": "Andhra Pradesh",
        "country": "India",
        "airport_type": "DOMESTIC",
        "runway_length_ft": 11155,
        "elevation_ft": 82
    },
    {
        "airport_code": "VTZ",
        "airport_name": "Visakhapatnam International Airport",
        "city": "Visakhapatnam",
        "state": "Andhra Pradesh",
        "country": "India",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 10007,
        "elevation_ft": 16
    },
    {
        "airport_code": "NAG",
        "airport_name": "Dr. Babasaheb Ambedkar International Airport",
        "city": "Nagpur",
        "state": "Maharashtra",
        "country": "India",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 10502,
        "elevation_ft": 1033
    },
    {
        "airport_code": "IDR",
        "airport_name": "Devi Ahilyabai Holkar Airport",
        "city": "Indore",
        "state": "Madhya Pradesh",
        "country": "India",
        "airport_type": "DOMESTIC",
        "runway_length_ft": 9000,
        "elevation_ft": 1850
    },
    {
        "airport_code": "BBI",
        "airport_name": "Biju Patnaik International Airport",
        "city": "Bhubaneswar",
        "state": "Odisha",
        "country": "India",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 9000,
        "elevation_ft": 138
    },
    {
        "airport_code": "PAT",
        "airport_name": "Jay Prakash Narayan Airport",
        "city": "Patna",
        "state": "Bihar",
        "country": "India",
        "airport_type": "DOMESTIC",
        "runway_length_ft": 6800,
        "elevation_ft": 170
    },
    {
        "airport_code": "JAI",
        "airport_name": "Jaipur International Airport",
        "city": "Jaipur",
        "state": "Rajasthan",
        "country": "India",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 11178,
        "elevation_ft": 1263
    },
    {
        "airport_code": "SXR",
        "airport_name": "Sheikh ul-Alam International Airport",
        "city": "Srinagar",
        "state": "Jammu and Kashmir",
        "country": "India",
        "airport_type": "DOMESTIC",
        "runway_length_ft": 12100,
        "elevation_ft": 5429
    },
    {
        "airport_code": "GAU",
        "airport_name": "Lokpriya Gopinath Bordoloi International Airport",
        "city": "Guwahati",
        "state": "Assam",
        "country": "India",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 10200,
        "elevation_ft": 162
    },
    {
        "airport_code": "IXZ",
        "airport_name": "Veer Savarkar International Airport",
        "city": "Port Blair",
        "state": "Andaman and Nicobar Islands",
        "country": "India",
        "airport_type": "DOMESTIC",
        "runway_length_ft": 10800,
        "elevation_ft": 14
    }
]

international_airports = [
    {
        "airport_code": "DXB",
        "airport_name": "Dubai International Airport",
        "city": "Dubai",
        "state": "Dubai",
        "country": "United Arab Emirates",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 14764,
        "elevation_ft": 62
    },
    {
        "airport_code": "AUH",
        "airport_name": "Zayed International Airport",
        "city": "Abu Dhabi",
        "state": "Abu Dhabi",
        "country": "United Arab Emirates",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 13451,
        "elevation_ft": 88
    },
    {
        "airport_code": "DOH",
        "airport_name": "Hamad International Airport",
        "city": "Doha",
        "state": "Doha",
        "country": "Qatar",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 15912,
        "elevation_ft": 13
    },
    {
        "airport_code": "MCT",
        "airport_name": "Muscat International Airport",
        "city": "Muscat",
        "state": "Muscat",
        "country": "Oman",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 13123,
        "elevation_ft": 49
    },
    {
        "airport_code": "SIN",
        "airport_name": "Singapore Changi Airport",
        "city": "Singapore",
        "state": "Singapore",
        "country": "Singapore",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 13123,
        "elevation_ft": 22
    },
    {
        "airport_code": "KUL",
        "airport_name": "Kuala Lumpur International Airport",
        "city": "Kuala Lumpur",
        "state": "Selangor",
        "country": "Malaysia",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 13648,
        "elevation_ft": 69
    },
    {
        "airport_code": "BKK",
        "airport_name": "Suvarnabhumi Airport",
        "city": "Bangkok",
        "state": "Bangkok",
        "country": "Thailand",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 13123,
        "elevation_ft": 5
    },
    {
        "airport_code": "CMB",
        "airport_name": "Bandaranaike International Airport",
        "city": "Colombo",
        "state": "Western Province",
        "country": "Sri Lanka",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 10991,
        "elevation_ft": 30
    },
    {
        "airport_code": "KTM",
        "airport_name": "Tribhuvan International Airport",
        "city": "Kathmandu",
        "state": "Bagmati",
        "country": "Nepal",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 10007,
        "elevation_ft": 4390
    },
    {
        "airport_code": "DAC",
        "airport_name": "Hazrat Shahjalal International Airport",
        "city": "Dhaka",
        "state": "Dhaka",
        "country": "Bangladesh",
        "airport_type": "INTERNATIONAL",
        "runway_length_ft": 10500,
        "elevation_ft": 27
    },
    {
    "airport_code": "MLE",
    "airport_name": "Velana International Airport",
    "city": "Malé",
    "state": "Kaafu Atoll",
    "country": "Maldives",
    "airport_type": "INTERNATIONAL",
    "runway_length_ft": 11155,
    "elevation_ft": 6
},
{
    "airport_code": "CGP",
    "airport_name": "Shah Amanat International Airport",
    "city": "Chattogram",
    "state": "Chattogram",
    "country": "Bangladesh",
    "airport_type": "INTERNATIONAL",
    "runway_length_ft": 9650,
    "elevation_ft": 12
}
]

domestic_df = pd.DataFrame(domestic_airports)
international_df = pd.DataFrame(international_airports)

airports_final_df = [domestic_df, international_df]

airports = pd.concat(airports_final_df)

airports.to_csv("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/static_datasource/dim_airports.csv")