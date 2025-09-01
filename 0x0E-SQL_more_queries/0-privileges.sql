#!/usr/bin/bash

-- Write a script that lists all privileges of the
-- MySQL users user_0d_1 and user_0d_2 on your server

SHOW IF EXISTS GRANTS FOR 'user_od_1'@'localhost';
SHOW IF EXISTS GRANTS FOR 'user_od_2'@'localhost';
