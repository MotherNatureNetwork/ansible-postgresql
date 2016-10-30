[![Build Status](https://travis-ci.org/MotherNatureNetwork/ansible-postgresql.svg?branch=master)](https://travis-ci.org/MotherNatureNetwork/ansible-postgresql)

PostgreSQL
=========

Installs Postgresql.

Requirements
------------

N/A

Role Variables
--------------

See defaults/main.yml

    postgresql_version: 9.4
    postgresql_distro_version: trusty
    postgresql_user: db_user (optional)
    postgresql_password: 123456
    postgresql_database: main_db (optional)

when `postgresql_user`, `postgresql_password`, or `postgresql_database` are not
specified, their respective tasks will be skipped.

Dependencies
------------

N/A

Example Playbook
----------------

    - hosts: old_db
      roles:
         - role: mnn.postgresql
           postgresql_version: 8.4
           postgresql_distro_version: trusty

License
-------

GPLv3

Author Information
------------------

This role was written by Justin Caratzas <bigjust@lambdaphil.es> for Mother Nature Network (https://github.com/MotherNatureNetwork)
