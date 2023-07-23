import requests
def get_url_status(urls): 
    # checks status for each url in list urls
    for url in urls:
        try:
            r = requests.get(url)
            print(url + "\tStatus: " + str(r.status_code))
        except Exception as e:
            print(url + "\tNA FAILED TO CONNECT\t" + str(e))    
            return None

def main():
    urls = ["https://www.example.org"]    
    get_url_status(urls)

if __name__ == "__main__":
    main()
