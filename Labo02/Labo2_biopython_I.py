import sys
from Bio import Entrez, SeqIO


# Télécharger une séquence depuis GenBank
def loadFromGenbank(noAccession):
    Entrez.email = 'john.doe@domain.com'
    handle       = Entrez.efetch(db="nucleotide", id=noAccession, rettype="gb")
    rec          = SeqIO.read(handle, "genbank")
    print (rec.format("gb"))   # On affiche le contenu
    print (dir(rec))           # On affiche la liste des méthodes disponibles pour l'objet SeqIO

    fileName = noAccession + ".gb"
    SeqIO.write(rec, fileName, "gb") # Enregistrer la fiche localement

#= ligne de commande
if len(sys.argv) == 2:
    loadFromGenbank(sys.argv[1]) # Attention, ici on passe le numéro d'accession via la console en appelant le programme.
                                 # Vous pouvez essayer avec le numéro d'accession 'AB123456'. Ex. python Labo2_biopython_I.py AB123456