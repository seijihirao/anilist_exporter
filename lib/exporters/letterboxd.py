from datetime import datetime

class Exporter:
    def export_meta(self):
        return 'Title,Rating10,WatchedDate,Rewatch'

    def export_media(self, media):
        title = media['media']['title']['english']
        if title is None:
            title = media['media']['title']['romaji']
        score = round(media['score'])
        createdAt = datetime.fromtimestamp(media['createdAt']).strftime('%Y-%m-%d')
        repeat = media['repeat']
        return f'{title},{score},{createdAt},{repeat}'

