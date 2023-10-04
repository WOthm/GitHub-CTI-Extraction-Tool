import requests

git_token = "YOUR_GITHUB_TOKEN"

# Github CTI extraction tool is used in order to get infos  CTI on Github 

print()
print("Hello, What Github CTI extraction tool can do for you today? ")
user_input = str(input("Choose between one of thoses: Best matches, Better ranked, Most forked, Recent Update: "))
keyword_input = str(input("Optional: (default keyword: CTI) Any specific keywords to add to your research? +keyword1+keyword2... "))
print()

def FCTU():

    if user_input ==  "Best matches":
        URL = f'https://api.github.com/search/repositories?q=cti{keyword_input}&type=repositories'
        return URL
    elif user_input == "Better ranked":
        URL =   f'https://api.github.com/search/repositories?q=cti{keyword_input}&ty+threats&type=repositories&s=stars&o=desc'
        return URL
    elif user_input == "Most forked":
        URL = f'https://api.github.com/search/repositories?q=cti{keyword_input}&type=repositories&s=forks&o=desc'
        return URL
    elif user_input == "Recent Update":   
        URL = f'https://api.github.com/search/repositories?q=cti{keyword_input}&type=repositories&s=updated&o=desc'
        return URL
    else :
        print("The purpose of this tool is to monitor Open source CTI tools on github via CLI")
        print("First choose the critera of your research between the one proposed")
        print("Then add a keyword/keywords respecting the pattern given to filter more ")
        print()
        exit()

headers = {
    'Authorization' : f'token {git_token}',
}

URL = FCTU()

try:
    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for item in data['items']:
            print("-"*100)
            print(f'{str(item["updated_at"].split("T")[0])} {item["full_name"]}: {item["description"]} ')
        
        print("-"*100)
        print()
    else:
        print(f'request failed: {response.status_code}')

except Exception as e:
    print(f'something failed {e}')
