


go: *.py
	-mkdir cgi-bin
	cp *.py cgi-bin/
	chmod 755 cgi-bin/*
	python -m CGIHTTPServer
