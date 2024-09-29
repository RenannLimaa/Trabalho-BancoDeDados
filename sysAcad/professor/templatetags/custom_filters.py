from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Retorna o valor do dicionário para a chave fornecida."""
    if isinstance(dictionary, dict):
        return dictionary.get(key, None)
    return None