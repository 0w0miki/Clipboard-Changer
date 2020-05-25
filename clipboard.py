import re
import time
import pyperclip

def changeString(s):
    res = pattern.search(s)

    if res:
        if res.group(2)[0] == "*":
            changed_str = res.group(2)[1:] + ":" + res.group(1) + "*"
        else:
            changed_str = res.group(2) + ":" + res.group(1)
        pyperclip.copy(changed_str)
        print("this is a function",changed_str)
        return changed_str
    else:
        print("this is not a function",s)
        return s

def main():
    last_value = ""
    while True:
        cur_value = pyperclip.paste()
        try:
            if cur_value != last_value:
                cur_value = changeString(cur_value)
                last_value = cur_value
            time.sleep(0.1)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    reg_type = r"\w*\**"
    reg_fun = r"\**\w+"
    reg_param = r"\**\w+"
    reg = r"\s*(" + reg_type + ") (" + reg_fun + "\((" + reg_type + "( \**" + reg_param + ")*,* *)+\));*"
    pattern = re.compile(reg)
    main()