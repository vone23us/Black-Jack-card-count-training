# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters¶


def paper_doll(text):
    tript = ""

    for i in text:
        tript += i*3

    print(tript)


paper_doll("dicks")

paper_doll("start")
