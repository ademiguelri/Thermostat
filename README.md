Docker barrun postgres terminala irikitzeko:
    docker exec -it <dockerID> psql -U postgres

Datubasea sortu:
    CREATE DATABASE <izena>;
    create database test;
Datubasera sartu:
    \c <datubase izena>
    \c test

Taula sortu:
    CREATE TABLE <izena> (<zutabe-izena> <datu-mota>, ... );
    create table auto (data TIMESTAMP, balio INT);

Taulan datuak sartu:
    insert into  auto(data, balio) values (generate_series('2020-01-01'::date, '2020-12-31'::date, INTERVAL '1 day'),generate_series(1,365)*(10 + 10 * random()));


Grafana PostgreSQL konfigurazioa:
    Host: 172.20.0.1:5432
    Database: test
    User: postgres
    Password: password
    TLS/SSL mode: disable

    Version: 14
    TimescaleDB: check