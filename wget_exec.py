import settings, insertions
import os, subprocess, json
from classes import PhasterJSON
import time
import pandas as pd

phaster_io_keys = ["REGION", "REGION_LENGTH", "COMPLETENESS(score)", "SPECIFIC_KEYWORD", "REGION_POSITION", "TRNA_NUM", 
"TOTAL_PROTEIN_NUM", "PHAGE_HIT_PROTEIN_NUM", "HYPOTHETICAL_PROTEIN_NUM", "PHAGE+HYPO_PROTEIN_PERCENTAGE", "BACTERIAL_PROTEIN_NUM", 
"ATT_SITE_SHOWUP", "PHAGE_SPECIES_NUM", "MOST_COMMON_PHAGE_NAME(hit_genes_count)", "FIRST_MOST_COMMON_PHAGE_NUM", 
"FIRST_MOST_COMMON_PHAGE_PERCENTAGE", "GC_PERCENTAGE"]



def runPhaster(seq):
    link = ("http://phaster.ca/phaster_api?acc=%s" %(seq))
    osLink = ("wget \"%s\" -O %s" %(link, settings.jsonFile))
    
    info = os.system(osLink)
    summ = getPhasterJson(seq)
    if summ:
        settings.runTimes += 1
        print("RUN {} TIMES; this was {}".format(settings.runTimes, seq))
        print("*******")
        return summ
    else:
        settings.badAccessions.append(seq)
        print("DELAYED FOR {}".format(seq))
        # time.sleep(61)
        return False



def getPhasterJson(seq):
    with open(settings.jsonFile) as f:
        json_data = json.load(f)
    try:
        obj = PhasterJSON(json_data)
        summary = obj.summary.split("-----------",1)
        summary_large = cleanSummary(summary[1])
        # for summary in summary_large:
        # mc_phage = summary["MOST_COMMON_PHAGE_NAME(hit_genes_count)"].split(',')
        # row = (""""%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s"
        #         """ %(seq, summary["REGION"], summary["REGION_LENGTH"], summary["COMPLETENESS(score)"], summary["COMPLETENESS(score)"], 
        #                 summary["TOTAL_PROTEIN_NUM"], summary["REGION_POSITION"], mc_phage[0], summary["GC_PERCENTAGE"], "None"))
        # insertions.insertRow(row)
        return summary_large
    except Exception as e:
        print("ERROR: {}".format(e))
        return False


def cleanSummary(summary):
    summarySplit = summary.split('\n')
    summarySplit.pop(0)
    cleanDict = dict.fromkeys(phaster_io_keys)
    # cleaned = [cleanDict for _ in range(len(summarySplit))]
    cleaned = []
    for count, region in enumerate(summarySplit):
        details = region.split()
        cleanThis = dict.fromkeys(phaster_io_keys)
        if len(details) > 1:
            for val, key in enumerate(list(cleanThis.keys())):
                cleanThis[key] = details[val]
            cleaned.append(cleanThis)

    return cleaned
