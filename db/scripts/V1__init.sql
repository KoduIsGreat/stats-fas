CREATE EXTENSION postgis;
CREATE EXTENSION "uuid-ossp";

CREATE SCHEMA nwm AUTHORIZATION fas;
ALTER USER fas SET search_path = fas, public;