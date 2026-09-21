import pandas as pd
#cars = pd.read_csv("cars.xls")
file.xls

is_visayas = file["Hometown"] == "Visayas"
is_comm = file["Track"] == "Communication"
visayas_columns = ["Name", "Gender", "Math", "Electronics", "Average"]

parta = file.loc[hometown & track, visayas_columns]
print(parta)
print(len(parta))





is_female = file["Gender"] == "Female"
female_columns = ["Name", "Gender", "Math", "Electronics", "Average"]

visfemale = file.loc[is_visayas & is_female, female_columns]
print(visfemale)

isave60 = visfemale["Average"] >= 60
print(visfemale[isave60])
