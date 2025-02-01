#!/bin/bash
echo "⏳ Esperando a que MongoDB inicie..."
sleep 5  # Esperar 5 segundos para asegurar que MongoDB esté listo

echo "📥 Importando datos en MongoDB..."

mongoimport --host localhost --db gestion-de-eventos --collection feedback --type json --file /data/feedback.json --jsonArray
mongoimport --host localhost --db gestion-de-eventos --collection eventos --type json --file /data/eventos.json --jsonArray

echo "✅ Importación completada."