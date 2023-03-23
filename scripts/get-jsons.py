#gets values from all the metadata jsons for HGL records and writes them to a spreadsheet
import os, json
import pandas as pd

path_to_json = '{FILEPATH}/harvard-geodata/json'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
jsons_data = pd.DataFrame(columns=['layerid','title', 'description', 'layertype', 'creator', 'format', 'date', 'desc_date', 'place', 'subject', 'bbox'])

for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)

        layerid = json_text['layer_id_s']
        title = json_text['dc_title_s']
        description = json_text['dc_description_s']
        layertype = json_text['layer_geom_type_s']
        creator = json_text['dc_creator_sm'][0]
        format = json_text['dc_format_s']
        try:
            date = json_text['solr_year_i']
        except KeyError:
            date = "null"
        desc_date = json_text['layer_modified_dt'][0:4]
        try:
            place = json_text['dct_spatial_sm'][0]
        except KeyError:
            place = "null"
        subject = json_text['dc_subject_sm'][0]
        bbox = json_text['solr_geom']
        jsons_data.loc[index] = [layerid, title, description, layertype, creator, format, date, desc_date, place, subject, bbox]

# now that we have the pertinent json data in our DataFrame let's look at it
jsons_data.to_csv('{FILEPATH}/hgl-records-summary.csv')