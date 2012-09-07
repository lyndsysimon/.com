
html:
	rm -fr output/*.html output/theme
	./pelican_r -t theme -s settings.py content
