#API KEY  #AIzaSyAnxHAQMnR-fqZAIgAyypVwPT1-r0u7aI8
import requests
def gen_map(long,lat,zoom):
    g = open('static1.png','wb')
    g.write(requests.get(
        'https://maps.googleapis.com/maps/api/staticmap?center=' + str(long)+',' + str(lat)+ ' &zoom=' + str(zoom)+'&size=530x640&scale=1&style=visibility:off&style=feature:road|element:geometry|color:99ff30|visibility:on&sensor=false').content)
    g.close()
gen_map(-37.784002,145.219566,16)