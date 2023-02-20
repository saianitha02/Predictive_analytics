library(psych)
setwd("~/GitHub/PA/Data_preparation")

SL <- rnorm(1000, mean = 0, sd = 1)
SL <- iris$Sepal.Width

log_SL <- log(SL)
sqrt_SL <- sqrt(SL)
inv_sqrt_SL <- 1/sqrt_SL

hist(SL)
hist(log_SL)
hist(sqrt_SL)
hist(inv_sqrt_SL)

skew(SL)
skew(log_SL)
skew(sqrt_SL)
skew(inv_sqrt_SL)
