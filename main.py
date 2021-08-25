import play_scraper
import json


def main():
    with open('input_file', 'r', encoding='utf-8') as file:
        for query in file.readlines():
            answer = play_scraper.search(query=query, page=12, detailed=True)
            if answer:
                for app in answer:
                    file = open(f'exit/{app["app_id"]}.json', 'w')
                    out = {}
                    for i, j in app.items():
                        try:
                            j = j.decode('utf-8')
                        except:
                            pass
                        finally:
                            out[i] = j
                    json.dump(out, file, indent=4, sort_keys=True)
            else:
                main()

if __name__ == '__main__':
    main()