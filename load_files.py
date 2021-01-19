import csv
import re


data = []

with open("data.csv", "r") as datafile:
    data = [
        row[:9]
        + [re.findall(r"((?:January|February) \d{1,2}(?:st|th|nd))", "".join(row[9:]))]
        for row in csv.reader(datafile)
    ]

dict_data = [
    {
        "Email": row[1],
        "First": row[2],
        "Last": row[3],
        "ANS 281": row[6],
        "PVMA": row[8],
        "ANS": row[7],
        "Dates": row[9],
    }
    for row in data[1:]
]

dict_data = sorted(dict_data, key=lambda i: (i["Last"], i["First"]))

for date in (
    "January 21st",
    "January 28th",
    "February 4th",
    "February 11th",
):
    with open(f"{date.replace(' ', '_')}_roster.csv", "w") as output_file:
        # output_file.write("Email,First,Last,ANS,PVMA,ANS 281\n")
        out = csv.DictWriter(
            output_file, ["Email", "First", "Last", "ANS", "PVMA", "ANS 281"]
        )
        out.writeheader()
        for row in dict_data:
            dates = row.pop("Dates")
            if date in dates:
                out.writerow(row)
            row["Dates"] = dates
