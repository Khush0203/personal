f = open('names.txt')
haha = list()
hehe = list()

for line in f:
    names=line.split()
    haha.append(names)


print(haha)




for i in range(0,len(haha)):
    hehe.append(haha[i][1])


print(hehe)




from selenium import webdriver

web = webdriver.Chrome()

web.get("https://www.google.com/?gws_rd=ssl")

searchbox = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys('fuck you')
#haha[0][0]

searchbutton = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
searchbutton.click()
