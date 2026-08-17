import psycopg2

from ETL.load.connection import get_connection

def create_dimension_tables():

    connection = get_connection()

    try:

        cursor = connection.cursor()

        #dim_aircraft

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dim_aircraft (aircraft_registration VARCHAR(20) PRIMARY KEY, aircraft_manufacture_date DATE, aircraft_status VARCHAR(25)
            );
        """)

        #dim_engine

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dim_engine (engine_serial_number VARCHAR(20) PRIMARY KEY, engine_model VARCHAR(20), engine_family VARCHAR(20), engine_manufacturer VARCHAR(20), engine_manufacture_date DATE, engine_status VARCHAR(20)
        );
        """)

        #dim_airport

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dim_airport (airport_code VARCHAR(20) PRIMARY KEY, airport_name VARCHAR(50), city VARCHAR(20), state VARCHAR(20), country VARCHAR(20), airport_type VARCHAR(20), runway_length_ft INT, elevation_ft INT
        );
        """)

        #dim_route

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dim_route (route_id VARCHAR(20) PRIMARY KEY, origin VARCHAR(20), destination VARCHAR(20), distance_nm INT, typical_duration_min INT, route_type VARCHAR(20)
        );
        """)

        #dim_component

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dim_component (component_id VARCHAR(20) PRIMARY KEY, component_name VARCHAR(20), ata_chapter INT, engine_module VARCHAR(20), maintenance_type VARCHAR(20), life_unit VARCHAR(20), life_limit NUMERIC, repairable VARCHAR(20), serialized VARCHAR(20)
        );
        """)

        connection.commit()

        print("="*60)
        print("dimension tables have created")
        print("="*60)

    except Exception as e:

        connection.rollback()

        print("error in creating dimension has appeared")
        print(e)

        raise

    finally:

        cursor.close()
        connection.close()


def create_fact_tables():

    connection = get_connection()

    try:

        cursor = connection.cursor()

        #==========================transform_engine_component_inventory_df==================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS engine_component_inventory (
        inventory_id VARCHAR(20) PRIMARY KEY,
        component_serial_number VARCHAR(20),
        component_id VARCHAR(20),
        component_name VARCHAR(20),
        engine_serial_number VARCHAR(20),
        manufacture_date DATE,
        installation_date DATE,
        position VARCHAR(20),
        installation_type VARCHAR(20),
        status VARCHAR(20)
        );
        """)
#==========================transform_fact_engine_removal_df==================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fact_engine_removal (
        removal_id VARCHAR(20) PRIMARY KEY,
        maintenance_event_id VARCHAR(20),
        work_order_id VARCHAR(20),
        engine_serial_number VARCHAR(20),
        aircraft_registration VARCHAR(20),
        removal_date DATE,
        removal_reason VARCHAR(20),
        removal_type VARCHAR(20),
        engine_hours_at_removal NUMERIC,
        engine_cycles_at_removal INT,
        removed_by VARCHAR(20),
        replacement_engine_serial VARCHAR(20),
        removal_status VARCHAR(20)
        );
        """)
#==========================transform_fact_component_life_df==================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fact_component_life (
        utilization_id VARCHAR(20) PRIMARY KEY,
        component_serial_number VARCHAR(20),
        component_id VARCHAR(20),
        engine_serial_number VARCHAR(20),
        utilization_date DATE,
        tsn NUMERIC,
        tso NUMERIC,
        tsr NUMERIC,
        life_unit VARCHAR(20),
        life_limit NUMERIC,
        status VARCHAR(20)
        );
        """)
#==========================transform_fact_flight_df==================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fact_flight (
        flight_id VARCHAR(20) PRIMARY KEY,
        flight_date DATE,
        aircraft_registration VARCHAR(20),
        route_id VARCHAR(20),
        origin VARCHAR(20),
        destination VARCHAR(20),
        left_engine_serial_number VARCHAR(20),
        right_engine_serial_number VARCHAR(20),
        scheduled_departure TIMESTAMP,
        actual_departure TIMESTAMP,
        scheduled_arrival TIMESTAMP,
        actual_arrival TIMESTAMP,
        flight_duration_min INT,
        block_hours NUMERIC,
        air_hours NUMERIC,
        flight_cycles INT,
        weather VARCHAR(20),
        delay_minutes INT,
        flight_status VARCHAR(20)
        );
        """)
#==========================transform_fact_engine_utilization_df==================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fact_engine_utilization (
        utilization_id VARCHAR(20) PRIMARY KEY,
        utilization_date DATE,
        flight_id VARCHAR(20),
        engine_serial_number VARCHAR(20),
        aircraft_registration VARCHAR(20),
        flight_hours NUMERIC,
        flight_cycles INT,
        cumulative_engine_hours NUMERIC,
        cumulative_engine_cycles INT,
        engine_status VARCHAR(20)
        );
        """)
#==========================transform_fact_maintenance_event_df==================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fact_maintenance_event (
        maintenance_event_id VARCHAR(20) PRIMARY KEY,
        work_order_id VARCHAR(20),
        fault_id VARCHAR(20),
        engine_serial_number VARCHAR(20),
        aircraft_registration VARCHAR(20),
        component_serial_number VARCHAR(20),
        component_id VARCHAR(20),
        maintenance_date TIMESTAMP,
        maintenance_type VARCHAR(20),
        action_taken VARCHAR(20),
        technician_id VARCHAR(20),
        labor_hours NUMERIC,
        parts_replaced VARCHAR(20),
        maintenance_result VARCHAR(20),
        release_to_service VARCHAR(20)
        );
        """)
#==========================transform_fact_workorder_df==================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fact_workorder (
        work_order_id VARCHAR(20) PRIMARY KEY,
        fault_id VARCHAR(20),
        engine_serial_number VARCHAR(20),
        aircraft_registration VARCHAR(20),
        component_serial_number VARCHAR(20),
        component_id VARCHAR(20),
        work_order_date DATE,
        maintenance_type VARCHAR(20),
        priority VARCHAR(20),
        assigned_team VARCHAR(20),
        technician_id VARCHAR(20),
        planned_start TIMESTAMP,
        planned_end TIMESTAMP,
        actual_start TIMESTAMP,
        actual_end TIMESTAMP,
        labor_hours NUMERIC,
        work_order_status VARCHAR(20)
        );
        """)
#==========================transform_fact_fault_event_df==================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fact_fault_event (
        fault_id VARCHAR(20) PRIMARY KEY,
        flight_id VARCHAR(20),
        engine_serial_number VARCHAR(20),
        aircraft_registration VARCHAR(20),
        component_serial_number VARCHAR(20),
        component_id VARCHAR(20),
        fault_date DATE,
        fault_code VARCHAR(20),
        fault_description VARCHAR(20),
        fault_category VARCHAR(20),
        severity VARCHAR(20),
        detection_source VARCHAR(20),
        status VARCHAR(20)
        );
        """)
#==========================transform_fact_shop_df==================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fact_shop_visit (
        shop_visit_id VARCHAR(20) PRIMARY KEY,
        maintenance_event_id VARCHAR(20),
        work_order_id VARCHAR(20),
        engine_serial_number VARCHAR(20),
        aircraft_registration VARCHAR(20),
        visit_reason VARCHAR(20),
        shop_name VARCHAR(20),
        arrival_date DATE,
        teardown_date DATE,
        assembly_date DATE,
        completion_date DATE,
        days_in_shop INT,
        modules_removed INT,
        llp_replaced VARCHAR(20),
        test_cell_result VARCHAR(20),
        return_to_service VARCHAR(20)
        );
        """)
#==========================transform_engine_installation_df==================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS engine_installation (
        installation_id INT PRIMARY KEY,
        aircraft_registration VARCHAR(20),
        engine_serial_number VARCHAR(20),
        engine_position VARCHAR(20)
        );
        """)
    #============================================================

        connection.commit()

        print("="*60)
        print("fact tables have created")
        print("="*60)
 
    except Exception as e:
        print('fact tables could not be created')
        print(e)

    finally:
        cursor.close()
        connection.close()
        
 
if __name__ == "__main__":

    
    create_dimension_tables()

    create_fact_tables()