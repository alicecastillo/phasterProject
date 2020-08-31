# contains main executable

import spatula, settings, wget_exec

#init desired website (this case NCBI)
settings.init("https://www.ncbi.nlm.nih.gov/assembly/GCF_000006765.1") 

# #init web scrape
# spatula.init() 

wget_exec.runPhaster("CP029097.1") #("NC_000913")
