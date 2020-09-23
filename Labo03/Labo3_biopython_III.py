import sys
from pathlib import Path
from Bio import Entrez, SeqIO



# Télécharger une fiche GenBank depuis NCBI
def loadFromGenbank(noAccession):
    Entrez.email = 'lemieux.mathieu@courrier.uqam.ca' # Mettez votre propre adresse svp!
    handle       = Entrez.efetch(db="nucleotide", id=noAccession, rettype="gb")
    record       = SeqIO.read(handle, "genbank")
    fileName     = Path(f'./{noAccession}.gb')
    SeqIO.write(record, fileName, "gb") # Enregistrer la fiche localement



# Charger une fiche GenBank à partir de votre poste de travail
def parseGenbank(filepath):
    
    # Accéder au fichier
    record = SeqIO.read(filepath, "genbank")

    # 1. Afficher la séquence uniquement
    print(record.seq); print('-'*50)

    # 2. Afficher les features
    for feature in record.features:
        print (f'Type: {feature.type}; Location: {feature.location}')
        # Si on veut inclure une liste de leurs champs (qualifiers)...
        for qualifier in feature.qualifiers:
            print(f'Qualifier: {qualifier}')
    print('-'*50)

    # 3. Exemple; Obtenir le numéro d'accession du transcrit (mRNA = ARN messager)
    for feature in record.features:
        if feature.type == 'mRNA':
            for qualifier in feature.qualifiers:
                if qualifier == 'transcript_id':
                    print(f"Numéro d'accession du transcrit: {feature.qualifiers[qualifier][0]}")




if __name__ == '__main__':
    # Essayez avec NG_021471.2: 'python Labo3_biopython_III.py NG_021471.2'
    if len(sys.argv) >= 2:
        noAccession = sys.argv[1]                 # Récupérer le numéro d'accession via la console
        loadFromGenbank(noAccession)              # 1. Télécharger la fiche depuis NCBI et enregistrer dans un fichier
        parseGenbank(Path(f'./{noAccession}.gb')) # 2. Charger la fiche depuis le fichier