library(ggplot2)

df <- read.csv('D:/ubuntu/code_test/modifiled.csv', sep = ',', header = FALSE)

p <- ggplot(df, aes(x=V2, y =, fill=V1))
p <- p + geom_boxplot() 

print(p)