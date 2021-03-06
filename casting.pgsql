--
-- PostgreSQL database dump
--

-- Dumped from database version 12.8 (Ubuntu 12.8-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.8 (Ubuntu 12.8-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actor; Type: TABLE; Schema: public; Owner: cap
--

CREATE TABLE public.actor (
    id integer NOT NULL,
    name character varying,
    age character varying,
    gender character varying
);


ALTER TABLE public.actor OWNER TO cap;

--
-- Name: actor_id_seq; Type: SEQUENCE; Schema: public; Owner: cap
--

CREATE SEQUENCE public.actor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actor_id_seq OWNER TO cap;

--
-- Name: actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cap
--

ALTER SEQUENCE public.actor_id_seq OWNED BY public.actor.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: cap
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO cap;

--
-- Name: movie; Type: TABLE; Schema: public; Owner: cap
--

CREATE TABLE public.movie (
    id integer NOT NULL,
    title character varying,
    date character varying
);


ALTER TABLE public.movie OWNER TO cap;

--
-- Name: movie_id_seq; Type: SEQUENCE; Schema: public; Owner: cap
--

CREATE SEQUENCE public.movie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movie_id_seq OWNER TO cap;

--
-- Name: movie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cap
--

ALTER SEQUENCE public.movie_id_seq OWNED BY public.movie.id;


--
-- Name: actor id; Type: DEFAULT; Schema: public; Owner: cap
--

ALTER TABLE ONLY public.actor ALTER COLUMN id SET DEFAULT nextval('public.actor_id_seq'::regclass);


--
-- Name: movie id; Type: DEFAULT; Schema: public; Owner: cap
--

ALTER TABLE ONLY public.movie ALTER COLUMN id SET DEFAULT nextval('public.movie_id_seq'::regclass);


--
-- Data for Name: actor; Type: TABLE DATA; Schema: public; Owner: cap
--

COPY public.actor (id, name, age, gender) FROM stdin;
3	mohammed	23	male
2	khalid	25	male
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: cap
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Data for Name: movie; Type: TABLE DATA; Schema: public; Owner: cap
--

COPY public.movie (id, title, date) FROM stdin;
2	catch me if you can	03/25/2006
\.


--
-- Name: actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cap
--

SELECT pg_catalog.setval('public.actor_id_seq', 3, true);


--
-- Name: movie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cap
--

SELECT pg_catalog.setval('public.movie_id_seq', 2, true);


--
-- Name: actor actor_pkey; Type: CONSTRAINT; Schema: public; Owner: cap
--

ALTER TABLE ONLY public.actor
    ADD CONSTRAINT actor_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: cap
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: movie movie_pkey; Type: CONSTRAINT; Schema: public; Owner: cap
--

ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

