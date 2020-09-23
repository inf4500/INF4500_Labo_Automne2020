import sys
from pathlib import Path
from Bio import Entrez, SeqIO


# Télécharger une séquence Fasta depuis NCBI à l'aide du numéro d'accession
def fastaFromNCBI(noAccession):
    Entrez.email = 'john.doe@domain.com'
    handle       = Entrez.efetch(db="nucleotide", id=noAccession, rettype="fasta")
    rec          = SeqIO.read(handle, "fasta")

    # Afficher le contenu de la requête
    print (rec.format("fasta"))

    # Enregistrer le fichier sur votre poste de travail
    fileName = Path(noAccession + ".fasta")
    SeqIO.write(rec, fileName, "fasta")


# Charger un fichier fasta à partir de votre poste de travail
def fastaFromFilesystem(noAccession):
    fileName = Path(noAccession + ".fasta")
    rec = SeqIO.read(fileName, "fasta")

     # Afficher le contenu du fichier
    print (rec.format("fasta"))


if __name__ == '__main__':
    # Vous pouvez essayer avec le numéro d'accession 'AB123456'.
    # Ex. python Labo3_biopython_II.py AB123456
    if len(sys.argv) >= 2:
        fastaFromNCBI(sys.argv[1])
        # fastaFromFilesystem(sys.argv[1])