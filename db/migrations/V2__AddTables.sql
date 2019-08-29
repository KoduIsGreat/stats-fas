CREATE TABLE nwm.features(
	id bigint NOT NULL,
	geom geometry(GEOMETRY, 4326),
	CONSTRAINT features_pk PRIMARY KEY (id)
);

CREATE TABLE nwm.parameters(
    id bigserial NOT NULL,
    name text NOT NULL,
    CONSTRAINT parameters_pk PRIMARY KEY (id),
    CONSTRAINT parameters_uq UNIQUE (name)
);

CREATE TABLE nwm.observations(
	id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
	feature_id bigint NOT NULL,
	parameter_id bigint NOT NULL,
	observed timestamptz NOT NULL,
	value double precision NOT NULL,
	CONSTRAINT observations_pk PRIMARY KEY (id),
    CONSTRAINT observations_uq UNIQUE (feature_id, parameter_id, observed)
);

ALTER TABLE nwm.observations ADD CONSTRAINT observation_features_fk FOREIGN KEY (feature_id) REFERENCES nwm.features (id);
ALTER TABLE nwm.observations ADD CONSTRAINT observation_parameters_fk FOREIGN KEY (parameter_id) REFERENCES nwm.parameters (id);

CREATE VIEW nwm.all_observations AS SELECT o.id, o.feature_id AS comid, p.name, observed, value FROM nwm.observations o, nwm.parameters p WHERE o.parameter_id = p.id;