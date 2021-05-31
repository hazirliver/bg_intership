import argparse
import os


def iterate_over_folders(root_dir: str) -> dict:
    """
    Iterate over subdirectories of root_dir and run check_download_status to each .txt file.

    :param root_dir: path to directory containing folders with download logs
    :type root_dir: str

    :return: dict with keys - folder name, values - list of aborted downloads files
    :rtype: dict
    """
    res_dict = {}
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".txt"):
                file_path = subdir + "/" + file
                aborted_downloads = check_download_status(file_path)
                res_dict[os.path.basename(subdir)] = aborted_downloads

    return res_dict


def check_download_status(file_path: str) -> set:
    """
    Iterate over log file and check each processing RNA-seq file to download status.

    :param file_path: relative path to file to check
    :type file_path: str

    :return: set of accession numbers RNA-seq files that did not download
    :rtype: set
    """
    aborted_list = set()
    with open(file_path, "r") as rep:
        for line in rep:
            if line.startswith("Processing"):
                acc_num = line.split(" ")[1]
            if line.startswith("gid"):
                line = next(rep)
                line = next(rep)
                status_line = line.split("|")
                download_status = status_line[1].strip()
                if download_status == "ERR":
                    aborted_list.add(acc_num)
    return aborted_list


def print_report(res_dict: dict, report_fname: str) -> None:
    """ Create report file containing info about aborted downloads.

    :param res_dict: dict with keys - folder name, values - list of aborted downloads files
    :type res_dict: dict
    :param report_fname: name of file to be created
    :type report_fname: str

    :return: None. Create .txt file in script directory with report_filename filename
    :rtype: None
    """

    with open(report_fname, "w") as aborted_report:
        for acc, aborted_list in res_dict.items():
            if len(aborted_list) == 0:
                continue
            aborted_report.write(acc + ":\n")
            aborted_report.write("\n".join(aborted_list))
            aborted_report.write("\n")


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description="Creates file containing info about aborted downloads.")
    ap.add_argument("-f", help="Folder name where download logs are located. Required argument.", type=str,
                    required=True)
    ap.add_argument("-r", help="Report filename. Default name is aborted_downloads_report.txt.", type=str,
                    required=False)

    opts = ap.parse_args()
    root_folder = opts.f
    report_filename = "aborted_downloads_report.txt" if opts.r is None else opts.r

    try:
        result_dict = iterate_over_folders(root_folder)
        print_report(result_dict, report_filename)
        print("Logs processed successfully. Created file " + report_filename + ".")
    except:
        print("Something went wrong. Check that the files match the expected input.")
