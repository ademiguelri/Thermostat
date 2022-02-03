Open postgres terminal inside the docker:
    docker exec -it <dockerID> psql -U postgres

Create database:

    CREATE DATABASE <name>;
    create database test;

Enter to database:

    \c <database-name>
    \c test

Create table:

    CREATE TABLE <name> (<column-name> <data-type>, ... );
    create table auto (dateTime TIMESTAMP, info INT);

Insert data to DB with generate_series:

    insert into  auto(dateTime, info) values (generate_series('2020-01-01'::date, '2020-12-31'::date, INTERVAL '1 day'),generate_series(1,365)*(10 + 10 * random()));


Grafana PostgreSQL configuration:

    Host: 172.20.0.1:5432
    Database: test
    User: postgres
    Password: password
    TLS/SSL mode: disable
    Version: 14
    TimescaleDB: check