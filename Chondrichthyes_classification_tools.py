#!/usr/bin/env python
# coding: utf-8


# extract genus names from a fasta alignment and return the classification of each sample

from Bio import SeqIO
Rhino_sequences = list(SeqIO.parse("Rhino_test.fasta", "fasta"))

genus_list=[]
for i in range(0,len(Rhino_sequences)):
    seqID=Rhino_sequences[i].id
    genus=seqID.rsplit("_")[0]
    genus_list.append(genus)
    
import pandas as pd
classification=pd.read_csv("Chondrichthyes_classification.csv",index_col="Genus")

result_order=[]
result_family=[]
for i in genus_list:
    id_class=classification.loc[i]
    id_order=id_class["Order"]
    id_family=id_class["Family"]
    result_order.append(id_order)
    result_family.append(id_family)

df = pd.DataFrame(list(zip(result_order, result_family,genus_list)),
               columns =["Order", "Family","Genus"])

df.to_csv("classification_results.csv")



# extract genus names from a list of samples and return the classification of each sample

import pandas as pd
new_sample=pd.read_csv("samples_20210624.csv",header=None, usecols=[0])
Species_list=new_sample.values.tolist()

genus_list=[]
for i in range(0,len(Species_list)):
    genus=str(Species_list[i]).rsplit(" ")[0].replace("['","")
    genus_list.append(genus)

classification=pd.read_csv("Chondrichthyes_classification.csv",index_col="Genus")

result_order=[]
result_family=[]
for i in genus_list:
    id_class=classification.loc[i]
    id_order=id_class["Order"]
    id_family=id_class["Family"]
    result_order.append(id_order)
    result_family.append(id_family)

df = pd.DataFrame(list(zip(result_order, result_family,genus_list)),
               columns =["Order", "Family","Genus"])

df.to_csv("classification_results2.csv")


# In[ ]:


# extract species names from a fasta alignment

from Bio import SeqIO
Rhino_sequences = list(SeqIO.parse("Rhino_test.fasta", "fasta"))

species_list=[]
for i in range(0,len(Rhino_sequences)):
    seqID=Rhino_sequences[i].id
    species=seqID.rsplit("_")[1]
    species_list.append(species)
species_list




# extract GN numbers from a fasta alignment

from Bio import SeqIO
Rhino_sequences = list(SeqIO.parse("Rhino_test.fasta", "fasta"))

GN_list=[]
for i in range(0,len(Rhino_sequences)):
    seqID=Rhino_sequences[i].id
    GN=seqID.rsplit("_")[2].replace("GN","")
    GN_list.append(GN)
GN_list




# extract genus names from a fasta alignment and return the classification of each sample

from Bio import SeqIO
Rhino_sequences = list(SeqIO.parse("Alignment_20201214_name_updated.fasta", "fasta"))

genus_list=[]
for i in range(0,len(Rhino_sequences)):
    seqID=Rhino_sequences[i].id
    genus=seqID.rsplit("_")[0]
    if genus == "apristurus":
        genus=genus.replace("apristurus", "Apristurus")
    if genus == "wobbegong":
        genus=genus.replace("wobbegong", "")
    if genus == "shark":
        genus=genus.replace("shark", "")
    if genus == "Shark":
        genus=genus.replace("Shark", "")
    genus_list.append(genus)
    
genus_list = list(filter(None, genus_list)) # remove empty items from a list

import pandas as pd
classification=pd.read_csv("Chondrichthyes_classification.csv",index_col="Genus")

result_order=[]
result_family=[]
for i in genus_list:
    id_class=classification.loc[i]
    id_order=id_class["Order"]
    id_family=id_class["Family"]
    result_order.append(id_order)
    result_family.append(id_family)

df = pd.DataFrame(list(zip(result_order, result_family,genus_list)),
               columns =["Order", "Family","Genus"])

df.to_csv("classification_results3.csv", index=False, index_label=False)

