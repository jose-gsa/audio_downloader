def read_links(file_path: str) -> list[str]:
    clean_links = []

    with open(file_path, "r") as file:
        for line in file:
            clean_line = line.strip()
            if clean_line:
                clean_links.append(clean_line)

    return clean_links

