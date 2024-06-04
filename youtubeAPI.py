import os
from googleapiclient.discovery import build

YOUTUBE_API_KEY = os.getenv("API_KEY")
VIDEO_ID = "DthGyfkkeVk"

youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

comments_data = []
page_token = None

while True:
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=VIDEO_ID,
        textFormat="plainText",
        pageToken=page_token,
        maxResults=100,
    )
    response = request.execute()

    if "items" in response:
        for item in response["items"]:

            published_date = item["snippet"]["topLevelComment"]["snippet"][
                "publishedAt"
            ]
            comment_text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            author_name = item["snippet"]["topLevelComment"]["snippet"][
                "authorDisplayName"
            ]
            like_count = item["snippet"]["topLevelComment"]["snippet"]["likeCount"]
            total_reply_count = item["snippet"]["totalReplyCount"]
            video_id = item["snippet"]["videoId"]
            comments_data.append(
                {
                    "author": author_name,
                    "text": comment_text,
                    "like_count": like_count,
                    "total_reply_count": total_reply_count,
                    "video_id": video_id,
                    "published_date": published_date,
                }
            )

        if "nextPageToken" in response:
            page_token = response["nextPageToken"]
        else:
            break
