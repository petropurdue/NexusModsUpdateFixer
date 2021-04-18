#There should presumably be two :
#Ways of separating subnumbers:
#   hyphens -
#   periods .

#1. find 2(+?) files with the same title. AND THEY SHOULD BE ZIPPED. (regex end in .zip) This can be determined by taking everything before the first number.
#   1.1 As a failsafe, if the length of the title is too short (<5 characters?) then run until the next number OR end of title.
#2. Find the higher number. While files with the same title exist, remove ones with a lower number than the higher number.
#   2.1 at this point we are still operating with exclusively the zip files.
#   2.2 I suppose it would make sense to remove the non-zip folders as well via the same process
#3. Unzip the remaining folder! At this point the process should be done.


from zipfile import ZipFile


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
