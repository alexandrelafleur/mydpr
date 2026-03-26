LATEXMK ?= latexmk

.PHONY: pdf clean

pdf:
	cd document && $(LATEXMK) -pdf article.tex

clean:
	cd document && $(LATEXMK) -C article.tex || true
