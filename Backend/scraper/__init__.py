from main import main
import sys
import asyncio

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('Usage: python -m package_name url search_text endpoint')
        sys.exit(1)

    url = sys.argv[1]
    search_text = sys.argv[2]
    endpoint = sys.argv[3]

 
    asyncio.run(main(url, search_text, endpoint))
