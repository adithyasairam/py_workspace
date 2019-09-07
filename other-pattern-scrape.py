import re
import datetime

line_start_pattern = r"^(\[)(.*?)(\])(\s)(.*?)(:)(.*)$"


all_txt = open('chat.txt')  # exported input file

out_text = open('chat-cleared.txt', 'w')  # cleaned up file

for i, line in enumerate(all_txt):
    match = re.match(line_start_pattern, line)
    if match:
        # print(line)
        matches = match.groups()
        print(len(matches))
        if(len(matches) == 7):
            date = datetime.datetime.strptime(
                matches[1], '%m/%d/%y, %H:%M:%S').strftime("%Y-%m-%d %H:%M:%S")
            user = matches[4]
            out_text.write("\"{0}\", \"{1}\"\n".format(date, user))

out_text.close()
