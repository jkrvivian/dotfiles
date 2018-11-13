import os, json, re, lz4.block

def set_history_path():
    # export firefox history
    cmd = 'export opentabs=$(ls -t ~/.mozilla/firefox*/*/sessionstore-backups/recovery.jsonlz4 | sed q)'
    os.system(cmd)

    # test if export success
    if len(os.environ['opentabs']) == 0:
        quit()
    return


set_history_path();
# read history
f = open(os.environ["opentabs"], "rb")
magic = f.read(8)
jdata = json.loads(lz4.block.decompress(f.read()).decode("utf-8"))
f.close()

# start parsing
for win in jdata.get("windows"):
    for tab in win.get("tabs"):
        i = tab.get("index") - 1
        urls = tab.get("entries")[i].get("title")
        if "YouTube" in urls:
            p = re.compile(" (.*) - YouTube")
            title = p.search(urls).group(1)
            print(title)
