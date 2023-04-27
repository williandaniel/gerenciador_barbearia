--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

-- Started on 2023-04-27 14:39:40

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
-- TOC entry 214 (class 1259 OID 25027)
-- Name: agendamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.agendamento (
    codagendamento integer NOT NULL,
    dataagendamento date NOT NULL,
    hora time without time zone NOT NULL,
    situacao character varying(100) DEFAULT 'agendado'::character varying,
    codfuncionario integer NOT NULL,
    codcliente integer NOT NULL,
    codservico integer NOT NULL
);


ALTER TABLE public.agendamento OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 25031)
-- Name: agendamento_codagendamento_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.agendamento_codagendamento_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.agendamento_codagendamento_seq OWNER TO postgres;

--
-- TOC entry 3373 (class 0 OID 0)
-- Dependencies: 215
-- Name: agendamento_codagendamento_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.agendamento_codagendamento_seq OWNED BY public.agendamento.codagendamento;


--
-- TOC entry 216 (class 1259 OID 25032)
-- Name: cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cliente (
    codcliente integer NOT NULL,
    nome character varying(150) NOT NULL,
    sobrenome character varying(50) NOT NULL,
    telefone character varying(20) NOT NULL,
    cpf character varying(11),
    rg character varying(9),
    dtnascimento date,
    genero character varying(20),
    idendereco integer
);


ALTER TABLE public.cliente OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 25035)
-- Name: cliente_codcliente_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cliente_codcliente_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cliente_codcliente_seq OWNER TO postgres;

--
-- TOC entry 3374 (class 0 OID 0)
-- Dependencies: 217
-- Name: cliente_codcliente_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cliente_codcliente_seq OWNED BY public.cliente.codcliente;


--
-- TOC entry 218 (class 1259 OID 25036)
-- Name: endereco; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.endereco (
    idendereco integer NOT NULL,
    bairro character varying(50) NOT NULL,
    rua character varying(150) NOT NULL,
    numero integer NOT NULL,
    complemento character varying(150),
    uf character varying(2) NOT NULL,
    cidade character varying(150) NOT NULL
);


ALTER TABLE public.endereco OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 25041)
-- Name: endereco_idendereco_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.endereco_idendereco_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.endereco_idendereco_seq OWNER TO postgres;

--
-- TOC entry 3375 (class 0 OID 0)
-- Dependencies: 219
-- Name: endereco_idendereco_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.endereco_idendereco_seq OWNED BY public.endereco.idendereco;


--
-- TOC entry 220 (class 1259 OID 25042)
-- Name: funcionario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.funcionario (
    codfuncionario integer NOT NULL,
    nome character varying(150) NOT NULL,
    sobrenome character varying(50) NOT NULL,
    telefone character varying(20) NOT NULL,
    cpf character varying(11) NOT NULL,
    rg character varying(9) NOT NULL,
    email character varying(100) NOT NULL,
    dtnascimento date NOT NULL,
    genero character varying(20) NOT NULL,
    estadocivil character varying(30) NOT NULL,
    idendereco integer NOT NULL
);


ALTER TABLE public.funcionario OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 25045)
-- Name: funcionario_codfuncionario_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.funcionario_codfuncionario_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.funcionario_codfuncionario_seq OWNER TO postgres;

--
-- TOC entry 3376 (class 0 OID 0)
-- Dependencies: 221
-- Name: funcionario_codfuncionario_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.funcionario_codfuncionario_seq OWNED BY public.funcionario.codfuncionario;


--
-- TOC entry 222 (class 1259 OID 25046)
-- Name: servico; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.servico (
    codservico integer NOT NULL,
    tiposervico character varying(50) NOT NULL,
    preco real NOT NULL,
    tempomedio integer NOT NULL,
    CONSTRAINT servico_preco_check CHECK ((preco > (0)::double precision)),
    CONSTRAINT servico_tempomedio_check CHECK ((tempomedio > 0))
);


ALTER TABLE public.servico OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 25051)
-- Name: servico_codservico_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.servico_codservico_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.servico_codservico_seq OWNER TO postgres;

--
-- TOC entry 3377 (class 0 OID 0)
-- Dependencies: 223
-- Name: servico_codservico_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.servico_codservico_seq OWNED BY public.servico.codservico;


--
-- TOC entry 3193 (class 2604 OID 25052)
-- Name: agendamento codagendamento; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agendamento ALTER COLUMN codagendamento SET DEFAULT nextval('public.agendamento_codagendamento_seq'::regclass);


--
-- TOC entry 3195 (class 2604 OID 25053)
-- Name: cliente codcliente; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente ALTER COLUMN codcliente SET DEFAULT nextval('public.cliente_codcliente_seq'::regclass);


--
-- TOC entry 3196 (class 2604 OID 25054)
-- Name: endereco idendereco; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco ALTER COLUMN idendereco SET DEFAULT nextval('public.endereco_idendereco_seq'::regclass);


--
-- TOC entry 3197 (class 2604 OID 25055)
-- Name: funcionario codfuncionario; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionario ALTER COLUMN codfuncionario SET DEFAULT nextval('public.funcionario_codfuncionario_seq'::regclass);


--
-- TOC entry 3198 (class 2604 OID 25056)
-- Name: servico codservico; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.servico ALTER COLUMN codservico SET DEFAULT nextval('public.servico_codservico_seq'::regclass);


--
-- TOC entry 3358 (class 0 OID 25027)
-- Dependencies: 214
-- Data for Name: agendamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.agendamento VALUES (27, '2023-04-22', '10:00:00', 'agendado', 10, 7, 1);
INSERT INTO public.agendamento VALUES (28, '2023-04-22', '09:00:00', 'agendado', 11, 8, 3);
INSERT INTO public.agendamento VALUES (29, '2023-04-22', '10:00:00', 'agendado', 7, 8, 3);
INSERT INTO public.agendamento VALUES (30, '2023-04-22', '11:00:00', 'agendado', 11, 9, 1);
INSERT INTO public.agendamento VALUES (31, '2023-04-22', '11:00:00', 'agendado', 10, 10, 1);
INSERT INTO public.agendamento VALUES (32, '2023-04-22', '13:00:00', 'agendado', 12, 11, 3);
INSERT INTO public.agendamento VALUES (33, '2023-04-22', '15:00:00', 'agendado', 12, 12, 1);
INSERT INTO public.agendamento VALUES (34, '2023-04-22', '16:00:00', 'agendado', 12, 13, 3);
INSERT INTO public.agendamento VALUES (36, '2023-04-22', '15:00:00', 'agendado', 1, 15, 1);
INSERT INTO public.agendamento VALUES (38, '2023-04-22', '13:00:00', 'agendado', 5, 17, 3);
INSERT INTO public.agendamento VALUES (39, '2023-04-22', '15:00:00', 'agendado', 5, 18, 1);
INSERT INTO public.agendamento VALUES (40, '2023-04-22', '16:00:00', 'agendado', 5, 19, 1);
INSERT INTO public.agendamento VALUES (41, '2023-04-22', '17:00:00', 'agendado', 5, 20, 1);
INSERT INTO public.agendamento VALUES (1, '2023-04-21', '08:00:00', 'finalizado', 8, 1, 1);
INSERT INTO public.agendamento VALUES (2, '2023-04-21', '09:00:00', 'finalizado', 1, 2, 3);
INSERT INTO public.agendamento VALUES (3, '2023-04-21', '08:00:00', 'cancelado', 3, 3, 2);
INSERT INTO public.agendamento VALUES (4, '2023-04-21', '09:00:00', 'finalizado', 8, 4, 3);
INSERT INTO public.agendamento VALUES (5, '2023-04-21', '08:00:00', 'finalizado', 2, 5, 1);
INSERT INTO public.agendamento VALUES (6, '2023-04-21', '09:00:00', 'cancelado', 2, 6, 1);
INSERT INTO public.agendamento VALUES (7, '2023-04-21', '09:00:00', 'finalizado', 3, 7, 3);
INSERT INTO public.agendamento VALUES (8, '2023-04-21', '10:00:00', 'finalizado', 2, 8, 3);
INSERT INTO public.agendamento VALUES (9, '2023-04-21', '11:00:00', 'finalizado', 8, 9, 1);
INSERT INTO public.agendamento VALUES (10, '2023-04-21', '11:00:00', 'finalizado', 1, 10, 1);
INSERT INTO public.agendamento VALUES (11, '2023-04-21', '11:00:00', 'finalizado', 3, 11, 2);
INSERT INTO public.agendamento VALUES (12, '2023-04-21', '13:00:00', 'cancelado', 4, 12, 3);
INSERT INTO public.agendamento VALUES (13, '2023-04-21', '13:00:00', 'finalizado', 5, 13, 3);
INSERT INTO public.agendamento VALUES (14, '2023-04-21', '13:00:00', 'cancelado', 9, 15, 1);
INSERT INTO public.agendamento VALUES (15, '2023-04-21', '15:00:00', 'finalizado', 4, 14, 3);
INSERT INTO public.agendamento VALUES (16, '2023-04-21', '15:00:00', 'finalizado', 5, 16, 3);
INSERT INTO public.agendamento VALUES (17, '2023-04-21', '14:00:00', 'cancelado', 9, 17, 1);
INSERT INTO public.agendamento VALUES (18, '2023-04-21', '15:00:00', 'finalizado', 9, 18, 3);
INSERT INTO public.agendamento VALUES (19, '2023-04-21', '17:00:00', 'finalizado', 4, 19, 3);
INSERT INTO public.agendamento VALUES (20, '2023-04-21', '17:00:00', 'finalizado', 5, 20, 1);
INSERT INTO public.agendamento VALUES (21, '2023-04-22', '08:00:00', 'cancelado', 6, 1, 3);
INSERT INTO public.agendamento VALUES (22, '2023-04-22', '08:00:00', 'finalizado', 7, 2, 1);
INSERT INTO public.agendamento VALUES (23, '2023-04-22', '08:00:00', 'finalizado', 10, 3, 3);
INSERT INTO public.agendamento VALUES (24, '2023-04-22', '08:00:00', 'finalizado', 11, 4, 1);
INSERT INTO public.agendamento VALUES (25, '2023-04-22', '10:00:00', 'finalizado', 6, 5, 3);
INSERT INTO public.agendamento VALUES (35, '2023-04-22', '13:00:00', 'cancelado', 1, 14, 3);
INSERT INTO public.agendamento VALUES (37, '2023-04-22', '16:00:00', 'cancelado', 1, 16, 3);
INSERT INTO public.agendamento VALUES (26, '2023-04-22', '09:00:00', 'cancelado', 7, 6, 1);


--
-- TOC entry 3360 (class 0 OID 25032)
-- Dependencies: 216
-- Data for Name: cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.cliente VALUES (1, 'Edson', 'Galvão', '(47) 9826-90058', '46133065907', '473689716', '1968-03-04', 'Marculino', NULL);
INSERT INTO public.cliente VALUES (2, 'Julio', 'Ramos', '(47) 3183-1773', NULL, NULL, '1998-05-27', 'Marculino', 13);
INSERT INTO public.cliente VALUES (3, 'Leandro', 'Santos', '(47) 3551-4789', NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.cliente VALUES (4, 'Joaquim', 'Vieira', '(48) 3434-4332', '11107243220', NULL, '1992-11-18', 'Marculino', NULL);
INSERT INTO public.cliente VALUES (5, 'Davi', 'Rosa', '(47) 3849-9674', NULL, '752421153', '2002-07-27', 'Marculino', NULL);
INSERT INTO public.cliente VALUES (6, 'Matheus', 'Souza', '(47) 2552-1132', '48343786670', '214808361', '1987-10-21', 'Marculino', 14);
INSERT INTO public.cliente VALUES (7, 'Fernando', 'Rocha', '(47) 3298-4019', NULL, NULL, NULL, 'Marculino', NULL);
INSERT INTO public.cliente VALUES (8, 'Daniel', 'Moura', '(47) 3878-5410', NULL, NULL, '2001-07-14', 'Marculino', NULL);
INSERT INTO public.cliente VALUES (9, 'Guilherme', 'Nogueira', '(49) 2804-6236', NULL, NULL, NULL, 'Marculino', NULL);
INSERT INTO public.cliente VALUES (10, 'Lucca', 'Viana', '(48) 3444-4914', '82227138769', NULL, '1993-05-21', 'Marculino', NULL);
INSERT INTO public.cliente VALUES (11, 'Lorenzo', 'Mota', '(48) 3333-6883', NULL, NULL, NULL, 'Marculino', 15);
INSERT INTO public.cliente VALUES (12, 'Milena', 'Souza', '(47) 3478-3364', '33996558007', NULL, NULL, 'Feminino', NULL);
INSERT INTO public.cliente VALUES (13, 'Francisco', 'Santos', '(47) 3525-2334', '14633925598', NULL, '1978-08-13', 'Marculino', NULL);
INSERT INTO public.cliente VALUES (14, 'Gustavo', 'Sales', '(48) 2726-4262', NULL, NULL, NULL, 'Marculino', NULL);
INSERT INTO public.cliente VALUES (15, 'Esther', 'Paz', '(47) 2057-4959', '21593098006', '112362795', '2004-05-29', 'Feminino', 16);
INSERT INTO public.cliente VALUES (16, 'Arthur', 'Melo', '(49) 3768-3420', NULL, NULL, NULL, 'Marculino', NULL);
INSERT INTO public.cliente VALUES (17, 'Ana', 'Monteiro', '(47) 2057-7344', NULL, NULL, NULL, 'Feminino', NULL);
INSERT INTO public.cliente VALUES (18, 'Thiago', 'Lima', '(49) 3036-1686', NULL, NULL, '2004-08-12', 'Marculino', NULL);
INSERT INTO public.cliente VALUES (19, 'Bruno', 'Nogueira', '(48) 2271-8364', '34555857950', '491772762', NULL, 'Marculino', NULL);
INSERT INTO public.cliente VALUES (20, 'Calebe', 'Martins', '(47) 2879-2519', '02242636170', '364874466', '1992-08-19', 'Marculino', 17);


--
-- TOC entry 3362 (class 0 OID 25036)
-- Dependencies: 218
-- Data for Name: endereco; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.endereco VALUES (1, 'Costa e Silva', 'Almirante Jaceguay', 111, NULL, 'SC', 'Joinville');
INSERT INTO public.endereco VALUES (2, 'Bom Retiro', 'Amandus Alandt', 97, 'Apt 101 Bloco F', 'SC', 'Joinville');
INSERT INTO public.endereco VALUES (3, 'Costa e Silva', 'Antonio Schmitt', 678, NULL, 'SC', 'Joinville');
INSERT INTO public.endereco VALUES (4, 'Glória', 'Benjamin Constant', 45, 'Apt 302', 'SC', 'Joinville');
INSERT INTO public.endereco VALUES (5, 'Glória', 'Jaú', 42, NULL, 'SC', 'Joinville');
INSERT INTO public.endereco VALUES (6, 'Costa e Silva', 'Dona Elza Meinert', 789, NULL, 'SC', 'Joinville');
INSERT INTO public.endereco VALUES (7, 'Glória', 'Presidente Campos Salles', 678, NULL, 'SC', 'Joinville');
INSERT INTO public.endereco VALUES (8, 'Glória', 'Lindóia', 107, 'Apt 304', 'SC', 'Joinville');
INSERT INTO public.endereco VALUES (9, 'Glória', 'Marquês de Olinda', 485, NULL, 'SC', 'Joinville');
INSERT INTO public.endereco VALUES (10, 'Bom Retiro', 'Barriga Verde', 398, NULL, 'SC', 'Joinville');
INSERT INTO public.endereco VALUES (11, 'Glória', 'Max Colin', 857, NULL, 'SC', 'Joinville');
INSERT INTO public.endereco VALUES (12, 'Costa e Silva', 'Edgar Klein', 436, 'Apt 604', 'SC', 'Joinville');
INSERT INTO public.endereco VALUES (13, 'Glória', 'Presidente Campos Salles', 478, NULL, 'SC', 'Joinville');
INSERT INTO public.endereco VALUES (14, 'Bom Jesus', 'Tancredo Neves', 546, NULL, 'SC', 'Itaiópolis');
INSERT INTO public.endereco VALUES (15, 'Glória', 'Nazareno', 534, NULL, 'SC', 'Joinville');
INSERT INTO public.endereco VALUES (16, 'Costa e Silva', 'Claudionor Borba', 356, NULL, 'SC', 'Joinville');
INSERT INTO public.endereco VALUES (17, 'Glória', 'Max Colin', 218, 'Apt 201 Bloco G', 'SC', 'Joinville');


--
-- TOC entry 3364 (class 0 OID 25042)
-- Dependencies: 220
-- Data for Name: funcionario; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.funcionario VALUES (1, 'Danilo', 'Peixoto', '(47) 2437-7084', '12851558749', '843865088', 'danilo.peixoto@gmail.com', '1996-08-17', 'Marculino', 'Solteiro', 1);
INSERT INTO public.funcionario VALUES (2, 'Thales', 'Fogaça', '(47) 2787-7914', '14466346127', '257475126', 'thales.fogaca@gmail.com', '1998-12-09', 'Marculino', 'Separado', 2);
INSERT INTO public.funcionario VALUES (3, 'Matheus', 'Rezende', '(49) 2552-7855', '69799185670', '671447336', 'matheus.rezende@hotmail.com', '1989-06-01', 'Marculino', 'Casado', 3);
INSERT INTO public.funcionario VALUES (4, 'Rodrigo', 'Barros', '(48) 3655-3747', '94102139834', '716699503', 'rodrigo.barros@gmail.com', '1999-04-23', 'Marculino', 'Solteiro', 4);
INSERT INTO public.funcionario VALUES (5, 'Yuri', 'Freitas', '(47) 3998-1150', '67899879833', '41319579X', 'yuri.freitas@hotmail.com', '1994-11-18', 'Marculino', 'Solteiro', 5);
INSERT INTO public.funcionario VALUES (6, 'Luiz', 'Ribeiro', '(47) 3556-5135', '83354352868', '676865689', 'luiz.ribeiro@gmail.com', '1988-03-27', 'Marculino', 'Divorciado', 6);
INSERT INTO public.funcionario VALUES (7, 'Vinicius', 'Barros', '(48) 3987-8483', '22515568181', '150493411', 'vinicius.barros@gmail.com', '1997-08-10', 'Marculino', 'Solteiro', 7);
INSERT INTO public.funcionario VALUES (8, 'André', 'Costela', '(48) 3305-7468', '64663786758', '584847191', 'andre.costela@hotmail.com', '1986-07-14', 'Marculino', 'Casado', 8);
INSERT INTO public.funcionario VALUES (9, 'Laura', 'Porto', '(47) 3140-4289', '38877506679', '525348505', 'laura.porto@gmail.com', '2001-05-16', 'Feminino', 'Solteiro', 9);
INSERT INTO public.funcionario VALUES (10, 'Caio', 'Costela', '(47) 3638-5046', '81563256649', '022139308', 'caio.costela@gmail.com', '1995-08-13', 'Marculino', 'Solteiro', 10);
INSERT INTO public.funcionario VALUES (11, 'Kamilly', 'Novaes', '(47) 3173-2914', '16640911140', '346146707', 'kamilly.novaes@gmail.com', '1999-07-25', 'Feminino', 'Solteiro', 11);
INSERT INTO public.funcionario VALUES (12, 'Beatriz', 'Martins', '(48) 3772-7715', '34764973995', '346146707', 'beatriz.martins@gmail.com', '1997-03-11', 'Feminino', 'Separado', 12);


--
-- TOC entry 3366 (class 0 OID 25046)
-- Dependencies: 222
-- Data for Name: servico; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.servico VALUES (1, 'Cabelo', 50, 60);
INSERT INTO public.servico VALUES (2, 'Barba', 40, 50);
INSERT INTO public.servico VALUES (3, 'Cabelo e Barba', 85, 110);


--
-- TOC entry 3378 (class 0 OID 0)
-- Dependencies: 215
-- Name: agendamento_codagendamento_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.agendamento_codagendamento_seq', 41, true);


--
-- TOC entry 3379 (class 0 OID 0)
-- Dependencies: 217
-- Name: cliente_codcliente_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cliente_codcliente_seq', 20, true);


--
-- TOC entry 3380 (class 0 OID 0)
-- Dependencies: 219
-- Name: endereco_idendereco_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.endereco_idendereco_seq', 17, true);


--
-- TOC entry 3381 (class 0 OID 0)
-- Dependencies: 221
-- Name: funcionario_codfuncionario_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.funcionario_codfuncionario_seq', 12, true);


--
-- TOC entry 3382 (class 0 OID 0)
-- Dependencies: 223
-- Name: servico_codservico_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.servico_codservico_seq', 3, true);


--
-- TOC entry 3202 (class 2606 OID 25058)
-- Name: agendamento agendamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_pkey PRIMARY KEY (codagendamento);


--
-- TOC entry 3204 (class 2606 OID 25060)
-- Name: cliente cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (codcliente);


--
-- TOC entry 3206 (class 2606 OID 25062)
-- Name: endereco endereco_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco
    ADD CONSTRAINT endereco_pkey PRIMARY KEY (idendereco);


--
-- TOC entry 3208 (class 2606 OID 25064)
-- Name: funcionario funcionario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionario
    ADD CONSTRAINT funcionario_pkey PRIMARY KEY (codfuncionario);


--
-- TOC entry 3210 (class 2606 OID 25066)
-- Name: servico servico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.servico
    ADD CONSTRAINT servico_pkey PRIMARY KEY (codservico);


--
-- TOC entry 3211 (class 2606 OID 25067)
-- Name: agendamento agendamento_codcliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_codcliente_fkey FOREIGN KEY (codcliente) REFERENCES public.cliente(codcliente) ON DELETE CASCADE;


--
-- TOC entry 3212 (class 2606 OID 25072)
-- Name: agendamento agendamento_codfuncionario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_codfuncionario_fkey FOREIGN KEY (codfuncionario) REFERENCES public.funcionario(codfuncionario) ON DELETE CASCADE;


--
-- TOC entry 3213 (class 2606 OID 25077)
-- Name: agendamento agendamento_codservico_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_codservico_fkey FOREIGN KEY (codservico) REFERENCES public.servico(codservico) ON DELETE CASCADE;


--
-- TOC entry 3214 (class 2606 OID 25082)
-- Name: cliente cliente_idendereco_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_idendereco_fkey FOREIGN KEY (idendereco) REFERENCES public.endereco(idendereco) ON DELETE SET NULL;


--
-- TOC entry 3215 (class 2606 OID 25087)
-- Name: funcionario funcionario_idendereco_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionario
    ADD CONSTRAINT funcionario_idendereco_fkey FOREIGN KEY (idendereco) REFERENCES public.endereco(idendereco);


-- Completed on 2023-04-27 14:39:41

--
-- PostgreSQL database dump complete
--

