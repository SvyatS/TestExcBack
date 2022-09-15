import os
import json


def main():
    data = {}

    try:
        with open("output.json", 'w') as outputfile:
            with os.scandir("pdf_files/") as it:
                for entry in it:
                    if entry.is_file() and entry.name.endswith(".pdf") and entry.name.lower().find("j") == -1:
                        name = entry.name.replace(".pdf", "")
                        data[entry.name] = [i for i in name.split("_")]

                        new_path = os.path.abspath(entry.path)[:-len(entry.name)] + name[-1] + "_" + name[:-2] + ".pdf"
                        os.rename(os.path.abspath(entry.path), new_path)

            with os.scandir("pdf_files/") as it:
                for entry in it:
                    if entry.is_file() and entry.name.endswith(".pdf") and entry.name.lower().find("j") == -1:
                        name = entry.name.replace(".pdf", "")
                        data[entry.name] = [i for i in name.split("_")]

            json.dump(data, outputfile, indent=4)

        print("Completed")
    except:
        print("Completed with error")
    return 0


if __name__ == "__main__":
    main()
