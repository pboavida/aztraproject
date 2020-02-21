import psycopg2
from config import config

# to be added would be checks to see if the tables are already created and confirm that we are not creating duplicates,
# and some checks to make sure the database is there and we can open it correctly


# the possible values for the enum variables were obtained by running the queries for a large number of ads and listing
# all the obtained values. This is obviously not ideal and instead there should be some external confirmation about all the
# values that can be received for those variables

commands = (
    """CREATE TYPE apartment_type AS ENUM (
        'APARTMENT',
        'PENTHOUSE',
        'GROUND_FLOOR',
        'TERRACED_FLAT',
        'MAISONETTE',
        'NO_INFORMATION',
        'ROOF_STOREY',
        'OTHER',
        'LOFT',
        'RAISED_GROUND_FLOOR'
    )""",
    """CREATE TYPE heating_type AS ENUM (
        'CENTRAL_HEATING',
        'SELF_CONTAINED_CENTRAL_HEATING'
    )""",
    """CREATE TABLE dim_address(
        id uuid CONSTRAINT address_id PRIMARY KEY,
        city text NOT NULL,
        district text,
        zip_code integer,
        street text,
        house_number text,
        lng float,
        lat float 
    );""",
    """CREATE TABLE dim_agency(
        id uuid CONSTRAINT agency_id PRIMARY KEY,
        company_name text,
        contact_firstname text,
        contact_lastname text,
        salutation text,
        email text,
        phone_number text,
        mobile_number text,
        address_city text,
        address_street text,
        address_zip_code text,
        address_house_number text
    );""",
"""CREATE TABLE fact_flats(
    id uuid CONSTRAINT flat_id PRIMARY KEY,
    immoscout_id integer NOT NULL,
    address_id uuid REFERENCES dim_address(id),
    agency_id uuid REFERENCES dim_agency(id),
    area_sq_m float NOT NULL,
    cnt_rooms float NOT NULL,
    cnt_floors integer,
    floor integer,
    type apartment_type,
    has_fitted_kitchen boolean,
    has_lift boolean,
    has_balcony boolean,
    has_garden boolean,
    has_guest_toilet boolean,
    is_barrier_free boolean,
    heating_type heating_type,
    thermal_characteristics float,
    total_rent float NOT NULL,
    base_rent float NOT NULL,
    service_charge float,
    deposit float
);""")


params = config()
print(params['database'])
con = psycopg2.connect(**params)


cur = con.cursor()

for command in commands:
    cur.execute(command)

cur.close()
con.commit()
con.close()
