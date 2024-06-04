from youtubeAPI import *
import dlt

pipeline = dlt.pipeline(
    pipeline_name="youtube_comments_pipeline",
    destination="bigquery",
    dataset_name="youtube_comments_data",
)

info = pipeline.run(
    comments_data, table_name="youtube_comments_table", write_disposition="append"
)
