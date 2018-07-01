import csv
def main():
    csv_file = open("--path--", "r", encoding = "UTF-8", errors = "", newline = "")
    f = csv.reader(csv_file, delimiter = ",", skipinitialspace = True, doublequote = True, lineterminator = "\r\n", quotechar = '"')
    
    csv_out_file = open("--path--", "w", encoding = "UTF-8")
    writer = csv.writer(csv_out_file, lineterminator = '\n')
    header = ["Date", "Time", "Temperature"]
    writer.writerow(header)

    header = next(f)
    for row in f:
        idx = row[0].rfind(r" ")
        result = row[0][:idx] + "," + row[0][idx:len(row[0])]
        result = result.replace(" ", "")
        dt = result.split(",")   #datatime
        
        dt[0] = dt[0].replace("/", "-")
        list_r = []
        list_r.append(dt[0])
        list_r.append(dt[1])
        list_r.append(row[1])
        writer.writerow(list_r)


if __name__ == "__main__":
    main()
