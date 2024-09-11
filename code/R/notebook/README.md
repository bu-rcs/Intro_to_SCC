# Processing Markdown file


The following command will convert the notebook to html<br>
```
[scc1$ ] Rscript -e 'rmarkdown::render("example.Rmd")'
```


The following command will convert the notebook to pdf format<br>
```   
[scc1$ ] Rscript -e 'rmarkdown::render(input="example.Rmd", output_format="pdf_document",output_file="example.pdf")'
```
