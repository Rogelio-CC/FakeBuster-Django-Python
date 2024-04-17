from newspaper import Article, ArticleException

# Cache para almacenar artículos analizados
articulos_cache = {}

def obtener_datos_articulo(url):
    try:
        # Verificar si el artículo ya está en caché
        if url in articulos_cache:
            article = articulos_cache[url]
        else:
            article = analizar_url(url)
            articulos_cache[url] = article

        if not article:
            return None, None, None

        autor = article.authors[0] if article.authors else ""
        titulo = article.title if article.title else ""
        fecha = article.publish_date.strftime("%Y-%m-%d") if article.publish_date else ""

        return autor, titulo, fecha

    except ArticleException as e:
        print(f"Error al procesar el artículo: {e}")
        return None, None, None

def analizar_url(url):
    try:
        article = Article(url, language='es')
        article.download()
        article.parse()
        return article
    except ArticleException as e:
        print(f"Error al analizar URL: {url}. Error: {e}")
        return None