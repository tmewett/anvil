test_exit() {
    echo "$2"
    exit $1
}

PYTHON="${PYTHON:-python3}"
export PYTHONPATH=../..
