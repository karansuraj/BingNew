import time, random, os, sys, shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#Set encoding and environment variables
#reload(sys)
#sys.setdefaultencoding('UTF8')
binary = FirefoxBinary('C:/Program Files (x86)/Mozilla Firefox/firefox.exe')
profile_loc = 'dependencies/webdriver-py-profilecopy' #1ndsjjut.default'
start_time = time.time()
profile = webdriver.FirefoxProfile(profile_loc)
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0")
#profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml")

def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f), 
                                    os.path.join(dest, f), 
                                    ignore)
    else:
        shutil.copyfile(src, dest)

#Copying function
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

if (os.name == 'nt'):
	browser = webdriver.Firefox(profile, firefox_binary=binary)
else:
	browser = webdriver.Firefox(profile)
temp_prof_path = browser.firefox_profile.path

print(temp_prof_path)		
try:
	while True:
		# This will fail when the browser is closed.
		browser.execute_script("")
		#recursive_overwrite(temp_prof_path, profile_loc)
		time.sleep(0.02)
# Setting such a wide exception handler is generally not advisable but
# I'm not convinced there is a definite set of exceptions that
# Selenium will stick to if it cannot contact the browser. And I'm not
# convinced the set cannot change from release to release.
except:
	#copytree(temp_prof_path, profile_loc)
	
	has_quit = False
	while not has_quit:
		try:
			# This is to allow Selenium to run cleanup code.
			browser.quit()
			has_quit = True
		except:  # See comment above regarding such wide handlers...
			pass

print("--- Program Runtime: %s seconds ---" % (time.time() - start_time))