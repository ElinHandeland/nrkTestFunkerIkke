import requests
import argparse


def main(brukerNavn):


    #Spørring mot API
    API_call_respons = requests.get(f"https://api.github.com/users/{brukerNavn}/repos") #"Query"
    API_content = API_call_respons.json() #Jsonify API repsons data

    print()

    print(f" Denne kontoen har {len(API_content)} public repository(s)")

    #Dictoneries for hver reposetory
    for index, repo in enumerate(API_content):
        #Printer navn, URL og beskrivelse
        print(f"   {index + 1}: Name: {repo['name']} \n"
              f"         -URL: {repo['html_url']} \n"
              f"         -Description: {repo['description']}")

        #if test på om det er flere enn 0 topics
        if len(repo["topics"]) > 0:
            print(f"         -Her er det {len(repo['topics'])} topics og de er:")
            for indexTopic, topic in enumerate(repo['topics']):
                print(f"              Topic{indexTopic + 1}: {topic}")
        else:
            print('         -Ingen topics og finne her')

        #if test på om det står ikke står null i repo
        if (repo['license']) != None:
            print(f"         -License:")
            print(f"            License Key: {repo['license']['key']}")
            print(f"            License Name: {repo['license']['name']}")
            print(f"            License Spdx_id: {repo['license']['spdx_id']}")
            print(f"            License URL: {repo['license']['url']}")
            print(f"            License Node_id: {repo['license']['node_id']}")
        else:
            print('         -Her finnes det ingen license')

        if (repo['language']) != None:
            print(f"         -Language: {repo['language']}")
            print()
        else:
            print("         -Language er ikke oppgitt")
            print()

if __name__ == "__main__":
    #Parser brukernavn
    ap = argparse.ArgumentParser()
    ap.add_argument("-r", "--repo", required=True, help="Skriv inn brukernavn")

    args = vars(ap.parse_args())
    brukerNavn = args["repo"]

    main(brukerNavn)



