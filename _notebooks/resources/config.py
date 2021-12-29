def generate_query(endpoint_url, query, limit):

    raw_query = (f"{endpoint_url}?$query="
                 f"{query}%20"
                 f"limit {limit}"
                )
    
    # get rid of control characters
    for replacements in ((" ", "%20"), ("\n", "%20")):
        raw_query = raw_query.replace(*replacements)
    
    return raw_query
