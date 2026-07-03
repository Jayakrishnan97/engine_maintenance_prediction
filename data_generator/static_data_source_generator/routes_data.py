import pandas as pd

domestic_routes = [
    {"route_id":"R001","origin":"DEL","destination":"BOM","distance_nm":620,"typical_duration_min":125,"route_type":"DOMESTIC"},
    {"route_id":"R002","origin":"DEL","destination":"BLR","distance_nm":940,"typical_duration_min":170,"route_type":"DOMESTIC"},
    {"route_id":"R003","origin":"DEL","destination":"HYD","distance_nm":680,"typical_duration_min":135,"route_type":"DOMESTIC"},
    {"route_id":"R004","origin":"DEL","destination":"MAA","distance_nm":950,"typical_duration_min":170,"route_type":"DOMESTIC"},
    {"route_id":"R005","origin":"DEL","destination":"CCU","distance_nm":710,"typical_duration_min":130,"route_type":"DOMESTIC"},
    {"route_id":"R006","origin":"DEL","destination":"AMD","distance_nm":420,"typical_duration_min":90,"route_type":"DOMESTIC"},
    {"route_id":"R007","origin":"DEL","destination":"GOX","distance_nm":820,"typical_duration_min":150,"route_type":"DOMESTIC"},
    {"route_id":"R008","origin":"DEL","destination":"COK","distance_nm":1115,"typical_duration_min":190,"route_type":"DOMESTIC"},

    {"route_id":"R009","origin":"BOM","destination":"BLR","distance_nm":455,"typical_duration_min":95,"route_type":"DOMESTIC"},
    {"route_id":"R010","origin":"BOM","destination":"HYD","distance_nm":335,"typical_duration_min":80,"route_type":"DOMESTIC"},
    {"route_id":"R011","origin":"BOM","destination":"MAA","distance_nm":565,"typical_duration_min":115,"route_type":"DOMESTIC"},
    {"route_id":"R012","origin":"BOM","destination":"CCU","distance_nm":900,"typical_duration_min":160,"route_type":"DOMESTIC"},
    {"route_id":"R013","origin":"BOM","destination":"GOX","distance_nm":220,"typical_duration_min":60,"route_type":"DOMESTIC"},
    {"route_id":"R014","origin":"BOM","destination":"AMD","distance_nm":240,"typical_duration_min":60,"route_type":"DOMESTIC"},
    {"route_id":"R015","origin":"BOM","destination":"PNQ","distance_nm":65,"typical_duration_min":40,"route_type":"DOMESTIC"},

    {"route_id":"R016","origin":"BLR","destination":"HYD","distance_nm":270,"typical_duration_min":60,"route_type":"DOMESTIC"},
    {"route_id":"R017","origin":"BLR","destination":"MAA","distance_nm":155,"typical_duration_min":50,"route_type":"DOMESTIC"},
    {"route_id":"R018","origin":"BLR","destination":"COK","distance_nm":200,"typical_duration_min":55,"route_type":"DOMESTIC"},
    {"route_id":"R019","origin":"BLR","destination":"GOX","distance_nm":260,"typical_duration_min":60,"route_type":"DOMESTIC"},
    {"route_id":"R020","origin":"BLR","destination":"VTZ","distance_nm":430,"typical_duration_min":90,"route_type":"DOMESTIC"},

    {"route_id":"R021","origin":"HYD","destination":"MAA","distance_nm":275,"typical_duration_min":60,"route_type":"DOMESTIC"},
    {"route_id":"R022","origin":"HYD","destination":"VTZ","distance_nm":285,"typical_duration_min":60,"route_type":"DOMESTIC"},
    {"route_id":"R023","origin":"HYD","destination":"VGA","distance_nm":135,"typical_duration_min":40,"route_type":"DOMESTIC"},
    {"route_id":"R024","origin":"HYD","destination":"CCU","distance_nm":650,"typical_duration_min":120,"route_type":"DOMESTIC"},
    {"route_id":"R025","origin":"HYD","destination":"AMD","distance_nm":480,"typical_duration_min":95,"route_type":"DOMESTIC"},

    {"route_id":"R026","origin":"MAA","destination":"COK","distance_nm":285,"typical_duration_min":60,"route_type":"DOMESTIC"},
    {"route_id":"R027","origin":"MAA","destination":"TRV","distance_nm":330,"typical_duration_min":65,"route_type":"DOMESTIC"},
    {"route_id":"R028","origin":"MAA","destination":"CCU","distance_nm":735,"typical_duration_min":130,"route_type":"DOMESTIC"},
    {"route_id":"R029","origin":"MAA","destination":"GOX","distance_nm":455,"typical_duration_min":90,"route_type":"DOMESTIC"},
    {"route_id":"R030","origin":"MAA","destination":"IXM","distance_nm":215,"typical_duration_min":50,"route_type":"DOMESTIC"},

    {"route_id":"R031","origin":"CCU","destination":"GAU","distance_nm":280,"typical_duration_min":60,"route_type":"DOMESTIC"},
    {"route_id":"R032","origin":"CCU","destination":"BBI","distance_nm":200,"typical_duration_min":55,"route_type":"DOMESTIC"},
    {"route_id":"R033","origin":"CCU","destination":"PAT","distance_nm":255,"typical_duration_min":60,"route_type":"DOMESTIC"},
    {"route_id":"R034","origin":"CCU","destination":"DEL","distance_nm":710,"typical_duration_min":130,"route_type":"DOMESTIC"},
    {"route_id":"R035","origin":"CCU","destination":"VTZ","distance_nm":420,"typical_duration_min":90,"route_type":"DOMESTIC"},

    {"route_id":"R036","origin":"DEL","destination":"DXB","distance_nm":1180,"typical_duration_min":210,"route_type":"INTERNATIONAL"},
    {"route_id":"R037","origin":"BOM","destination":"DXB","distance_nm":1040,"typical_duration_min":180,"route_type":"INTERNATIONAL"},
    {"route_id":"R038","origin":"BLR","destination":"SIN","distance_nm":1720,"typical_duration_min":255,"route_type":"INTERNATIONAL"},
    {"route_id":"R039","origin":"HYD","destination":"AUH","distance_nm":1385,"typical_duration_min":225,"route_type":"INTERNATIONAL"},
    {"route_id":"R040","origin":"MAA","destination":"CMB","distance_nm":350,"typical_duration_min":75,"route_type":"INTERNATIONAL"},
    {"route_id":"R041","origin":"COK","destination":"DXB","distance_nm":1480,"typical_duration_min":240,"route_type":"INTERNATIONAL"},
    {"route_id":"R042","origin":"CCU","destination":"DAC","distance_nm":130,"typical_duration_min":45,"route_type":"INTERNATIONAL"},
    {"route_id":"R043","origin":"DEL","destination":"KTM","distance_nm":435,"typical_duration_min":90,"route_type":"INTERNATIONAL"},
    {"route_id":"R044","origin":"BOM","destination":"MCT","distance_nm":855,"typical_duration_min":150,"route_type":"INTERNATIONAL"},
    {"route_id":"R045","origin":"HYD","destination":"DXB","distance_nm":1370,"typical_duration_min":220,"route_type":"INTERNATIONAL"}
]

international_routes = [
    {
        "route_id": "R046",
        "origin": "DEL",
        "destination": "DXB",
        "distance_nm": 1180,
        "typical_duration_min": 210,
        "route_type": "INTERNATIONAL"
    },
    {
        "route_id": "R047",
        "origin": "BOM",
        "destination": "DXB",
        "distance_nm": 1040,
        "typical_duration_min": 180,
        "route_type": "INTERNATIONAL"
    },
    {
        "route_id": "R048",
        "origin": "BLR",
        "destination": "SIN",
        "distance_nm": 1720,
        "typical_duration_min": 255,
        "route_type": "INTERNATIONAL"
    },
    {
        "route_id": "R049",
        "origin": "HYD",
        "destination": "AUH",
        "distance_nm": 1385,
        "typical_duration_min": 225,
        "route_type": "INTERNATIONAL"
    },
    {
        "route_id": "R050",
        "origin": "MAA",
        "destination": "CMB",
        "distance_nm": 350,
        "typical_duration_min": 75,
        "route_type": "INTERNATIONAL"
    },
    {
        "route_id": "R051",
        "origin": "COK",
        "destination": "DXB",
        "distance_nm": 1480,
        "typical_duration_min": 240,
        "route_type": "INTERNATIONAL"
    },
    {
        "route_id": "R052",
        "origin": "CCU",
        "destination": "DAC",
        "distance_nm": 130,
        "typical_duration_min": 45,
        "route_type": "INTERNATIONAL"
    },
    {
        "route_id": "R053",
        "origin": "DEL",
        "destination": "KTM",
        "distance_nm": 435,
        "typical_duration_min": 90,
        "route_type": "INTERNATIONAL"
    },
    {
        "route_id": "R054",
        "origin": "BOM",
        "destination": "MCT",
        "distance_nm": 855,
        "typical_duration_min": 150,
        "route_type": "INTERNATIONAL"
    },
    {
        "route_id": "R055",
        "origin": "HYD",
        "destination": "DXB",
        "distance_nm": 1370,
        "typical_duration_min": 220,
        "route_type": "INTERNATIONAL"
    },
    {
        "route_id": "R056",
        "origin": "DEL",
        "destination": "BKK",
        "distance_nm": 1590,
        "typical_duration_min": 250,
        "route_type": "INTERNATIONAL"
    },
    {
        "route_id": "R057",
        "origin": "CCU",
        "destination": "BKK",
        "distance_nm": 875,
        "typical_duration_min": 145,
        "route_type": "INTERNATIONAL"
    },
    {
        "route_id": "R058",
        "origin": "MAA",
        "destination": "KUL",
        "distance_nm": 1425,
        "typical_duration_min": 230,
        "route_type": "INTERNATIONAL"
    },
    {
        "route_id": "R059",
        "origin": "BLR",
        "destination": "CMB",
        "distance_nm": 430,
        "typical_duration_min": 85,
        "route_type": "INTERNATIONAL"
    },
    {
        "route_id": "R060",
        "origin": "DEL",
        "destination": "DOH",
        "distance_nm": 1375,
        "typical_duration_min": 230,
        "route_type": "INTERNATIONAL"
    }
]


domestic_route_df = pd.DataFrame(domestic_routes)
international_route_df = pd.DataFrame(international_routes)

routes_final_df = [domestic_route_df, international_route_df]

routes = pd.concat(routes_final_df)

routes.to_csv("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/static_datasource/dim_routes.csv")