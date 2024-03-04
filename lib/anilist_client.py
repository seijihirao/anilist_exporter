import requests
import json

LIST_QUERY = '''
query ($username: String, $page: Int) {
  Page(page: $page, perPage: 50) {
    mediaList(userName: $username, type: ANIME, status: COMPLETED) {
      status
      score
      repeat
      createdAt
      media {
        title {
          romaji
          english
        }
      }
    }
  }
}
'''

class AnilistExporter:
    
    url = 'https://graphql.anilist.co'

    """
    Setups the exporter for the {username}
    """
    def __init__(self, username):
        self.variables = {
            'username': username,
            'page': 0
        }

    def export(self, exporter):
        self.variables['page'] = 0
        exporter.export_meta()
        medialist = [None]
        while len(medialist) != 0:
            self.variables['page'] += 1
            response = requests.post(self.url, json={'query': LIST_QUERY, 'variables': self.variables})

            if response.status_code == 200:
                medialist = json.loads(response.content)['data']['Page']['mediaList']
                for media in medialist:
                    exporter.export_media(media)
            else:
                print(response.content)
                break
     
