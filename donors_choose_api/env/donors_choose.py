import json
import requests
url = ("http://api.donorschoose.org/common/json_feed.html?subject1=-1&APIKey=DONORSCHOOSE")
response = requests.get(url)
result = response.json()
def loop_over_json():
    output_file = ""
    for response_value in result:
        #import pdb; pdb.set_trace();
        output_file += "proposals with id: {} and url: {} ".format(result['proposals'][0]['id'], result['proposals'][0]['proposalURL']) + "\n"
        output_file += "title of proposals: {}".format(result['proposals'][0]['title']) + "\n"
        output_file += "short description of proposal".format(result['proposals'][0]['shortDescription']) + "\n\n"
        output_file += "number of donors".format(result['proposals'][0]['numDonors']) + "\n"
        output_file += "percentage funded".format(result['proposals'][0]['percentFunded']) + "\n"
    return output_file
with open("profile.txt", "w") as output:
    output.write(loop_over_json())