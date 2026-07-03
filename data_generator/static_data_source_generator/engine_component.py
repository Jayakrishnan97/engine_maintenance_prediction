import pandas as pd

components = [

# ========================= FAN MODULE =========================

{
    "component_id": "CMP001",
    "component_name": "Fan Disk",
    "ata_chapter": 72,
    "engine_module": "Fan",
    "maintenance_type": "LLP",
    "life_unit": "FC",
    "life_limit": 20000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP002",
    "component_name": "Fan Shaft",
    "ata_chapter": 72,
    "engine_module": "Fan",
    "maintenance_type": "LLP",
    "life_unit": "FC",
    "life_limit": 30000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP003",
    "component_name": "Fan Blade Set",
    "ata_chapter": 72,
    "engine_module": "Fan",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "NO"
},

{
    "component_id": "CMP004",
    "component_name": "Fan Blade Platform",
    "ata_chapter": 72,
    "engine_module": "Fan",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "NO"
},

{
    "component_id": "CMP005",
    "component_name": "Fan Case",
    "ata_chapter": 72,
    "engine_module": "Fan",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP006",
    "component_name": "Spinner Cone",
    "ata_chapter": 72,
    "engine_module": "Fan",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

# ========================= LPC =========================

{
    "component_id": "CMP007",
    "component_name": "Booster Rotor",
    "ata_chapter": 72,
    "engine_module": "LPC",
    "maintenance_type": "LLP",
    "life_unit": "FC",
    "life_limit": 22000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP008",
    "component_name": "Booster Blade Set",
    "ata_chapter": 72,
    "engine_module": "LPC",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "NO"
},

{
    "component_id": "CMP009",
    "component_name": "Booster Stator Assembly",
    "ata_chapter": 72,
    "engine_module": "LPC",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP010",
    "component_name": "Booster Case",
    "ata_chapter": 72,
    "engine_module": "LPC",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

# ========================= HPC =========================

{
    "component_id": "CMP011",
    "component_name": "HPC Stage 1 Disk",
    "ata_chapter": 72,
    "engine_module": "HPC",
    "maintenance_type": "LLP",
    "life_unit": "FC",
    "life_limit": 18000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP012",
    "component_name": "HPC Stage 2 Disk",
    "ata_chapter": 72,
    "engine_module": "HPC",
    "maintenance_type": "LLP",
    "life_unit": "FC",
    "life_limit": 18000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP013",
    "component_name": "HPC Stage 3 Disk",
    "ata_chapter": 72,
    "engine_module": "HPC",
    "maintenance_type": "LLP",
    "life_unit": "FC",
    "life_limit": 18000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP014",
    "component_name": "HPC Stage 4 Disk",
    "ata_chapter": 72,
    "engine_module": "HPC",
    "maintenance_type": "LLP",
    "life_unit": "FC",
    "life_limit": 18000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP015",
    "component_name": "HPC Stage 5 Disk",
    "ata_chapter": 72,
    "engine_module": "HPC",
    "maintenance_type": "LLP",
    "life_unit": "FC",
    "life_limit": 18000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP016",
    "component_name": "HPC Rotor Shaft",
    "ata_chapter": 72,
    "engine_module": "HPC",
    "maintenance_type": "LLP",
    "life_unit": "FC",
    "life_limit": 25000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP017",
    "component_name": "HPC Blade Set",
    "ata_chapter": 72,
    "engine_module": "HPC",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "NO"
},

{
    "component_id": "CMP018",
    "component_name": "Variable Stator Vane Assembly",
    "ata_chapter": 75,
    "engine_module": "HPC",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP019",
    "component_name": "HPC Case",
    "ata_chapter": 72,
    "engine_module": "HPC",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
}

]
components.extend([

# ========================= COMBUSTOR =========================

{
    "component_id": "CMP020",
    "component_name": "Combustor Liner",
    "ata_chapter": 72,
    "engine_module": "Combustor",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP021",
    "component_name": "Fuel Nozzle Set",
    "ata_chapter": 73,
    "engine_module": "Combustor",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "NO"
},

{
    "component_id": "CMP022",
    "component_name": "Dome Assembly",
    "ata_chapter": 72,
    "engine_module": "Combustor",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP023",
    "component_name": "Swirler Assembly",
    "ata_chapter": 72,
    "engine_module": "Combustor",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "NO"
},

# ========================= HIGH PRESSURE TURBINE =========================

{
    "component_id": "CMP024",
    "component_name": "HPT Stage 1 Disk",
    "ata_chapter": 72,
    "engine_module": "HPT",
    "maintenance_type": "LLP",
    "life_unit": "FC",
    "life_limit": 15000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP025",
    "component_name": "HPT Stage 2 Disk",
    "ata_chapter": 72,
    "engine_module": "HPT",
    "maintenance_type": "LLP",
    "life_unit": "FC",
    "life_limit": 15000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP026",
    "component_name": "HPT Blade Set",
    "ata_chapter": 72,
    "engine_module": "HPT",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "NO"
},

{
    "component_id": "CMP027",
    "component_name": "HPT Nozzle Guide Vanes",
    "ata_chapter": 72,
    "engine_module": "HPT",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "NO"
},

{
    "component_id": "CMP028",
    "component_name": "HPT Shroud",
    "ata_chapter": 72,
    "engine_module": "HPT",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

# ========================= LOW PRESSURE TURBINE =========================

{
    "component_id": "CMP029",
    "component_name": "LPT Shaft",
    "ata_chapter": 72,
    "engine_module": "LPT",
    "maintenance_type": "LLP",
    "life_unit": "FC",
    "life_limit": 25000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP030",
    "component_name": "LPT Stage 1 Disk",
    "ata_chapter": 72,
    "engine_module": "LPT",
    "maintenance_type": "LLP",
    "life_unit": "FC",
    "life_limit": 22000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP031",
    "component_name": "LPT Stage 2 Disk",
    "ata_chapter": 72,
    "engine_module": "LPT",
    "maintenance_type": "LLP",
    "life_unit": "FC",
    "life_limit": 22000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP032",
    "component_name": "LPT Blade Set",
    "ata_chapter": 72,
    "engine_module": "LPT",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "NO"
},

{
    "component_id": "CMP033",
    "component_name": "LPT Nozzle Guide Vanes",
    "ata_chapter": 72,
    "engine_module": "LPT",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "NO"
},

{
    "component_id": "CMP034",
    "component_name": "Turbine Rear Frame",
    "ata_chapter": 72,
    "engine_module": "LPT",
    "maintenance_type": "LLP",
    "life_unit": "FC",
    "life_limit": 30000,
    "repairable": "YES",
    "serialized": "YES"
}

])

components.extend([

# ========================= FUEL SYSTEM =========================

{
    "component_id": "CMP035",
    "component_name": "Fuel Pump",
    "ata_chapter": 73,
    "engine_module": "Fuel System",
    "maintenance_type": "HARD_TIME",
    "life_unit": "FH",
    "life_limit": 12000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP036",
    "component_name": "Hydromechanical Unit (HMU)",
    "ata_chapter": 73,
    "engine_module": "Fuel System",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP037",
    "component_name": "Fuel Filter",
    "ata_chapter": 73,
    "engine_module": "Fuel System",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP038",
    "component_name": "Fuel Shutoff Valve",
    "ata_chapter": 73,
    "engine_module": "Fuel System",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP039",
    "component_name": "Fuel Manifold",
    "ata_chapter": 73,
    "engine_module": "Fuel System",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

# ========================= IGNITION SYSTEM =========================

{
    "component_id": "CMP040",
    "component_name": "Ignition Exciter",
    "ata_chapter": 74,
    "engine_module": "Ignition",
    "maintenance_type": "HARD_TIME",
    "life_unit": "FH",
    "life_limit": 10000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP041",
    "component_name": "Igniter Plug A",
    "ata_chapter": 74,
    "engine_module": "Ignition",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP042",
    "component_name": "Igniter Plug B",
    "ata_chapter": 74,
    "engine_module": "Ignition",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

# ========================= AIR SYSTEM =========================

{
    "component_id": "CMP043",
    "component_name": "Variable Bleed Valve (VBV)",
    "ata_chapter": 75,
    "engine_module": "Air System",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP044",
    "component_name": "VBV Actuator",
    "ata_chapter": 75,
    "engine_module": "Air System",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP045",
    "component_name": "High Stage Bleed Valve",
    "ata_chapter": 75,
    "engine_module": "Air System",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP046",
    "component_name": "Start Valve",
    "ata_chapter": 75,
    "engine_module": "Air System",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

# ========================= EXHAUST SYSTEM =========================

{
    "component_id": "CMP047",
    "component_name": "Exhaust Nozzle",
    "ata_chapter": 78,
    "engine_module": "Exhaust",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP048",
    "component_name": "Exhaust Mixer",
    "ata_chapter": 78,
    "engine_module": "Exhaust",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
}

])

components.extend([

# ========================= OIL SYSTEM =========================

{
    "component_id": "CMP049",
    "component_name": "Oil Pump",
    "ata_chapter": 79,
    "engine_module": "Oil System",
    "maintenance_type": "HARD_TIME",
    "life_unit": "FH",
    "life_limit": 18000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP050",
    "component_name": "Scavenge Pump",
    "ata_chapter": 79,
    "engine_module": "Oil System",
    "maintenance_type": "HARD_TIME",
    "life_unit": "FH",
    "life_limit": 18000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP051",
    "component_name": "Oil Filter",
    "ata_chapter": 79,
    "engine_module": "Oil System",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP052",
    "component_name": "Oil Pressure Transmitter",
    "ata_chapter": 79,
    "engine_module": "Oil System",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP053",
    "component_name": "Oil Temperature Sensor",
    "ata_chapter": 79,
    "engine_module": "Oil System",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

# ========================= ENGINE INDICATING =========================

{
    "component_id": "CMP054",
    "component_name": "EGT Thermocouple Harness",
    "ata_chapter": 77,
    "engine_module": "Engine Indicating",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP055",
    "component_name": "N1 Speed Sensor",
    "ata_chapter": 77,
    "engine_module": "Engine Indicating",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP056",
    "component_name": "N2 Speed Sensor",
    "ata_chapter": 77,
    "engine_module": "Engine Indicating",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP057",
    "component_name": "Vibration Sensor",
    "ata_chapter": 77,
    "engine_module": "Engine Indicating",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP058",
    "component_name": "Chip Detector",
    "ata_chapter": 79,
    "engine_module": "Oil System",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

# ========================= ACCESSORY GEARBOX =========================

{
    "component_id": "CMP059",
    "component_name": "Accessory Gearbox",
    "ata_chapter": 72,
    "engine_module": "Accessory Gearbox",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP060",
    "component_name": "Starter",
    "ata_chapter": 80,
    "engine_module": "Accessory Gearbox",
    "maintenance_type": "HARD_TIME",
    "life_unit": "FH",
    "life_limit": 10000,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP061",
    "component_name": "Integrated Drive Generator (IDG) Drive Pad",
    "ata_chapter": 72,
    "engine_module": "Accessory Gearbox",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
},

{
    "component_id": "CMP062",
    "component_name": "Hydraulic Pump Drive Pad",
    "ata_chapter": 72,
    "engine_module": "Accessory Gearbox",
    "maintenance_type": "ON_CONDITION",
    "life_unit": None,
    "life_limit": None,
    "repairable": "YES",
    "serialized": "YES"
}

])

component_df = pd.DataFrame(components)

component_df.to_csv("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/static_datasource/dim_engine_component.csv")