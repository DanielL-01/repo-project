"""
import hitungan.fis.fisika

print(hitungan.fis.fisika.gravity)


from hitungan.fis import fisika

print(fisika.gravity)
"""

from hitungan.fis.fisika import tekanan_tiang, tekanan_pipa

print(tekanan_tiang(100, 20, 10))

print(tekanan_pipa(100, 20))