-- Table: public.report

-- DROP TABLE public.report;

-- CS 3240 Final Project
-- Ryan Donovan, Bobby Andris, Neel Patel, Jeffrey You

CREATE TABLE public.report
(
    "report_ID" bigint NOT NULL DEFAULT nextval('"report_report_ID_seq"'::regclass),
    "timestamp" time with time zone NOT NULL,
    company_name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    company_phone character varying(14) COLLATE pg_catalog."default" NOT NULL,
    company_location character varying COLLATE pg_catalog."default",
    sector character varying COLLATE pg_catalog."default",
    industry character varying COLLATE pg_catalog."default",
    current_projects character varying COLLATE pg_catalog."default",
    privacy_designation character varying(7) COLLATE pg_catalog."default",
    CONSTRAINT report_pkey PRIMARY KEY ("report_ID", company_phone)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.report
    OWNER to postgres;