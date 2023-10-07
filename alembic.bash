#!/bin/bash

file_name="alembic.ini"
conn_string='sqlalchemy.url = $DBMS+$DRIVER://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME'

if [ ! -f $file_name ]; then
    echo "Файл alemnic.ini не обнаружен в данной директории"
    exit 1
fi

sed -i "s|sqlalchemy.url = .*|$conn_string|" "$file_name"

#python -m alembic upgrade headz