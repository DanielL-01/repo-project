from hitungan.mat.matematika import luas_persegi, luas_lingkaran
gravity = 9.8

def tekanan_tiang(m, x, y):
	return gravity * m /luas_persegi(x, y)

def tekanan_pipa(m, r):
	return m*gravity/luas_lingkaran(r)

