import json

movies = []

with open("data.html", "r+") as f:
  lines = f.readlines()
  for line in lines:
    temp = {}
    if '<a class="yt-simple-endpoint style-scope ytd-playlist-video-renderer" href="' in line:
      url = line[84:line.find('">')]
    if '<span id="video-title"' in line:
      title = line[97:line.find(" by Y")]
      temp["url"] = url
      temp["title"] = title
      del url
    if bool(temp) == True: 
      movies.append(temp)

with open("movies.json", "w") as outfile: 
  json.dump(movies, outfile)


# print(movies)