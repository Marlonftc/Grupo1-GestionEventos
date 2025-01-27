#!/bin/bash
mongoimport --host localhost --db gestion-de-eventos --collection feedback --type json --file /data/feedback.json --jsonArray