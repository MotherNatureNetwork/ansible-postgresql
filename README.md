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
