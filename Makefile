html:
	rm -fr output/*.html output/theme
	pelican -t theme -s settings.py content

publish: html
	cd output && git add . && git commit -m "automated publish" && git push origin master
	echo "Update Complete"
	echo "Don't forget to commit the source tree to Github!"
