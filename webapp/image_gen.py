#API KEY  #AIzaSyAnxHAQMnR-fqZAIgAyypVwPT1-r0u7aI8
import requests
def gen_map(lat,long,zoom):
    g = open('static1.png','wb')
    g.write(requests.get(
        'https://maps.googleapis.com/maps/api/staticmap?center=' + str(lat)+',' + str(long)+ ' &zoom=' + str(zoom)+'&size=530x640&scale=1&style=visibility:off&style=feature:road|element:geometry|color:99ff30|visibility:on&sensor=false').content)
    g.close()
    f = open('static.png','wb')
    f.write(requests.get(
        'https://maps.googleapis.com/maps/api/staticmap?center='+ str(lat)+',' + str(long)+ ' &zoom=' + str(zoom)+ '&size=530x640').content)
    f.close()
gen_map(-37.93766034904226,145.22606529319148,16)
print("SCAN COMPLETE")

#'https://maps.googleapis.com/maps/api/staticmap?center=-37.93766034904226,145.22606529319148&zoom=16&size=530x640'