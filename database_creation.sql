CREATE TABLE fact_flats(
    id uuid NOT NULL,
    immoscout_id integer NOT NULL,
    address_id uuid NOT NULL,
    agency_id uuid NOT NULL,
    area_sq_m float NOT NULL,
    cnt_rooms float NOT NULL,
    cnt_floors integer,
    floor integer,
    type pg_enum,
    has_fitted_kitchen boolean,
    has_lift boolean,
    has_balcony boolean,
    has_garden boolean,
    has_guest_toilet boolean,
    is_barrier_free boolean,
    heating_type pg_enum,
    thermal_characteristics float,
    total_rent float NOT NULL,
    base_rent float NOT NULL,
    service_charge float,
    deposit float
);

CREATE TABLE dim_address(
    id uuid NOT NULL,
    city char NOT NULL,
    district char,
    zip_code char,
    street char,
    house_number char,
    lng float,
    lat float
);

CREATE TABLE dim_agency(
    id uuid NOT NULL,
    company_name char,
    contact_firstname char,
    contact_lastname char,
    salutation char,
    email char,
    phone_number char,
    mobile_number char,
    address_city char,
    address_street char,
    address_zip_code char,
    address_house_number char
);


