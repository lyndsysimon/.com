html:
	rm -fr output/*.html output/theme
	./pelican_r -t theme -s settings.py content

publish: html
	cd output && git add . && git commit -m "automated publish" && git push origin master