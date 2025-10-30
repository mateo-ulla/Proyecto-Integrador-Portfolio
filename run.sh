# run.sh

set -e

# activar virtualenv 
if [ -f "venv/bin/activate" ]; then
  echo "activando virtualenv..."
  source venv/bin/activate
fi

export FLASK_APP=${FLASK_APP:-app.py}
export FLASK_ENV=${FLASK_ENV:-production}
export SECRET_KEY=${SECRET_KEY:-cambiar_este_valor_por_produccion}
export DB_HOST=${DB_HOST:-localhost}
export DB_USER=${DB_USER:-root}
export DB_PASSWORD=${DB_PASSWORD:-}
export DB_NAME=${DB_NAME:-portfolio_db}
export DB_PORT=${DB_PORT:-3306}

echo "iniciando gunicorn..."
gunicorn --workers 3 --bind 0.0.0.0:5000 app:app
