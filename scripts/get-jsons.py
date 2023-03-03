import os, json
import pandas as pd

path_to_json = '/Users/bellelipton/Documents/GitHub/harvard-geodata/json'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
jsons_data = pd.DataFrame(columns=['title', 'place'])

for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)


        title = json_text['dc_title_s']
        # description = json_text['dc_description_s']
        # layertype = json_text['layer_geom_type_s']
        # creator = json_text['dc_creator_sm'][0]
        # format = json_text['dc_format_s']
        try:
            place = json_text['dct_spatial_sm'][0]
        except KeyError:
            place = "null"
        # subject = json_text['dc_subject_sm'][0]
        # bbox = json_text['solr_geom']
        # here I push a list of data into a pandas DataFrame at row given by 'index'
        jsons_data.loc[index] = [title, place]

# now that we have the pertinent json data in our DataFrame let's look at it
jsons_data.to_csv('/Users/bellelipton/Downloads/data/hgl-records-summary.csv', sep='\t')