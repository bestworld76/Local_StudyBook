library(tidyverse)
ggplot(data = mpg) +
  geom_point(mapping = aes(x=displ, y=hwy))

# 1.2.4 연습문제
# 1. ggplot(data=mpg)을 실행하라, 무엇이 나타나는가?
ggplot(data=mpg)
# 2. mpg는 행이 몇개인가? 열은 몇개인가?
str(mpg)
# 1.3 심미성 매핑
ggplot(data = mpg) +
  geom_point(mapping = aes(x=displ, y=hwy, color = class))

ggplot(data = mpg) +
  geom_point(mapping = aes(x=displ, y=hwy, size = class))

# 위
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y=hwy, alpha=class))
# 아래
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y=hwy, shape=class))