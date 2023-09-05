def main():
    #makes filename from input lowercase and removes whitespace
    filename = input("Filename: ").lower().strip()
    typefinder(filename)


def typefinder(name):
    # check if there is at least one . in filename
    if "." in name:
    # split on . and take last entry
        extension = name.split(".")[-1]
    else:
        extension = None

    match extension:
        case "gif":
            print("image/gif")
        case "jpg"|"jpeg":
            print("image/jpeg")
        case "png":
             print("image/png")
        case "pdf":
             print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


main()