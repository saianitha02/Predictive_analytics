library(car)
# set.seed(500)
x <- 1:1000
y1 <- rnorm(1000)
y2 <- rlogis(1000)
y3 <- iris$Petal.Length
y4 <- x*x
y <- y1
plot(y)
hist(y)
qqnorm(y)
qqline(y, col = "darkgreen", lwd = 10)
qqPlot(y)
