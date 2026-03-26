PYTHON ?= python3
LATEXMK ?= latexmk

.PHONY: evidence pdf refresh refresh-pdf clean

refresh:
	./scripts/refresh-thesis-evidence.sh

refresh-pdf:
	./scripts/refresh-thesis-evidence.sh --pdf

evidence:
	$(PYTHON) scripts/extract_thesis_evidence.py
	$(PYTHON) scripts/refresh_test_llms_reporting.py
	$(PYTHON) scripts/extract_test_llms_evidence.py

pdf: evidence
	cd document && $(LATEXMK) -pdf memoire.tex

clean:
	cd document && $(LATEXMK) -C memoire.tex || true
	rm -f source/tableaux_et_figures/*.tex generated/notes/*.md
