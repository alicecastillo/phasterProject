# contains main executable
from collections import defaultdict
import spatula, settings, wget_exec
import pandas as pd


#init desired website (this case NCBI)
settings.init("https://www.ncbi.nlm.nih.gov/assembly/%s" %("phage here")) 

# #init web scrape
# spatula.init() 

access = []

#get all access nums from file
f = open("acn_1.txt", "r")
access_soup = f.read()

access_blocks = access_soup.split("\n")

#create dict of all access_nums
access_dict = defaultdict(list)
for ab in access_blocks:
    ab = ab.replace("ID ", "")
    ab = ab.replace(" ", "")
    splitter = ab.split(":")
    id = splitter[0]
    nums = splitter[-1] # for now, keep chained
    access_dict[id] = nums.split(",")

df_list = []
error_list = []
for key, value in access_dict.items():
    for p in value:
      summary_list = wget_exec.runPhaster(p)
      if summary_list:
        for summary in summary_list:
          print("{} region {}".format(p, summary["REGION"]))
          df_dict = {}
          df_dict["ID"] = key
          df_dict["Accession"] = p
          df_dict["Region"] = summary["REGION"]
          df_dict["Region Length"] = summary["REGION_LENGTH"]
          comp_score = summary["COMPLETENESS(score)"].split("(")
          df_dict["Completeness"] = comp_score[0]
          df_dict["Completeness Score"] = comp_score[1].replace(")", "")
          df_dict["# Total Proteins"] = summary["TOTAL_PROTEIN_NUM"]
          df_dict["Region Position"] = summary["REGION_POSITION"]
          mcp = summary["MOST_COMMON_PHAGE_NAME(hit_genes_count)"].split(',')[0]
          if "(" in mcp:
            mcp_list = mcp.split("(")
            df_dict["Most Common Phage (MCP)"] = mcp_list[0]
            df_dict["MCP Occurrences"] = mcp_list[1].replace(")", "")
          else:
            df_dict["Most Common Phage (MCP)"] = mcp
            df_dict["MCP Occurrences"] = None
          df_dict["GC %"] = summary["GC_PERCENTAGE"]
          df_dict["Details"] = "None"
          df_list.append(df_dict)
      else:
        print("ERROR for {}".format(p))
        error_dict = {}
        error_dict["ID"] = key
        error_dict["Accession"] = p
        error_dict["Error"] = "Phaster API backlogged"
        error_list.append(error_dict)



final_df = pd.DataFrame(df_list)
writer = pd.ExcelWriter(path="/Users/alicecastillo/Desktop/phaster_run1.xlsx", engine='xlsxwriter')
final_df.to_excel(writer, sheet_name = "Successful Accession Runs", index=False)
if error_list:
  error_df = pd.DataFrame(error_list)
  error_df.to_excel(writer, sheet_name="Errors", index=False)
writer.save()
print(settings.badAccessions)
