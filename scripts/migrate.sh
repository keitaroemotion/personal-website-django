if [[ $1 == '-c' ]]; then
    rm -rf peer/migrations/*
    python3 manage.py makemigrations peer
else
    python3 manage.py makemigrations peer
fi
