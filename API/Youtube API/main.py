import os
import googleapiclient.discovery
import googleapiclient.errors

# adding the limitations to Django query
# type should be movie, runtime should > 1hr, 

def search_trailer(query, x='network'):

    # To save the api key on your computer, run this locally in the venv: export api_key="API_KEY_HERE"
    api_service_name = "youtube"
    api_version = "v3"
    api_key = os.environ.get('api_key')

    # creating Youtube Resource Object 
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = api_key)

    # calling the search.list method to retrieve youtube search results 

    search_term = query+" Official Trailer" + x
    # search_term = 'intitle:'+'"'+query+'"' + ' official trailer ' + x

    search_keyword = youtube.search().list(
        part="snippet",
        maxResults=5,
        q=search_term, 
        type="video",
        videoEmbeddable="true",
        videoDuration="short"
        # order = "relevance" # videoCount Channels are sorted in descending order of their number of uploaded videos.
                            # viewCount – Resources are sorted from highest to lowest number of views. For live broadcasts, videos are sorted by number of concurrent viewers while the broadcasts are ongoing.
    ).execute() 

    # Get the name & url of the results
    results = search_keyword.get("items", []) 
    videos=[]
    videos_url=[]

    for result in results: 
            videos.append("name: %s, embed_url: https://www.youtube-nocookie.com/embed/%s" % 
                            (result["snippet"]["title"], result["id"]["videoId"]))  
            videos_url.append(("https://www.youtube-nocookie.com/embed/%s")% (result["id"]["videoId"]))

    return videos
