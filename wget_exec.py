import settings
import os, subprocess, json
from classes import PhasterJSON

phaster_io_keys = ["REGION", "REGION_LENGTH", "COMPLETENESS(score)", "SPECIFIC_KEYWORD", "REGION_POSITION", "TRNA_NUM", 
"TOTAL_PROTEIN_NUM", "PHAGE_HIT_PROTEIN_NUM", "HYPOTHETICAL_PROTEIN_NUM", "PHAGE+HYPO_PROTEIN_PERCENTAGE", "BACTERIAL_PROTEIN_NUM", 
"ATT_SITE_SHOWUP", "PHAGE_SPECIES_NUM", "MOST_COMMON_PHAGE_NAME(hit_genes_count)", "FIRST_MOST_COMMON_PHAGE_NUM", 
"FIRST_MOST_COMMON_PHAGE_PERCENTAGE", "GC_PERCENTAGE"]


def runPhaster(seq):
    link = ("http://phaster.ca/phaster_api?acc=%s" %(seq))
    osLink = ("wget \"%s\" -O %s" %(link, settings.jsonFile))
    
    info = os.system(osLink)
    print((osLink))
    print("*******")

    getPhasterJson()



def getPhasterJson():
    with open(settings.jsonFile) as f:
        json_data = json.load(f)
    obj = PhasterJSON(json_data)
    summary = obj.summary.split("---------------------",1)
    summary = cleanSummary(summary[1])
    # print(summary.split('\n'))


def cleanSummary(summary):
    summarySplit = summary.split('\n')
    summarySplit.pop(0)
    cleanDict = dict.fromkeys(phaster_io_keys)
    cleaned = [cleanDict for _ in range(len(summarySplit))]

    for count, region in enumerate(summarySplit):
        details = region.split()
        cleanThis = cleaned[count]
        if len(details) > 1:
            for val, key in enumerate(list(cleanDict.keys())):
                cleanThis[key] = details[val]
            cleaned[count] = cleanThis

    print(cleaned)
    print("*******")


    return cleaned
