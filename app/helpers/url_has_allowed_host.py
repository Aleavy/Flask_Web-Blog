def url_is_safe(url, allowed_hosts, require_https=False):
    if url is not None:
        url = url.strip()
    if not url:
        return False
    if allowed_hosts is None or allowed_hosts is False:
        return False
    return True