-- Table: public."user"

-- DROP TABLE public."user";

-- CS 3240 Final Project
-- Ryan Donovan, Bobby Andris, Neel Patel, Jeffrey You

CREATE TABLE public."user"
(
    "userID" integer NOT NULL DEFAULT nextval('"user_userID_seq"'::regclass),
    username character varying(20) COLLATE pg_catalog."default" NOT NULL,
    user_password character varying(50) COLLATE pg_catalog."default" NOT NULL,
    user_type character varying COLLATE pg_catalog."default",
    CONSTRAINT user_pkey PRIMARY KEY ("userID")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."user"
    OWNER to postgres;