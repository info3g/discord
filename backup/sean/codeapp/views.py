from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os,re
import requests
import time
from bs4 import BeautifulSoup as bs
import csv
import re
import os



def index(request):
	if request.method =='POST':
		list_of_user = request.POST.getlist('Nagatar')
		Users = request.POST['Users']
		Passwards = request.POST['Passward']
		Groups = request.POST['Group']
		Nagatar = request.POST['Nagatar']
		RPs = request.POST['RP']
		year = request.POST['years']
		symbol = request.POST['dil']
		democratically = request.POST['democratically']
		Candy = request.POST['Candy']
		Kansas = request.POST['Kansas']
		driver = webdriver.Chrome('chromedriver.exe')
		driver.get('https://discord.com/login')
		user = driver.find_elements_by_xpath('//input[@name="email"]')
		time.sleep(1)
		try:
			for login in user:
				login.send_keys(Users)
		except:
			pass
		
		users = driver.find_elements_by_xpath('//input[@name="password"]')
		time.sleep(1)
		try:
			for logins in users:
				logins.send_keys(Passwards)
		except:
			pass
		login_user = driver.find_elements_by_xpath('//button[@class="marginBottom8-AtZOdT button-3k0cO7 button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeLarge-1vSeWK fullWidth-1orjjo grow-q77ONN"]')
		time.sleep(2)
		try:
			for log in login_user:
				log.click()
		except:
			pass
		
		user_data_add = []
		Group = Groups 
		time.sleep(10)
		try:
		    go_it = driver.find_elements_by_xpath("//body/div[@id='app-mount']/div[6]/div[1]/div[1]/div[1]/div[1]/button[1]")
		    for go in go_it:
		        go.click()
		except:
		    pass
		user_data_add = []
		user = []
		mesage_all = []
		Group = 'Among Us'
		links = driver.find_elements_by_xpath('//div[@class="wrapper-1BJsBx"]')
		for link in links:
			link.click()
			group_name = driver.find_elements_by_xpath('//h1[@class="name-1jkAdW"]')
			Text_Channels = driver.find_elements_by_xpath('//div[@class="overflow-WK9Ogt"]')
			for gruop in group_name:
				gruops = gruop.text
				if gruops == Group:
					for textchannel in Text_Channels: 
							time.sleep(1)
							match = textchannel.text
							if match == 'TEXT CHANNELS':
								time.sleep(1)
								all_channels = driver.find_elements_by_xpath('//div[@class="channelName-2YrOjO"]') 
								time.sleep(1)
								for texts in all_channels:
									time.sleep(3)
									texts.click()
									driver.find_elements_by_xpath('//*[@class="scrollerInner-2YIMLh"]')
									time.sleep(3)
									while True:
										time.sleep(1)
										datt = driver.page_source
										soup = bs(datt, "html.parser")
										data_all = soup.findAll("div", attrs={"class": "contents-2mQqc9"})
										for fin in data_all:
											time.sleep(0.2)
											try:
												text = fin.find("div", attrs={"class": "markup-2BOw-j messageContent-2qWWxC"}).text
												datetime = fin.find("span", attrs={"class": "timestamp-3ZCmNB timestampInline-yHQ6fX"}).text
												user_name = fin.find("span", attrs={"class": "username-1A8OIy desaturateUserColors-1gar-1 clickable-1bVtEA"}).text
												name_date = user_name + str(datetime) + '  '+ text
												if name_date not in user_data_add:
													user_data_add.append(name_date)
											except:
												ele =driver.find_element_by_tag_name('html')
												name_date = user_name + str(datetime) + '  '+ text
												if name_date not in user_data_add:
													user_data_add.append(name_date)
												pass
											print(name_date)
										print("******************************************************************")
										time.sleep(2)
										try:
											stop_Loop = driver.find_element_by_xpath('//*[@class="container-3RCQyg"]').text
											print('stop_Loop:--------------',stop_Loop)
										except:
											stop_Loop = ''
											element = driver.find_element_by_xpath('//*[@class="markup-2BOw-j messageContent-2qWWxC"]')
											driver.execute_script("return arguments[0].scrollIntoView();", element)
											element = driver.find_element_by_xpath('//*[@class="markup-2BOw-j messageContent-2qWWxC"]')
											driver.execute_script("return arguments[0].scrollIntoView();", element)
										if stop_Loop != '':
											print("breakkkkkkkkkkkkkkkkkkkk")
											break
										else:
											element = driver.find_element_by_xpath('//*[@class="markup-2BOw-j messageContent-2qWWxC"]')
											driver.execute_script("return arguments[0].scrollIntoView();", element)
											element = driver.find_element_by_xpath('//*[@class="markup-2BOw-j messageContent-2qWWxC"]')
											driver.execute_script("return arguments[0].scrollIntoView();", element)

		
		user = []
		current_feed = []
		part_one = []
		part_two = []
		part_three = []
		Nagat = Nagatar
		

		for user in user_data_add:
		    for one_by_one in list_of_user:
		        if one_by_one in user:
		            user.append('DISCORD'+' '+tetx.split('  ')[0])
					current_feed.append(tetx.split('  ')[0])
					strings = tetx.split('  ')[1]
					part_one.append(strings.split(Nagatar)[0])
					part_two.append(Nagatar)
					part_three.append(strings.split(Nagatar)[1])

		if Nagatar != '':
			for tetx in user_data_add:
				if Nagatar in tetx:
					user.append('DISCORD'+' '+tetx.split('  ')[0])
					current_feed.append(tetx.split('  ')[0])
					strings = tetx.split('  ')[1]
					part_one.append(strings.split(Nagatar)[0])
					part_two.append(Nagatar)
					part_three.append(strings.split(Nagatar)[1])
			onss = 'Nagatars'

		if RPs != '':
			RPs = 'RPs'
			for tetx in user_data_add:
				if RPs in tetx:
					user.append('DISCORD'+' '+tetx.split('  ')[0])
					current_feed.append(tetx.split('  ')[0])
					strings = tetx.split('  ')[1]
					part_one.append(strings.split(RPs)[0])
					part_two.append(RPs)
					part_three.append(strings.split(RPs)[1])

		
		if year != '':
			year = 'year'
			for tetx in user_data_add:
				if year in tetx:
					user.append('DISCORD'+' '+tetx.split('  ')[0])
					current_feed.append(tetx.split('  ')[0])
					strings = tetx.split('  ')[1]
					part_one.append(strings.split(year)[0])
					part_two.append(year)
					part_three.append(strings.split(year)[1])
		
		if symbol != '':
			symbol = 'symbol'
			for tetx in user_data_add:
				if symbol in tetx:
					user.append('DISCORD'+' '+tetx.split('  ')[0])
					current_feed.append(tetx.split('  ')[0])
					strings = tetx.split('  ')[1]
					part_one.append(strings.split(symbol)[0])
					part_two.append(symbol)
					part_three.append(strings.split(symbol)[1])
		
		if democratically != '':
			democratically = 'democratically'
			for tetx in user_data_add:
				if democratically in tetx:
					user.append('DISCORD'+' '+tetx.split('  ')[0])
					current_feed.append(tetx.split('  ')[0])
					strings = tetx.split('  ')[1]
					part_one.append(strings.split(democratically)[0])
					part_two.append(democratically)
					part_three.append(strings.split(democratically)[1])
		
		if Candy != '':
			Candy = 'Candy'
			for tetx in user_data_add:
				if Candy in tetx:
					user.append('DISCORD'+' '+tetx.split('  ')[0])
					current_feed.append(tetx.split('  ')[0])
					strings = tetx.split('  ')[1]
					part_one.append(strings.split(Candy)[0])
					part_two.append(Candy)
					part_three.append(strings.split(Candy)[1])
		
		
		if Kansas != '':
			Kansas = 'Kansas'
			for tetx in user_data_add:
				if Kansas in tetx:
					user.append('DISCORD'+' '+tetx.split('  ')[0])
					current_feed.append(tetx.split('  ')[0])
					strings = tetx.split('  ')[1]
					part_one.append(strings.split(Kansas)[0])
					part_two.append(Kansas)
					part_three.append(strings.split(Kansas)[1])

		both = zip(user,part_one,part_two,part_three)
		print('mesage_all:--',user)
		print('scraping should be complete')
		return render(request, 'home.html',{'Naga':Nagat,'mess':user,'matching':both,'Kansas':Kansas,'Candy':Candy,'on':onss,'RPs':RPs,'year':year,'symbol':symbol,'democratically':democratically,'current':current_feed})
		
	wait = 'Please wait scraping is progress.'
	return render(request, 'home.html',{'wait':wait})