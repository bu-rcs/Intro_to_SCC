<html>
<head>
    <link rel="stylesheet" href="/css/examples.css">
</head>
<body>

<h3>RCS examples: Processing Markdown file</h3>
<br><br>

The following command will convert the notebook to html<br>
<code style="background:#f2f2f2">
scc1% <b>Rscript -e 'rmarkdown::render("example.Rmd")'</b>
</code><br>
<br><br>

The following command will convert the notebook to pdf format<br>
<code style="background:#f2f2f2">
   scc1% <b>Rscript -e 'rmarkdown::render(input="example.Rmd", output_format="pdf_document",output_file="example.pdf")'</b>
</code><br>

<h4>Contact Information:</h4>
Research Computing Services: <em>help@scc.bu.edu</em>
<br><br>

<!--#include virtual="/css/footer.html" -->
</body>
</html>
