import json
import requests
import xmltodict
from flatten_dict import flatten

with open("settings.json", "r") as file:
    SETTINGS = json.load(file)

#   REQUESTS:
#       <TrackRequest USERID="ADSFADSGFADG">
#           <TrackID ID="klwlejrgjrg"></TrackID>
#       </TrackRequest>
#
#   RESPONSE:
#       <TrackResponse>
#          <TrackInfo ID="klwlejrgjrg">
#               <TrackSummary> Your item was delivered at 6:50 am on February 6 in BARTOW FL 33830.</TrackSummary>
#               <TrackDetail>February 6 6:49 am NOTICE LEFT BARTOW FL 33830</TrackDetail>
#           </TrackInfo ID="klwlejrgjrg">
#           <TrackSummary There is no record of that mail item. If it was mailed recently, It may not yet be tracked. Please try again later. </TrackSummary>
#       </TrackResponse>
#
#

def get_resp(id):
    REQ = """
        <TrackRequest USERID="{usr}">
            <TrackID ID="{id}"></TrackID>
        </TrackRequest>
    """
    usr=SETTINGS['usps']['key']
    REQUEST = REQ.format(usr = usr, id=id)

    return SETTINGS['usps']['url']+REQUEST

def parse_resp(resp): # lol this needs to be made more abstracted
    resp = resp.content.decode()
    DICT = xmltodict.parse(resp)
    DICT = dict(DICT)
    return dict(dict(DICT['TrackResponse'])['TrackInfo'])

def shipment_info(resp):
    resp = parse_resp(resp)
    ID = 'Package: '+resp['@ID']
    SUMMARY = resp['TrackSummary']
    LATEST = 'UPDATE: '+resp['TrackDetail'][0]
    OLD = 'OLD: ' +' '.join([i for i in resp['TrackDetail'].pop(0)])  
    return  [ID,SUMMARY,LATEST,OLD]

def track(id):
    FORMATED = []
    if isinstance(id,list):
        for i in id:
            t = requests.get(get_resp(i))
            FORMATED.append(shipment_info(t))
            
    elif isinstance(id,str):
        t = requests.get(get_resp(id))
        FORMATED.append(shipment_info(t))
    else:
        #Error handle eventually
        pass
        
    return FORMATED

