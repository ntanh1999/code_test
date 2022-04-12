library(ggplot2)

df <- read.csv('D:/ubuntu/code_test/modifiled.csv', sep = ',', header = TRUE)

p <- ggplot(df, aes(x=depth, y = feature_count, group=depth))
p <- p + geom_boxplot() + facet_wrap(~sample_id)

print(p)