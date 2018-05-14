'''
The following script requires selenium to be installed as a dependency. If you don't have selenium, make sure pip.exe
is on your system's PATH and do a pip install on selenium. Of course google for more details if you need specifics.

The methodology of this code is to run Bing s
'''

import time, random, os, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


binary = FirefoxBinary('C:/Program Files (x86)/Mozilla Firefox/firefox.exe')


file1 = "list1.txt"
file2 = "list2.txt"
start_time = time.time()
#This function pops off (removes from file) the first line of the file and returns it
def pullNdelFileLine1(fname):
    #Open list1 file ignoring unicode errors and read all lines into memory
    lines = open(fname, 'r', encoding='utf-8', errors='ignore').readlines()
    line1 = lines[0]
    file = open(fname, 'w')
    n = 1
    for line in lines:
        if(n==1):
            n+=1
            continue
        file.write(line)
    file.close()
    return line1


def wordFileManipulator(fname1, fname2):
    fo2 = open(fname2, "a+")
    line1 = ""
    if (os.path.getsize(fname1) > 0):
        line1 = pullNdelFileLine1(fname1)
        fo2.write(line1)
        fo2.close()
    else:  # Close file 2, rename it to file 1 and vice versa
        fo2.close()
        os.rename(fname1, fname1 + ".old")
        os.rename(fname2, fname1)
        os.rename(fname1 + ".old", fname2)
    return line1

def bingSearcher(browser, search_string):
    browser.get('http://www.bing.com')
    elem = browser.find_element_by_name('q')  # Find the search box
    time.sleep(randTimeGen()%4+2)
    elem.send_keys(search_string + Keys.RETURN)

def browseMobile(url, how_long, num_searches, prof_loc):
    profile = webdriver.FirefoxProfile(prof_loc)
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3")
    if(os.name=='nt'):
        browser = webdriver.Firefox(profile, firefox_binary=binary)
    else:
        browser = webdriver.Firefox(profile)
    inquiries = range(int(num_searches))
    for number in inquiries:
        bingSearcher(browser, wordFileManipulator(file1, file2))
        time.sleep(randTimeGen()*3)
        print("Mobile search "+str(number+1)+" complete.")
    browser.quit()

def browseDesktop(url, how_long, num_searches, prof_loc):
    profile = webdriver.FirefoxProfile(prof_loc)
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0")
    if (os.name == 'nt'):
        browser = webdriver.Firefox(profile, firefox_binary=binary)
    else:
        browser = webdriver.Firefox(profile)
    inquiries = range(int(num_searches))
    for number in inquiries:
        bingSearcher(browser, wordFileManipulator(file1, file2))
        time.sleep(randTimeGen()*3)
        print("Desktop search "+str(number+1)+" complete.")
    browser.quit()


def randTimeGen():
    randDec = round(random.random()*random.random()*10, random.randint(1,10)) #Random number randomly rounded between 1 and 10
    #print randDec
    '''
    ===To-Do===
    1. Develop strategy for determining time between searches
    2. Develop scheduling system to run searching scripts for a day
    '''
    return randDec

headlessOn = 0
if(os.name!='nt'):
	from pyvirtualdisplay import Display
	display = Display(visible=0, size=(800, 600))
	if (len(sys.argv)>1):
		if(sys.argv[1] == "-h"):
			display.start()
			headlessOn = 1
			print("Running in headless mode...")
        
rootdir = 'profiles'
for dirs in os.listdir(rootdir):
	profile_loc = rootdir+"/"+dirs
	print(rootdir+"/"+dirs)
	browseDesktop('', 0, 155/5, profile_loc)
	browseMobile('', 0, 115/5, profile_loc)
        
        


if(os.name!='nt'):
	if(headlessOn==1): display.stop()
print("--- Program Runtime: %s seconds ---" % (time.time() - start_time))

'''
===To-Do===
- Go to bing rewards dashboard and scrub to see search limit. Set randomizer to calculate number of searches + mod some small number
- Instead of file list of words, go to look up words from some other source
- Maybe generate list of words from some web source and keep it unique to the calculated amount
'''
