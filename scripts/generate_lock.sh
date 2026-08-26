#!/bin/sh
set -eu

python_version="${1:?usage: scripts/generate_lock.sh 3.11|3.12|3.13 [input] [output]}"
input_file="${2:-requirements/dev.in}"
output_file="${3:-locks/py${python_version}.txt}"

case "$python_version" in
    3.11|3.12|3.13) ;;
    *)
        echo "Unsupported Python version: $python_version" >&2
        exit 2
        ;;
esac

# Opt-in para redes corporativas que interceptan TLS y cuya CA no está en la
# imagen slim. CI no define esta variable y conserva la verificación TLS normal.
if [ -n "${COURSE_PIP_TRUSTED_HOSTS:-}" ]; then
    PIP_TRUSTED_HOST="$(printf '%s' "$COURSE_PIP_TRUSTED_HOSTS" | tr ',' ' ')"
    export PIP_TRUSTED_HOST
fi

python -m pip install --quiet "pip==25.0.1" "pip-tools==7.5.1"
python -m piptools compile \
    --no-emit-options \
    --resolver=backtracking \
    --strip-extras \
    --output-file="$output_file" \
    "$input_file"
