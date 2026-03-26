LATEXMK ?= latexmk

.PHONY: pdf clean

pdf:
	$(LATEXMK) -C -output-directory=document source/dpr.tex || true
	$(LATEXMK) -f -pdf -output-directory=document source/dpr.tex || test -f document/dpr.pdf

clean:
	$(LATEXMK) -C -output-directory=document source/dpr.tex || true
