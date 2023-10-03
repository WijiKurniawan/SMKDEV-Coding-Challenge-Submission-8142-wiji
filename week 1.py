def checkCats(CatsTuti, CatsNining):
    # Salin list CatsTuti dan hapus usia kucing pertama dan dua kucing terakhir
    correctedCatsTuti = CatsTuti[1:-2]

    # Gabungkan data Tuti yang sudah dikoreksi dengan data Nining
    combinedData = correctedCatsTuti + CatsNining

    # Tampilkan informasi tentang usia kucing
    for index, age in enumerate(combinedData, start=1):
        catStatus = "Kucing Dewasa" if age >= 5 else "Kucing Kecil"
        print(f"Kucing Nomor {index} adalah {catStatus}, dan berusia {age} tahun")

# Data uji 1
DataTuti1 = [3, 5, 2, 12, 7]
DataNining1 = [4, 1, 15, 8, 3]
checkCats(DataTuti1, DataNining1)

# Data uji 2
DataTuti2 = [9, 16, 6, 8, 3]
DataNining2 = [10, 5, 6, 1, 4]
checkCats(DataTuti2, DataNining2)
