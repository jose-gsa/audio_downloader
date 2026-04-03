import os
import file_handler
import downloader


def main():

    links_path = "links.txt"
    destination = "downloads"

    if not os.path.exists(destination):
        os.makedirs(destination)

    print(f"Reading Links from: {links_path}...")
    links_list = file_handler.read_links(links_path)

    if not links_list:
        print("No links found. Aborting")
        return

    # Download Loop
    print(f"Videos found: {len(links_list)}")
    for url in links_list:
        print(f"Stating download of: {url}")
        downloader.download_audio(url, destination)

    print("\n -- Process completed with sucess -- ")


if __name__ == "__main__":
    main()
