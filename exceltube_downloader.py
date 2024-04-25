from pytube import YouTube
import pandas as pd

# Make sure to specify the file paths below. Leaving them blank will result in errors.
excel_path = ""
sheet_name = ""
column_name = ""
download_path = ""

excel_data = pd.read_excel(excel_path, sheet_name=sheet_name)
column_data = excel_data[column_name]
links = column_data.values

for link in links:
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    video.download(download_path)
    
print("Videos have been downloaded successfully")



