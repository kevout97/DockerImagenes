# Webapp Verito

En el directorio webpage esta contenido todo el codigo html que levanta la pagina web.

El runit correspondiente a un contenedor con dicha imagen (creada a partir del Dockerfile) puede ser:

```bash
docker run -d -p 80:80 -p 443:443 kevout/webapp
```

Enseguida ejecutar el comando:

```bash
echo "127.0.0.1 webapp.ctin.net" >> /etc/hosts
```

Consultar la direccion http://webapp.ctin.net
