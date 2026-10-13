def build_context(search_json):
    context = ""
    organic = search_json.get("organic",[])
    for i, item in enumerate (organic[:10], start=1):
        context += f"""
        Source {i}

        Title:
        {item.get("title","")}

        Snippet:
        {item.get("snippet","")}

        URL:
        {item.get("links","")}

        -----------------------
        """
    return context