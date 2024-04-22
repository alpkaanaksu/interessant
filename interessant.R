library(rio)
library(stringr)
library(ggplot2)
library(dplyr)

data <- import("_chat.csv") %>%
  mutate(date = as.Date(datetime))

pre2023 <- data %>% filter(date < as.Date("2023-01-01"))
table(pre2023$interessant, pre2023$author)

freq <- data %>%
  filter(interessant) %>%
  group_by(date, author) %>%
  summarise(interessant_count = n()) %>%
  group_by(author) %>%
  mutate(interessant_cumulative = cumsum(interessant_count))


ggplot(freq,
    aes(date, interessant_cumulative, group = author, color = author)
) +
  geom_line() +
  geom_point()
