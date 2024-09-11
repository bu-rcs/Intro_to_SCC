# This is a simple R code

print("Hello, World!")


# Print current R version
print(version$version.string)

A <- rnorm(100,0,1)
summary(A)

# Open an output file for a graphics image
#pdf(file="histogram.pdf")
png(file="histogram.png")

   # plot
   hist(A)

# close file
dev.off() # close file



