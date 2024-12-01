"""
Wikipedia API Program
"""

import wikipedia


def main():
    print("Wikipedia Search Program")
    while True:
        title = input("Enter page title: ").strip()
        if not title:
            print("Thank you.")
            break
        try:
            # Perform a search to find related pages
            search_results = wikipedia.search(title)
            if not search_results:
                print(f"No results found for \"{title}\". Try another search.")
                continue

            # Fetch the first result's page
            page = wikipedia.page(search_results[0])
            print(f"\n{page.title}")
            print(f"{page.summary[:500]}...")  # Show only the first 500 characters of the summary
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("\nWe need a more specific title. Try one of the following, or a new search:")
            print(e.options)  # Print suggested options
        except wikipedia.exceptions.PageError:
            print(f"\nPage id \"{title}\" does not match any pages. Try another id!")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
