
import sys, os
from pathlib import Path
from Bio import Entrez, SeqIO


# MAIN
###################################################
def main():

    # # 1. Obtenir les séquences depuis une liste de séquences dans un fichier texte.
    fichier = Path("./noAccession.txt")
    try:
        with open(fichier, 'r') as f:
            accessions = [i.rstrip("\n") for i in f.readlines()]
            getSequences(accessions)
    except:
        print('err...')

    # # 2. Fusionner les fichier de séquences en un seul fichier Fasta de séquences multiples.
    # try:
    #     dossier          = Path('./Fasta')
    #     (_, _, fichiers) = next(os.walk(dossier))
    #     fichiers         = [Path(f'{dossier}/{fichier}') for fichier in fichiers]
    #     multiFasta(fichiers) # multiFasta()
    # except:
    #     print(f"Problèmes rencontrés avec l'ouverture des fichiers dans {dossier}")



# Obtenir les séquences
###################################################
def getSequences(accessions):

    # Dossiers pour stocker les fichiers de données
    if not os.path.isdir(Path('./GenBank')): os.mkdir(Path('./GenBank'))
    if not os.path.isdir(Path('./Fasta'))  : os.mkdir(Path('./Fasta'))

    # Pour chaque no d'accession, interroger l'API Entrez du NCBI...
    for id in accessions:
        try:
            Entrez.email = "votre.adresse.courriel@courrier.uqam.ca"
            handle       = Entrez.efetch(db="nucleotide", id=id, rettype="gb")
            record       = SeqIO.read(handle, "genbank")
            SeqIO.write(record, Path(f'./GenBank/{id}.gb'), "gb")     # Enregistrer la fiche au format GenBank
            SeqIO.write(record, Path(f'./Fasta/{id}.fasta'), "fasta") # Enregistrer le fichier de la séquence au format Fasta
            print(f"Fiche {id} téléchargée!")
        except:
            print(f"Problème rencontré avec le numéro d'accession {id}")


# Combiner les séquences en un seul fichier de séquences multiples
###################################################
def multiFasta(fichiers):

    # List des objets SeqIO
    my_records = []

    # Ajout à la liste d'un objet SeqIO par fichier Fasta
    for fichier in fichiers:
        try:
            seq_record = SeqIO.read(fichier, "fasta")
            my_records.append(seq_record)
        except:
            print(f'Problème rencontré avec la lecture de {fichier}')
    
    # Concatenation dans un fichier
    outputFile = Path('./sequences.fasta')
    try   : SeqIO.write(my_records, outputFile, 'fasta')
    except: print('Problème rencontré lors de la concaténation')




# Main Call
###################################################
if __name__ == '__main__': main()